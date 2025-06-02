import streamlit as st
import random
import os
import glob
import re

def extract_question_content(content):
    """問題文と選択肢の部分だけを抽出する"""
    # 四択・複数選択問題：##問題から##正解まで
    # 記述式問題：##問題から##解答例まで
    
    # まず記述式問題のパターンを試す
    pattern_descriptive = r'(##\s*問題.*?)##\s*解答例'
    match = re.search(pattern_descriptive, content, re.DOTALL | re.IGNORECASE)
    
    if match:
        return match.group(1).strip()
    
    # 次に四択・複数選択問題のパターンを試す
    pattern_choice = r'(##\s*問題.*?)##\s*正解'
    match = re.search(pattern_choice, content, re.DOTALL | re.IGNORECASE)
    
    if match:
        return match.group(1).strip()
    
    # どちらのパターンにもマッチしない場合は元のコンテンツを返す
    return content

st.write("Generative AI Test 学習アプリ") 

# 出題ボタンを設置
if st.button("生成AIのリスク"):
    # data\problems\生成AIのリスクからランダムに問題を出題
    problem_dir = "data/problems/生成AIのリスク"
    
    # すべてのmarkdownファイルを取得
    md_files = []
    for root, dirs, files in os.walk(problem_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    if md_files:
        # ランダムに問題ファイルを選択
        selected_file = random.choice(md_files)
        
        # ファイル名を表示
        st.write(f"**出題ファイル:** {os.path.basename(selected_file)}")
        
        # ファイル内容を読み取って表示
        try:
            with open(selected_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 問題文と選択肢の部分だけを抽出
            question_content = extract_question_content(content)
            st.markdown(question_content)
            
        except Exception as e:
            st.error(f"ファイルの読み取りエラー: {e}")
    else:
        st.error("問題ファイルが見つかりません。")


