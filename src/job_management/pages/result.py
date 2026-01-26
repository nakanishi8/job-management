from pathlib import Path

import streamlit as st
from db import JobStatus, get_job

if __name__ == "__main__":
    st.title("結果ページ")

    job_id = st.query_params.get("id", None)
    if job_id is None:
        st.error("job_id is required in query parameters")
        st.stop()

    job = get_job(job_id)
    if job is None:
        st.error(f"Job with id {job_id} does not exist.")
        st.stop()

    load_dir = Path(f"src/job_management/outputs/{job_id}")
    with open(load_dir / "input.json", "r") as f:
        input_data = f.read()

    st.write("### 入力データ")
    st.json(input_data)

    if job.status is JobStatus.RUNNING:
        st.info("実行中です。")
    elif job.status is JobStatus.FAILED:
        st.error("実行に失敗しました。")
    elif job.status is JobStatus.COMPLETED:
        with open(load_dir / "output.json", "r") as f:
            output_data = f.read()
        st.write("### 結果")
        st.json(output_data)
