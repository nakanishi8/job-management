import time

from pydantic import BaseModel


class ProblemInputModel(BaseModel):
    a: float
    b: float


class ProblemOutputModel(BaseModel):
    answer: float


def solve_problem(input_data: ProblemInputModel) -> ProblemOutputModel:
    answer = input_data.a + input_data.b
    time.sleep(60)  # 時間のかかる処理だという想定
    return ProblemOutputModel(answer=answer)
