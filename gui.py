import PySimpleGUI

label = PySimpleGUI.Text("Enter a todo: ")
input_box = PySimpleGUI.Input(tooltip="Enter todo here")
add_button = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
