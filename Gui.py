import function
import FreeSimpleGUI as sg

label = sg.Text("Type in to-do")#label on text in window
input_box = sg.InputText(tooltip="Enter todo")#in input box hovar something written
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',layout=[[label],[input_box,add_button]])#[]any obiject puting in one row putiing
window.read()
window.close()