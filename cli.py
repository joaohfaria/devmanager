from tasks import VALID_PRIORITIES


def get_task_data():
    while True:
        title = input("Enter the task title: ").strip()

        if not title:
            print("Title cannot be empty.")
        else:
            break

    while True:
        description = input("Enter the task description: ").strip()

        if not description:
            print("Description cannot be empty.")
        else:
            break

    while True:
        priority = input(
            "Enter the priority (Low, Medium, High): "
        ).strip().title()

        if priority in VALID_PRIORITIES:
            break
        else:
            print("Invalid priority.")

    return title, description, priority


def list_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    for task in tasks:
        print(f"\nID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Priority: {task['priority']}")
        print(f"Status: {task['status']}")