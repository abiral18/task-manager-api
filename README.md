# Task Manager REST API

A RESTful API built with Python and Flask for managing tasks. Supports full CRUD operations.

## Tech Stack
- Python 3.14
- Flask

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| POST | /tasks | Create a new task |
| PUT | /tasks/<id> | Mark task as done |
| DELETE | /tasks/<id> | Delete a task |

## Setup

```bash
git clone https://github.com/abiral18/task-manager-api
cd task-manager-api
pip install -r requirements.txt
python app.py
```

## Usage
API runs on `http://127.0.0.1:5000`