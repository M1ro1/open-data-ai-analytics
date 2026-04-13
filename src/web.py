import streamlit as st
import os
import json

st.set_page_config(page_title="AI Analytics", layout="wide")
st.title("📊 Аналітика відкритих даних")

col1, col2 = st.columns(2)

with col1:
    st.header("Перевірка якості даних")
    if os.path.exists("/app/reports/quality_report.txt"):
        with open("/app/reports/quality_report.txt", "r", encoding="utf-8") as f:
            st.text(f.read())

    st.header("Дослідження даних")
    if os.path.exists("/app/reports/research_report.json"):
        with open("/app/reports/research_report.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            st.json(data)

with col2:
    st.header("Візуалізація")
    if os.path.exists("/app/reports/figures/fuel_distribution.png"):
        st.image("/app/reports/figures/fuel_distribution.png")
    if os.path.exists("/app/reports/figures/top_brands.png"):
        st.image("/app/reports/figures/top_brands.png")
