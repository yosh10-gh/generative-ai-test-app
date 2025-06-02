import re

def extract_question_content(content):
    """問題文と選択肢の部分だけを抽出する"""
    pattern_descriptive = r'(##\s*問題.*?)例'
    match = re.search(pattern_descriptive, content, re.DOTALL | re.IGNORECASE)
    
    if match:
        return match.group(1).strip()
    return content

def get_first_10_chars(text):
    """文字列の最初の10文字を取得"""
    return text[:10]

def get_first_n_chars(text, n):
    """文字列の最初のn文字を取得"""
    return text[:n]

# テスト用のサンプルデータ
print("=" * 50)
print("🔤 最初の10文字取得テスト")
print("=" * 50)

# サンプル文章
sample_text = """##問題
生成AIとは何ですか？詳しく説明してください。

具体的には以下の点について述べてください：
- 定義
- 特徴
- 応用例

## 解答例"""

print("\n📝 元の文章:")
print(sample_text)

# 問題文を抽出
extracted = extract_question_content(sample_text)
print(f"\n📦 抽出された問題文:")
print(f"'{extracted}'")
print(f"📏 文字数: {len(extracted)} 文字")

# 最初の10文字を取得
first_10 = get_first_10_chars(extracted)
print(f"\n🔟 最初の10文字:")
print(f"'{first_10}'")
print(f"📏 文字数: {len(first_10)} 文字")

print("\n" + "=" * 50)
print("🧪 様々なパターンのテスト")
print("=" * 50)

# テストケース1: 短い文字列
short_text = "短い文字列"
print(f"1️⃣ 短い文字列の場合:")
print(f"   元の文字列: '{short_text}' ({len(short_text)}文字)")
print(f"   最初の10文字: '{get_first_10_chars(short_text)}'")

# テストケース2: 長い文字列
long_text = "これは非常に長い文字列です。10文字を超えています。"
print(f"\n2️⃣ 長い文字列の場合:")
print(f"   元の文字列: '{long_text}' ({len(long_text)}文字)")
print(f"   最初の10文字: '{get_first_10_chars(long_text)}'")

# テストケース3: 空文字列
empty_text = ""
print(f"\n3️⃣ 空文字列の場合:")
print(f"   元の文字列: '{empty_text}' ({len(empty_text)}文字)")
print(f"   最初の10文字: '{get_first_10_chars(empty_text)}'")

# テストケース4: 改行を含む文字列
multiline_text = "##問題\n生成AI\nとは"
print(f"\n4️⃣ 改行を含む文字列の場合:")
print(f"   元の文字列: '{multiline_text}' ({len(multiline_text)}文字)")
print(f"   最初の10文字: '{get_first_10_chars(multiline_text)}'")

print("\n" + "=" * 50)
print("🔧 可変長文字取得のテスト")
print("=" * 50)

test_text = "生成AIの技術について学習しましょう"
for n in [5, 10, 15, 20]:
    result = get_first_n_chars(test_text, n)
    print(f"最初の{n:2d}文字: '{result}' ({len(result)}文字)")

print("\n" + "=" * 50)
print("💡 実用的な使い方")
print("=" * 50)

def extract_and_preview(content, preview_length=10):
    """問題文を抽出して、プレビュー表示用に短縮"""
    # 問題文を抽出
    extracted = extract_question_content(content)
    
    # 最初のn文字を取得
    preview = extracted[:preview_length]
    
    # 短縮された場合は「...」を追加
    if len(extracted) > preview_length:
        preview += "..."
    
    return {
        'full_text': extracted,
        'preview': preview,
        'is_truncated': len(extracted) > preview_length
    }

# 実用例
result = extract_and_preview(sample_text, 15)
print(f"📄 完全版: '{result['full_text'][:50]}...'")
print(f"👁️ プレビュー: '{result['preview']}'")
print(f"✂️ 短縮された: {result['is_truncated']}")

print("\n" + "=" * 50)
print("🎉 テスト完了！")
print("=" * 50) 