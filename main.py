import streamlit as st

if __name__ == "__main__":
    st.navigation(
        [
            st.Page("pages/job_execution.py", title="ジョブ実行ページ"),
            st.Page("pages/job_list.py", title="ジョブ一覧ページ"),
            st.Page("pages/result.py", title="結果ページ"),
        ],
    ).run()
