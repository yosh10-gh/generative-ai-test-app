import os
import re

def fix_answer_format_in_file(file_path):
    """ファイル内の「回答：」を「## 解答例」に変更する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 元のコンテンツをバックアップ
        original_content = content
        
        # 「回答：」を「## 解答例」に変更
        # パターン: 行の始めにある「回答：」
        lines = content.split('\n')
        new_lines = []
        modified = False
        
        for line in lines:
            # 「回答：」で始まる行を検出
            if re.match(r'^\s*回答：\s*$', line):
                # 「## 解答例」に変更
                new_lines.append("## 解答例")
                modified = True
                print(f"   📝 変更: '{line.strip()}' → '## 解答例'")
            else:
                new_lines.append(line)
        
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
    print("🔧 記述式問題「回答：」→「## 解答例」変更開始")
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
                
                if fix_answer_format_in_file(file_path):
                    changed_files.append(file_path)
                    print(f"✅ 変更完了: {os.path.basename(file_path)}")
                else:
                    print(f"⚪ 変更なし: {os.path.basename(file_path)}")
    
    # 結果の表示
    print("\n" + "=" * 60)
    print("🎉 記述式問題回答形式変更処理完了！")
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
    print(f"   📝 変更前: '回答：'")
    print(f"   📝 変更後: '## 解答例'")

if __name__ == "__main__":
    main() 