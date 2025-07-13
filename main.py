TODOLIST_FILE = 'files/todos.txt'

print("Welcome to the TODO list!!\n"
      "1. Add a new task 'a'\n"
      "2. List all tasks 'l'\n"
      "3. Delete a task 'd'\n"
      "4. Update a task 'u'\n"
      "5. Complete a task 'c'\n"
      "6. Quit 'q'\n")

while True:
    action = input("\nWhat would you like to do?: ")
    action = action.strip().lower()
    match action:

        case 'a' | '1':
            addtodo = input("Enter the task you would like to add: ") + "\n"

            file = open(TODOLIST_FILE, 'r')
            todos = file.readlines()
            file.close()

            if addtodo in todos:
                print("Task already exists.")
                continue


            todos.append(addtodo)

            file = open(TODOLIST_FILE, 'w')
            file.writelines(todos)
            file.close()

        case 'l' | '2':
            file = open(TODOLIST_FILE, 'r')
            todos = file.readlines()
            for index, todo in enumerate(todos):
                print(f"{index+1}. {todo}")

        case 'd' | '3':
            file = open(TODOLIST_FILE, 'r')
            todos = file.readlines()
            if todos.count('\n') == 0:
                print("No tasks to delete.")

            todelete = input("Enter the task you would like to delete: ")
            if todelete in todos:
                todos.remove(todelete)
            else:
                print("Task not found.")

        case 'u' | '4':
            file = open(TODOLIST_FILE, 'r')
            todos = file.readlines()
            if todos.count('\n') == 0:
                print("No tasks to update.")
                continue

            toupdate = input("Enter the task you would like to update: ")

            for index, todo in enumerate(todos):
                if toupdate in todo:
                    newupdate = input("Enter the new task: ")
                    todos[index] = newupdate
                    break

        case 'c' | '5':
            file = open(TODOLIST_FILE, 'r')
            todos = file.readlines()
            if todos.count('\n') == 0:
                print("No tasks to complete.")
                continue

            tocomplete = input("Enter the task you would like to complete: ")
            for index, todo in enumerate(todos):
                if tocomplete in todo:

                    del todos[index]

        case 'q' | '6':
            break

        case _:
            print("Invalid choice. Please try again.")
