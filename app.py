import streamlit as st, pandas as pd, json

st.set_page_config(page_title="TruthAI-Universal Dashboard", layout="wide")
st.title("🌍 TruthAI-Universal — Living Evidence")

log = st.text_input("Log file", "examples/logs/core.jsonl")

if st.button("Load"):
    try:
        with open(log,"r",encoding="utf-8") as f:
            data=[json.loads(line) for line in f]
        df=pd.DataFrame(data)
        st.dataframe(df)
        if "accuracy" in df: st.bar_chart(df.set_index("name")["accuracy"])
    except Exception as e:
        st.error(str(e))
