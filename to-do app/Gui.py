import function
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

sg.theme("NeonGreen1")
label_time = sg.Text( key='time')
label = sg.Text("Type in to-do")  # label on text in window
input_box = sg.InputText(tooltip="Enter todo", key="todos")  # in input box hovar something written
add_button = sg.Button("Add",size=10)
list_box = sg.Listbox(values=function.get_todos(), key='items',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

layout = [[label_time],[label], [input_box, add_button], [list_box, edit_button, delete_button],[exit_button]]

window = sg.Window('My To-Do App',
                   layout= layout,
                   font=('Helvetica', 20))  # []any obiject puting in one row putiing
while True:
    event, values = window.read(timeout=200)  # this read all thing
    window['time'].update(value=time.strftime("%b %d, %y %H:%M:%S"))
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todos'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
            window["todos"].update(value="")  # Correct way to clear input field
            window["items"].update(values=todos)
        case "Edit":
            try:
                todos_edit= values["items"][0]
                new_todo = values["todos"]
                todos = function.get_todos()
                index = todos.index(todos_edit.strip() + '\n')
                todos[index] = new_todo + '\n'
                function.write_todos(todos)
                window["items"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 10))

        case 'Delete':
            try:
                todo_to_delete = values['items'][0]
                todos = function.get_todos()
                todos.remove(todo_to_delete)
                function.write_todos(todos)
                window['items'].update(values=todos)
            except IndexError:
                sg.popup("please select an item first", font=('Helvetica', 10))

        case 'Exit':
            break

        case 'items':
            window['todos'].update(value=values['items'][0])

        case sg.WIN_CLOSED:
            break
window.close()
