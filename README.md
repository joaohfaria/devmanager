# DevManager

A command-line task manager built with Python as a study project to practice
programming fundamentals, code organization and version control.

## Features

- Create tasks with title, description and priority
- List all tasks
- Mark tasks as completed
- Edit title, description or priority
- Delete tasks with confirmation
- Automatic ID assignment for each task
- Three priority levels: Low, Medium, High
- Data persistence with JSON — tasks are saved to a file and loaded on startup
- Input validation and error handling for invalid IDs and empty fields

## Requirements

- Python 3

No external dependencies.

## How to run

```bash
git clone https://github.com/joaohfaria/devmanager.git
cd devmanager
python devmanager.py
```

Tasks are stored in `tasks.json`, created automatically on first save.

## How it works

Each task is stored as a dictionary:

```python
{
    "id": 1,
    "title": "Study Python",
    "description": "Review functions and dictionaries",
    "priority": "High",
    "status": "pending"
}
```

All tasks are kept in a list, which is written to `tasks.json` after every
operation that changes the data.

## Project history

The first version stored tasks in memory only. Every task was lost when the
program was closed. To fix this, I implemented persistence with JSON, which
required learning file handling, and handling the case where the data file
does not exist yet.

## Concepts practiced

- Functions, parameters and return values
- Lists, dictionaries and tuples
- Loops and conditionals
- Error handling with try/except
- Reading and writing files
- Working with JSON
- Separation of responsibilities between functions
- Version control with Git

## Status

In development. The project is being extended as I learn new concepts.

## Next steps

- Handle corrupted data files
- Split the code into multiple modules
- Filter and sort tasks