import operations

while True:
    command = input("Enter command (add, update, delete, list, exit): ").strip().lower()

    if command == "add":
        description = input("Enter task description: ").strip()
        operations.add(description)

    elif command == "update":
        task_id = int(input("Enter task ID to update: "))
        description = input("Enter the new description: ")
        status = input("Enter new status (todo, in-progress, done): ").strip().lower()
        operations.update(task_id, status, description)

    elif command == "delete":
        task_id = int(input("Enter task ID to delete: "))
        operations.delete(task_id)

    elif command == "list":
        filter_status = input("Enter status to filter by (all, todo, in-progress, done): ").strip().lower()
        if filter_status == 'all':
            operations.list_tasks()
        else:
            operations.list_tasks(filter_status)

    elif command == "exit":
        print("Exiting the Task Tracker.")
        break

    else:
        print("Unknown command. Please try again.")