import os
import json
import shutil

TASKS_FILE = "tasks.json"


def get_previous_filename(rotate_number):
    return f"tasks_previous_{rotate_number}.json"


def rotate_backups():
    if not os.path.exists(TASKS_FILE):
        return

    if os.path.exists(get_previous_filename(2)):
        os.replace(
            get_previous_filename(2),
            get_previous_filename(3)
        )

    if os.path.exists(get_previous_filename(1)):
        os.replace(
            get_previous_filename(1),
            get_previous_filename(2)
        )

    shutil.copyfile(
        TASKS_FILE,
        get_previous_filename(1)
    )


def create_backup():
    backup_count = 1

    while True:
        backup_filename = f"tasks_backup_{backup_count}.json"

        if not os.path.exists(backup_filename):
            os.rename(TASKS_FILE, backup_filename)
            break

        backup_count += 1


def save_tasks(tasks):
    rotate_backups()

    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        create_backup()
        print(f"Error: {TASKS_FILE} is corrupted. A backup has been created.")
        return []
