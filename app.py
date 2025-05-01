from dotenv import load_dotenv
load_dotenv()


# 以下よりコード

# filepath: /Users/shuma/calf Dropbox/Hirose Shuma/Plogrming/VScode/20_6/streamlit-llm-app/app.py
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# OpenAI モデルの設定
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# Streamlit アプリのタイトル
st.title("課題21-6/観光かフードか")

st.write("##### 都道府県の名所と名物")
st.write("都道府県を入力し、「観光地」または「ソウルフード」を選択して実行ボタンを押してください。")

# 動作モードの選択
selected_item = st.radio(
    "動作モードを選択してください。",
    ["観光地", "ソウルフード"]
)

# 都道府県の入力フォーム
prefecture = st.text_input(label="都道府県を入力してください。")

if st.button("実行"):
    st.divider()
    if prefecture:
        # LangChain を使用して観光地またはソウルフードを取得
        if selected_item == "観光地":
            prompt = f"{prefecture}の観光地を教えてください。"
        elif selected_item == "ソウルフード":
            prompt = f"{prefecture}のソウルフードを教えてください。"

        messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=prompt),
        ]

        try:
            result = llm.invoke(messages)
            st.write(f"**{prefecture}の{selected_item}:**")
            st.write(result.content)
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.error("都道府県を入力してください。")