import function
import time

now = time.strftime("%b %d, %y %H:%M:%S")
print("The time is below")
print("It now",now)
while True:
    user_action = input("Type add, show, edit, delete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = function.get_todos()

        todos.append(todo.title())

        function.write_todos(todos)

    elif user_action.startswith("show"):

        todos = function.get_todos()

        for index, item in enumerate(todos, start=1):
            item = item.strip("\n")
            print(f"{index}: {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos = function.get_todos()

            new_todo = input("Enter the new item: ").title()
            todos[number] = new_todo + '\n'

            function.write_todos(todos)

            print(f"Successfully change  new todo item: {new_todo} ")
        except ValueError:
            print("Your comment is not valid")
            continue

    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:]) - 1
            todos = function.get_todos()

            remove_element = todos.pop(number)

            function.write_todos(todos)

            print(f"{remove_element.strip()}: Successfully deleted from the todo list.")
        except IndexError:
            print("There is no number in the todo-list ")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")
