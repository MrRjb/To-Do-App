import PySimpleGUI
import functions

label = PySimpleGUI.Text("Enter a todo: ")
input_box = PySimpleGUI.Input(tooltip="Enter todo here", key="todo")
add_button = PySimpleGUI.Button("Add")
listbox = PySimpleGUI.Listbox(values=functions.get_todo(), key="todos", 
                              enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("Edit")

window = PySimpleGUI.Window("My To-Do App", 
                            layout=[[label], 
                                    [input_box, add_button], 
                                    [listbox, edit_button]],
                            font=("Helvetica", 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values["todo"] + "\n" 
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todo(todos)
            window['todos'].update(values=todos)
       
        case "todos":
            window['todo'].update(value=values['todos'][0])
            
        case PySimpleGUI.WINDOW_CLOSED:
            break
     

window.close()
