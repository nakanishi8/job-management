import json
from pathlib import Path

from db import JobStatus, create_job, update_job_status
from problem import ProblemInputModel, ProblemOutputModel, solve_problem


def execute_job(name: str, input_data: ProblemInputModel) -> None:
    job_id = create_job(name)
    save_dir = Path(f"outputs/{job_id}")
    save_dir.mkdir(parents=True, exist_ok=False)

    try:
        # 入力データを保存
        with open(save_dir / "input.json", "w") as f:
            json.dump(input_data.model_dump(), f, indent=4)

        # 問題を解いて結果を保存
        output_data: ProblemOutputModel = solve_problem(input_data)
        with open(save_dir / "output.json", "w") as f:
            json.dump(output_data.model_dump(), f, indent=4)

        # status を COMPLETED に更新
        update_job_status(job_id, JobStatus.COMPLETED)
    except Exception:
        # エラーが発生した場合は status を FAILED に更新
        update_job_status(job_id, JobStatus.FAILED)
        raise
