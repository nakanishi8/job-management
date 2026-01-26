import pandas as pd
import streamlit as st

from db import get_all_jobs

if __name__ == "__main__":
    st.title("ジョブ一覧ページ")
    jobs = get_all_jobs()
    jobs_df = pd.DataFrame(
        [
            {
                "保存名": job.name,
                "ステータス": job.status,
                "結果": f"/result?id={job.id}",  # 結果ページへのリンク
            }
            for job in jobs
        ]
    )
    if jobs_df.empty:
        st.write("実行されたジョブはありません。")
    else:
        st.dataframe(
            jobs_df,
            column_config={"結果": st.column_config.LinkColumn("結果", display_text="結果を見る ↗️")},
            hide_index=True,
        )
