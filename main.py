import storage
import tasks
import cli


task_list = storage.load_tasks()
next_id = tasks.get_next_id(task_list)


while True:
    print("\n=== DevManager ===")
    print("1 - Create Task")
    print("2 - List Tasks")
    print("3 - Complete Task")
    print("4 - Delete Task")
    print("5 - Edit Task")
    print("6 - Exit")

    option = input("Choose an option: ").strip()

    match option:
        case "1":
            title, description, priority = cli.get_task_data()

            new_task = tasks.create_task(
                title,
                description,
                priority,
                next_id
            )

            task_list.append(new_task)
            next_id += 1

            storage.save_tasks(task_list)

            print("Task created successfully.")

        case "2":
            cli.list_tasks(task_list)

        case "3":
            try:
                task_id = int(input("Which task ID do you want to complete? "))

                if tasks.complete_task(task_list, task_id):
                    storage.save_tasks(task_list)
                    print("Task completed successfully.")
                else:
                    print("Task ID not found.")

            except ValueError:
                print("Invalid ID. Please enter a number.")

        case "4":
            try:
                task_id = int(input("Which task ID do you want to delete? "))

                confirmation = input(
                    "Do you really want to delete this task? s/n: "
                ).strip().lower()

                if confirmation == "s":
                    if tasks.delete_task(task_list, task_id):
                        storage.save_tasks(task_list)
                        print("Task deleted successfully.")
                    else:
                        print("Task ID not found.")
                else:
                    print("Deletion cancelled.")

            except ValueError:
                print("Invalid ID. Please enter a number.")

        case "5":
            try:
                task_id = int(input("Which task ID do you want to edit? "))

                existing_task = next(
                    (
                        task
                        for task in task_list
                        if task["id"] == task_id
                    ),
                    None
                )

                if not existing_task:
                    print("Task ID not found.")
                    continue

                field = input(
                    "Enter the field to edit "
                    "(title, description, priority): "
                ).strip().lower()

                new_value = input(
                    "Enter the new value: "
                ).strip()

                task_edit = tasks.edit_task(
                    task_list,
                    task_id,
                    field,
                    new_value
                )

                if task_edit == "success":
                    print("Your task has been successfully edited.")
                    storage.save_tasks(task_list)

                elif task_edit == "invalid_field":
                    print(
                        "Invalid field. Please enter "
                        "title, description, or priority."
                    )

                else:
                    print("Task ID not found.")

            except ValueError:
                print("Invalid ID. Please enter a number.")

        case "6":
            print("Exiting DevManager.")
            break

        case _:
            print("Invalid option.")