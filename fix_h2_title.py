import os
import re

def fix_h2_title_in_file(file_path):
    """ファイル内の最初のH2タグを「## 問題」に変更する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 元のコンテンツをバックアップ
        original_content = content
        
        # 最初のH2タグ（## で始まる行）を見つけて「## 問題」に変更
        # パターン: 行の始めにある「##」で始まる最初の行
        lines = content.split('\n')
        modified = False
        
        for i, line in enumerate(lines):
            # 行の先頭が ## で始まる場合（空白を除く）
            if re.match(r'^\s*##\s+', line):
                # 現在の内容を取得
                current_h2 = line.strip()
                
                # 既に「## 問題」の場合はスキップ
                if current_h2 == "## 問題":
                    break
                
                # 最初のH2タグを「## 問題」に変更
                lines[i] = "## 問題"
                modified = True
                print(f"   📝 変更: '{current_h2}' → '## 問題'")
                break
        
        if modified:
            # 変更された内容を結合
            new_content = '\n'.join(lines)
            
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
    print("🔧 最初のH2タグ → 「## 問題」統一開始")
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
                
                if fix_h2_title_in_file(file_path):
                    changed_files.append(file_path)
                    print(f"✅ 変更完了: {os.path.basename(file_path)}")
                else:
                    print(f"⚪ 変更なし: {os.path.basename(file_path)}")
    
    # 結果の表示
    print("\n" + "=" * 60)
    print("🎉 H2タイトル統一処理完了！")
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
    
    print(f"\n🎯 統一内容:")
    print(f"   📝 変更例:")
    print(f"      '## 四択_①' → '## 問題'")
    print(f"      '## 複数選択' → '## 問題'")
    print(f"      '## 記述式' → '## 問題'")
    print(f"      '## その他のタイトル' → '## 問題'")

if __name__ == "__main__":
    main() 