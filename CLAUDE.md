# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Streamlit-based job management system (streamlit-job-manager) for handling long-running processes. Written in Python 3.13+ with Japanese UI.

## Build & Development Commands

```bash
# Install dependencies (uses UV package manager)
uv sync --all-groups

# Install package in editable mode (required for imports)
uv pip install -e .

# Create outputs directory (required before first run)
mkdir -p outputs

# Run the Streamlit app
streamlit run app/main.py

# Run tests
pytest

# Run tests with coverage
pytest --cov=example_project

# Lint and format
ruff check . --fix
ruff format .
```

## Architecture

```
app/
├── main.py           # Entry point - Streamlit navigation
├── db.py             # SQLAlchemy + SQLite persistence (Job model, JobStatus enum)
├── job.py            # Job execution orchestration
├── problem.py        # Domain logic (Pydantic models, solve_problem)
└── pages/            # Streamlit UI pages
    ├── job_execution.py    # Job creation form
    ├── job_list.py         # Job listing table
    └── result.py           # Job result display
```

**Data flow:** User input (pages) → `execute_job()` → `solve_problem()` → SQLite + JSON output

**Key patterns:**
- Jobs run in `multiprocessing.Process` for async execution
- Output stored at `outputs/{job_id}/` (input.json, output.json)
- Job status: RUNNING → COMPLETED/FAILED
- ULID for unique job IDs

## Code Style

- Ruff for formatting/linting (120 char line length)
- Format on save enabled in VSCode
