import function
import FreeSimpleGUI as sg

label = sg.Text("Type in to-do")  # label on text in window
input_box = sg.InputText(tooltip="Enter todo", key="todos")  # in input box hovar something written
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))  # []any obiject puting in one row putiing
while True:
    event, values = window.read()  # this read all thing
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo= values['todos'] +'\n'
            todos.append(new_todo)
            function.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()
