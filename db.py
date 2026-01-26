from enum import StrEnum

from sqlalchemy import Enum, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from ulid import ULID


class Base(DeclarativeBase):
    pass


class JobStatus(StrEnum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    status: Mapped[JobStatus] = mapped_column(Enum(JobStatus))


engine = create_engine("sqlite:///outputs/jobs.db")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_job(name: str) -> str:
    session = SessionLocal()
    job_id = str(ULID())
    new_job = Job(id=job_id, name=name, status=JobStatus.RUNNING)
    session.add(new_job)
    session.commit()
    session.close()
    return job_id


def get_job(job_id: str) -> Job | None:
    session = SessionLocal()
    job = session.query(Job).filter(Job.id == job_id).first()
    session.close()
    return job


def get_all_jobs() -> list[Job]:
    session = SessionLocal()
    jobs = session.query(Job).all()
    session.close()
    return jobs


def update_job_status(job_id: str, status: JobStatus) -> None:
    session = SessionLocal()
    job = session.query(Job).filter(Job.id == job_id).first()
    assert job is not None, f"Job with id {job_id} does not exist."
    job.status = status
    session.commit()
    session.close()
