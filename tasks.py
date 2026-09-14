VALID_PRIORITIES = ["Low", "Medium", "High"]


def get_next_id(tasks):
    ids = [task["id"] for task in tasks]
    max_id = max(ids) if ids else 0
    return max_id + 1

def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def create_task(title, description, priority, next_id):
    new_task = {
        "id": next_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pending"
    }

    return new_task


def complete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if task:
        task["status"] = "done"
        return True
    return False
    


def delete_task(tasks, task_id):
    task= find_task(tasks, task_id)
    if task:
        tasks.remove(task)
        return True
    return False


def edit_task(tasks, task_id, field, new_value):
    task = find_task(tasks, task_id)
    if task:
        if field == "title":
            task["title"] = new_value
        elif field == "description":
            task["description"] = new_value
        elif field == "priority":
            task["priority"] = new_value
        else:
            return "invalid_field"

        return "success"

    return "id_not_found"