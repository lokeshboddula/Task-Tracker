import operations

task = input()

commands = '''choose command from below 
    add <text>
    update <text>
    delete <task id>
    list <type> - leave empty for all types'''

if 'add' in task:
    operations.add(task)
elif 'update' in task:
    operations.update(task)
elif 'delete' in task:
    operations.delete(task)
elif 'list done' in task:
    operations.list_done(task)
elif 'list todo' in task:
    operations.list_todo(task)
elif 'list in-progress' in task:
    operations.list_in_progress(task)
elif 'list' in task:
    operations.list_all(task)
else:
    print(commands)