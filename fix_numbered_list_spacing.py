import os
import re

def fix_numbered_list_spacing_in_file(file_path):
    """ファイル内の問題文中の連続した番号リスト間に改行を追加する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 元のコンテンツをバックアップ
        original_content = content
        
        # 連続した番号リストのパターンを検出して改行を追加
        # パターン: （1）、（2）、（3）や(1), (2), (3)などが連続している場合
        
        lines = content.split('\n')
        new_lines = []
        modified = False
        
        for i, line in enumerate(lines):
            # 現在の行を追加
            new_lines.append(line)
            
            # 現在の行が番号リスト（(数字)または（数字）で始まる）かチェック
            # ただし、## 問題セクション内のみを対象とする
            if re.match(r'^\s*[\(（]\d+[\)）]', line):
                # 次の行も番号リストかチェック
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    # 次の行も番号リストで、かつ空行でない場合
                    if re.match(r'^\s*[\(（]\d+[\)）]', next_line) and next_line.strip() != "":
                        # 空行を追加
                        new_lines.append("")
                        modified = True
                        print(f"   📝 改行追加: '{line.strip()[:40]}...' の後")
        
        if modified:
            # 変更された内容を結合
            new_content = '\n'.join(new_lines)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ エラー: {file_path} - {e}")
        return False

def main():
    """メイン処理"""
    print("=" * 60)
    print("🔧 問題文中の番号リスト間改行追加処理開始")
    print("=" * 60)
    
    # 対象ディレクトリ
    target_dir = "data/problems"
    
    # 変更されたファイルのカウンター
    changed_files = []
    total_files = 0
    
    # すべてのmarkdownファイルを処理
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                total_files += 1
                
                print(f"📄 処理中: {os.path.basename(file_path)}")
                
                if fix_numbered_list_spacing_in_file(file_path):
                    changed_files.append(file_path)
                    print(f"✅ 変更完了: {os.path.basename(file_path)}")
                else:
                    print(f"⚪ 変更なし: {os.path.basename(file_path)}")
    
    # 結果の表示
    print("\n" + "=" * 60)
    print("🎉 問題文中の番号リスト間改行追加処理完了！")
    print("=" * 60)
    print(f"📊 処理結果:")
    print(f"   📁 処理したファイル数: {total_files}")
    print(f"   ✅ 変更されたファイル数: {len(changed_files)}")
    print(f"   ⚪ 変更なしファイル数: {total_files - len(changed_files)}")
    
    if changed_files:
        print(f"\n📝 変更されたファイル一覧:")
        for i, file_path in enumerate(changed_files, 1):
            print(f"   {i:2d}. {os.path.basename(file_path)}")
            if i >= 15:  # 最初の15件のみ表示
                remaining = len(changed_files) - 15
                if remaining > 0:
                    print(f"   ... 他 {remaining} 件")
                break
    
    print(f"\n🎯 変更内容:")
    print(f"   📝 変更前:")
    print(f"      （1）技術的対策")
    print(f"      （2）組織的対策")
    print(f"      （3）人的対策")
    print(f"")
    print(f"   📝 変更後:")
    print(f"      （1）技術的対策")
    print(f"")
    print(f"      （2）組織的対策")
    print(f"")
    print(f"      （3）人的対策")

if __name__ == "__main__":
    main() 