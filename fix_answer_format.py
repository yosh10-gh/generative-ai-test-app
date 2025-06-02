import os
import re

def fix_answer_format_in_file(file_path):
    """ファイル内の「答え：」を「## 正解」に変更する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 元のコンテンツをバックアップ
        original_content = content
        
        # 「答え：」を「## 正解」に変更
        # パターン1: 行の始めにある「答え：」
        content = re.sub(r'^答え：', '## 正解', content, flags=re.MULTILINE)
        
        # パターン2: 空白の後にある「答え：」も対応
        content = re.sub(r'^(\s*)答え：', r'\1## 正解', content, flags=re.MULTILINE)
        
        # 変更があった場合のみファイルを更新
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"❌ エラー: {file_path} - {e}")
        return False

def main():
    """メイン処理"""
    print("=" * 60)
    print("🔧 「答え：」→「## 正解」形式変換開始")
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
                
                print(f"📄 処理中: {file_path}")
                
                if fix_answer_format_in_file(file_path):
                    changed_files.append(file_path)
                    print(f"✅ 変更完了: {os.path.basename(file_path)}")
                else:
                    print(f"⚪ 変更なし: {os.path.basename(file_path)}")
    
    # 結果の表示
    print("\n" + "=" * 60)
    print("🎉 変換処理完了！")
    print("=" * 60)
    print(f"📊 処理結果:")
    print(f"   📁 処理したファイル数: {total_files}")
    print(f"   ✅ 変更されたファイル数: {len(changed_files)}")
    print(f"   ⚪ 変更なしファイル数: {total_files - len(changed_files)}")
    
    if changed_files:
        print(f"\n📝 変更されたファイル一覧:")
        for i, file_path in enumerate(changed_files, 1):
            print(f"   {i:2d}. {os.path.basename(file_path)}")
            if i >= 10:  # 最初の10件のみ表示
                remaining = len(changed_files) - 10
                if remaining > 0:
                    print(f"   ... 他 {remaining} 件")
                break
    
    print(f"\n🎯 変換内容:")
    print(f"   📝 変更前: 答え：A")
    print(f"   📝 変更後: ## 正解")
    print(f"            A")

if __name__ == "__main__":
    main() 