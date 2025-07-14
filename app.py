"""起動

streamlit run ファイル名.py
"""
import streamlit as st
st.title("簡単なStreamlit　アプリ")

name = st. text_input("ユーザー名を入力してください")

age = st.slider("年齢を選んでください",0,100,0,)

if name:
    st.write(f"こんにちは{name}")
    st.write(f"あなたは{age}歳なんですね")
    st.write(f"{age-5}歳にしか見えません")
else:
    st.write("前を入力してください")