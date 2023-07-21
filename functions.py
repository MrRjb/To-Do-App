FILEPATH = "todos.txt"

def get_todo(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local
    

def write_todo(todos_arg, filepath=FILEPATH ):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)