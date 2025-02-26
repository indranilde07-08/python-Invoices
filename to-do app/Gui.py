import function
import FreeSimpleGUI as sg

label = sg.Text("Type in to-do")  # label on text in window
input_box = sg.InputText(tooltip="Enter todo", key="todos")  # in input box hovar something written
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todos(), key='items',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))  # []any obiject puting in one row putiing
while True:
    event, values = window.read()  # this read all thing
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todos'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
            window["todos"].update(value="")  # Correct way to clear input field
            window["items"].update(values=todos)
        case "Edit":
            todos_edit= values["items"][0]
            new_todo = values["todos"]
            todos = function.get_todos()
            index = todos.index(todos_edit.strip() + '\n')
            todos[index] = new_todo + '\n'
            function.write_todos(todos)
            window["items"].update(values=todos)

        case 'items':
            window['todos'].update(value=values['items'][0])

        case sg.WIN_CLOSED:
            break
window.close()
