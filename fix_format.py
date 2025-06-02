import os
import re

def fix_format_in_file(file_path):
    """ファイル内のA) B) C) D) E)形式をA. B. C. D. E.形式に変更する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 元のコンテンツをバックアップ
        original_content = content
        
        # A) B) C) D) E) を A. B. C. D. E. に変更
        content = re.sub(r'^([A-E])\)', r'\1.', content, flags=re.MULTILINE)
        
        # 正解の部分も修正（例：「答え A)」→「答え A」、「正解 B)」→「正解 B」）
        content = re.sub(r'(答え\s+)([A-E])\)', r'\1\2', content)
        content = re.sub(r'(正解\s+)([A-E])\)', r'\1\2', content)
        
        # 解説内の選択肢参照も修正（例：「- A) 説明」→「- A. 説明」）
        content = re.sub(r'^(\s*-\s*)([A-E])\)', r'\1\2.', content, flags=re.MULTILINE)
        
        # 変更があった場合のみファイルを更新
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"修正完了: {file_path}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"エラー: {file_path} - {e}")
        return False

def fix_all_markdown_files(root_dir):
    """指定されたディレクトリ以下のすべてのMarkdownファイルを修正する"""
    fixed_count = 0
    total_count = 0
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                total_count += 1
                if fix_format_in_file(file_path):
                    fixed_count += 1
    
    print(f"\n修正完了: {fixed_count}/{total_count} ファイル")

if __name__ == "__main__":
    # 問題ディレクトリを指定
    problems_dir = "data/problems"
    
    print("A) B) C) D) E) 形式を A. B. C. D. E. 形式に修正中...")
    fix_all_markdown_files(problems_dir)
    print("修正作業が完了しました！") 