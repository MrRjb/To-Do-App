import streamlit
import functions

streamlit.title("My To-Do App")
streamlit.subheader("A Minimalistic Todo App.")
streamlit.write("This app is designed to boost your productivity!")

todos = functions.get_todo()

for todo in todos:
    streamlit.checkbox(todo)
    
streamlit.text_input(label="", placeholder="Type in a new todo here ...", help="Press Enter to apply")

