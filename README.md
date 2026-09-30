# StudySprint

StudySprint is a command-line study planner for organizing coursework and tracking study sessions. It stores tasks locally in a JSON file and provides summaries of deadlines and estimated workload by subject.

## Features

- Add tasks with a subject, due date, estimated study time, and priority.
- List open tasks, ordered by deadline and priority.
- Mark tasks complete, remove them, or log study sessions.
- View progress summaries and open study time by subject.
- Save tasks between runs using a local JSON file.
- Validate input and display readable errors.

## Requirements

- Python 3.10 or newer
- No third-party runtime dependencies

## Setup

1. Clone the repository and open a terminal in the project folder.
2. Create and activate a virtual environment.

   **Windows PowerShell**

   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
