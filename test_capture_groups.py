import re

# テスト用のサンプル文章
sample_text = """##問題
生成AIとは何ですか？詳しく説明してください。

具体的には以下の点について述べてください：
- 定義
- 特徴
- 応用例

## 解答例"""

print("=" * 60)
print("🔍 キャプチャグループの違いテスト")
print("=" * 60)

print("\n📝 元の文章:")
print(sample_text)

print("\n" + "=" * 60)

# パターン1: (##\s*問題.*?)例
print("🅰️ パターン1: r'(##\\s*問題.*?)例'")
print("   ↑ カッコが「##問題」から始まる")
pattern1 = r'(##\s*問題.*?)例'
match1 = re.search(pattern1, sample_text, re.DOTALL)

if match1:
    print("✅ マッチしました！")
    print(f"📦 group(0) (全体): '{match1.group(0)}'")
    print(f"📦 group(1) (カッコ内): '{match1.group(1)}'")
    print(f"📏 group(1)の長さ: {len(match1.group(1))} 文字")
else:
    print("❌ マッチしませんでした")

print("\n" + "-" * 60)

# パターン2: ##\s*問題(.*?)例  
print("🅱️ パターン2: r'##\\s*問題(.*?)例'")
print("   ↑ カッコが「問題」の後から始まる")
pattern2 = r'##\s*問題(.*?)例'
match2 = re.search(pattern2, sample_text, re.DOTALL)

if match2:
    print("✅ マッチしました！")
    print(f"📦 group(0) (全体): '{match2.group(0)}'")
    print(f"📦 group(1) (カッコ内): '{match2.group(1)}'")
    print(f"📏 group(1)の長さ: {len(match2.group(1))} 文字")
else:
    print("❌ マッチしませんでした")

print("\n" + "=" * 60)
print("🎯 重要な違い")
print("=" * 60)

if match1 and match2:
    print("🅰️ パターン1で取得される内容:")
    print("   →「##問題」から始まる完全な問題文")
    print("   → HTMLのヘッダー（##）も含まれる")
    print()
    print("🅱️ パターン2で取得される内容:")  
    print("   →「問題」の後から始まる内容のみ")
    print("   → HTMLのヘッダー（##問題）は含まれない")
    print()
    print("📊 実際の使い分け:")
    print("   🅰️ → 問題のタイトルも含めて表示したい場合")
    print("   🅱️ → 問題の内容だけを取り出したい場合")

print("\n" + "=" * 60)
print("🔧 実用例での比較")
print("=" * 60)

# 実用例での使い方
def extract_with_pattern1(content):
    pattern = r'(##\s*問題.*?)例'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else content

def extract_with_pattern2(content):
    pattern = r'##\s*問題(.*?)例'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else content

result1 = extract_with_pattern1(sample_text)
result2 = extract_with_pattern2(sample_text)

print("🅰️ パターン1の結果（##問題も含む）:")
print(f"'{result1}'")
print()
print("🅱️ パターン2の結果（内容のみ）:")
print(f"'{result2}'")

print("\n" + "=" * 60)
print("💡 どちらを選ぶべき？")
print("=" * 60)
print("🎯 Streamlitアプリの場合:")
print("   → パターン1（現在使用中）がおすすめ！")
print("   → 理由: 「## 問題」というタイトルも表示されて分かりやすい")
print()
print("📝 内容だけ欲しい場合:")
print("   → パターン2を使用")
print("   → 理由: 純粋な問題文だけが取得できる") 