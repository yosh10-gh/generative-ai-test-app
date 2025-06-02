import re

def extract_question_content(content):
    """問題文と選択肢の部分だけを抽出する"""
    # 四択・複数選択問題：##問題から##正解まで
    # 記述式問題：##問題から##解答例まで
    
    # まず記述式問題のパターンを試す
    pattern_descriptive = r'(.*?)####################'
    match = re.search(pattern_descriptive, content, re.DOTALL | re.IGNORECASE)
    
    if match:
        print("✅ 記述式問題のパターンにマッチしました！")
        return match.group(1).strip()
    
    # どちらのパターンにもマッチしない場合は元のコンテンツを返す
    print("❌ どのパターンにもマッチしませんでした")
    return content

# テスト用のサンプルデータ
sample_descriptive = """# タイトル

問題
生成AIとは何ですか？詳しく説明してください。

具体的には以下の点について述べてください：
- 定義
- 特徴
- 応用例

####################解答例
生成AIとは、新しいコンテンツを自動的に生成する人工知能技術です...

## 参考資料
- 論文1
- 論文2
"""

result1 = extract_question_content(sample_descriptive)
print("抽出結果:")
print(result1)
