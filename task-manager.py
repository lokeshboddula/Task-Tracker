import operations

while True:
    command = input("Enter command (add, update, delete, list, exit): ").strip().lower()

    if command == "add":
        operations.add()

    elif command == "update":
        operations.update()

    elif command == "delete":
        operations.delete()

    elif command == "list":
        operations.list_tasks()

    elif command == "exit":
        print("Exiting the Task Tracker.")
        break

    else:
        print("Unknown command. Please try again.")