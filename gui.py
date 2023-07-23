import PySimpleGUI
import functions
import time 
import os

PySimpleGUI.theme("DarkPurple4")

clock = PySimpleGUI.Text('', key='clock')

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

label = PySimpleGUI.Text("Type in a new todo below: ")
input_box = PySimpleGUI.Input(tooltip="Enter todo here", key="todo")
add_button = PySimpleGUI.Button("Add", size=10)
listbox = PySimpleGUI.Listbox(values=functions.get_todo(), key="todos", 
                              enable_events=True, size=[45, 10])

edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window("My To-Do App. Created by - RJB", 
                            layout=[[clock],
                                    [label], 
                                    [input_box, add_button], 
                                    [listbox, edit_button, complete_button],
                                    [exit_button]],
                            font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y -- %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n" 
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("Please select an item first.", font=('Helvetica', 20))
                
        case "Complete":
            try:
                todo_to_remove = values["todos"][0]
                todos = functions.get_todo()
                todos.remove(todo_to_remove)
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                PySimpleGUI.popup("Please select an item first.", font=('Helvetica', 20))
                 
        case "Exit":
           break
       
        case "todos":
            window['todo'].update(value=values['todos'][0])
            
        case PySimpleGUI.WINDOW_CLOSED:
            break
     

window.close()
