import streamlit
import functions

todos = functions.get_todo()

def add_todo():
    todo = streamlit.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todo(todos)    

streamlit.title("My To-Do App")
streamlit.subheader("A Minimalistic Todo App.")
streamlit.write("This app is designed to boost your productivity!")

for todo in todos:
    streamlit.checkbox(todo)
    
streamlit.text_input(label="", placeholder="Type in a new todo here ...", 
                     on_change=add_todo, key='new_todo')

