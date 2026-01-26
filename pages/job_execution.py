from multiprocessing import Process

import streamlit as st

from job import execute_job
from problem import ProblemInputModel

if __name__ == "__main__":
    st.title("ジョブ実行ページ")
    a = st.number_input("a", min_value=0.0, max_value=100.0, value=50.0)
    b = st.number_input("b", min_value=0.0, max_value=100.0, value=50.0)
    name = st.text_input("保存名")

    if st.button("実行"):
        input_data = ProblemInputModel(a=a, b=b)
        process = Process(
            target=execute_job,
            args=(name, input_data),
        )
        process.start()
        st.success("実行しました。")
