VALID_PRIORITIES = ["Low", "Medium", "High"]

tasks = []
next_id = 1

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
        priority = input("Enter the priority (Low, Medium, High): ").strip().title()

        if priority in VALID_PRIORITIES:
            break
        else:
            print("Invalid priority.")

    return title, description, priority

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
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            return True

    return False

def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True

    return False

def edit_task(tasks, task_id, field, new_value):
    for task in tasks:
        if task["id"] == task_id:

            if field == "title":
                task["title"] = new_value

            elif field == "description":
                task["description"] = new_value

            elif field == "priority":
                task["priority"] = new_value

            return True

    return False
            
   

while True:
    print("\n=== DevManager ===")
    print("1 - Create Task")
    print("2 - List Tasks")
    print("3 - Complete Task")
    print("4 - Delete Task")
    print("5 - Edit Task")   
    print("6 - Exit")

    menu_option = input("\nChoose an option: ").strip()

    if menu_option == "1":
        title, description, priority = get_task_data()

        new_task = create_task(
            title,
            description,
            priority,
            next_id
        )

        tasks.append(new_task)
        next_id += 1

        print(f"Task {new_task['id']} created successfully!")

    elif menu_option == "2":
        list_tasks(tasks)

    elif menu_option == "3":
        try:
            task_id = int(
                input("Which task ID do you want to complete? ")
            )

            task_finished = complete_task(tasks, task_id)

            if task_finished:
                print("Your task has been successfully completed.")
            else:
                print("Task ID not found.")

        except ValueError:
            print("Please enter a valid numeric ID.")

    elif menu_option == "4":
        try:
            task_id = int(
                input("Which task ID do you want to delete? ")
            )

            want_to_delete = input(
                "Do you really want to delete this task? s/n: "
            ).strip().lower()

            if want_to_delete == "s":
                task_delete = delete_task(tasks, task_id)

                if task_delete:
                    print("Task deleted successfully!")
                else:
                    print("Task ID not found.")

            else:
                print("Sure, the task will not be deleted.")

        except ValueError:
            print("Please enter a valid numeric ID.")

    elif menu_option == "5":
        try:
            task_id = int(input("Which task do you want to edit?"))

            want_to_edit = input("Do you really want to edit this task? title/description/priority"
                                 ).strip().lower()

            new_value = input("What will the new amount be?")

             
            task_edit = edit_task(tasks ,task_id, want_to_edit, new_value)

            if task_edit:
                print("Your task has been successfully edited.")
            else:
                print("Task ID not found.")
                  

        except ValueError:
            print("Please enter a valid numeric ID.")    

    elif menu_option == "6":
        print("Closing DevManager...")
        break

    else:
        print("Invalid option.")