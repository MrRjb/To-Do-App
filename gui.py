import PySimpleGUI
import functions

label = PySimpleGUI.Text("Enter a todo: ")
input_box = PySimpleGUI.Input(tooltip="Enter todo here", key="todo")
add_button = PySimpleGUI.Button("Add")
listbox = PySimpleGUI.Listbox(values=functions.get_todo(), key="todos", 
                              enable_events=True, size=[43, 10])
edit_button = PySimpleGUI.Button("Edit")

window = PySimpleGUI.Window("My To-Do App", 
                            layout=[[label], 
                                    [input_box, add_button], 
                                    [listbox, edit_button]],
                            font=("Helvetica", 20))

event, value = window.read() 

while True:
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = value["todo"]
            todos.append(new_todo + "\n")
            functions.write_todo(todos)
        case WIN_CLOSED:
            break

window.close()
