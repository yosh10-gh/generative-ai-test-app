import os
import re

def fix_choice_spacing_in_file(file_path):
    """ファイル内の選択肢間に改行を追加する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 元のコンテンツをバックアップ
        original_content = content
        
        # 選択肢のパターンを検出して改行を追加
        # パターン: A. B. C. D. E. などの選択肢
        # 改行なしで連続している場合に改行を追加
        
        # 選択肢パターン: 行の始めにA. B. C. D. E.がある場合
        lines = content.split('\n')
        new_lines = []
        modified = False
        
        for i, line in enumerate(lines):
            # 現在の行を追加
            new_lines.append(line)
            
            # 現在の行が選択肢（A. B. C. D. E.で始まる）かチェック
            if re.match(r'^\s*[A-E]\.\s+', line):
                # 次の行も選択肢かチェック
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    # 次の行も選択肢で、かつ空行でない場合
                    if re.match(r'^\s*[A-E]\.\s+', next_line) and next_line.strip() != "":
                        # 空行を追加
                        new_lines.append("")
                        modified = True
                        print(f"   📝 改行追加: '{line.strip()[:30]}...' の後")
        
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
    print("🔧 選択肢間改行追加処理開始")
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
                
                if fix_choice_spacing_in_file(file_path):
                    changed_files.append(file_path)
                    print(f"✅ 変更完了: {os.path.basename(file_path)}")
                else:
                    print(f"⚪ 変更なし: {os.path.basename(file_path)}")
    
    # 結果の表示
    print("\n" + "=" * 60)
    print("🎉 選択肢間改行追加処理完了！")
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
    print(f"      A. 選択肢1")
    print(f"      B. 選択肢2")
    print(f"      C. 選択肢3")
    print(f"")
    print(f"   📝 変更後:")
    print(f"      A. 選択肢1")
    print(f"")
    print(f"      B. 選択肢2")
    print(f"")
    print(f"      C. 選択肢3")

if __name__ == "__main__":
    main() 