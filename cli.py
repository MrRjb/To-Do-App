print("Welcome to the Todo App. Created by Rupankar Borah")

from functions import get_todo, write_todo
import time        
        
now = time.strftime("%b %d, %Y -- %H:%M:%S \n")
print(f"It is now, {now}")   
        
todos = get_todo()

prompt = "Enter your choice (Add/Show/Edit/Complete): "

while True:
    user_choice = input(prompt).lower()
    user_choice.strip()
    
    if user_choice == "add":
        user_input = input("Enter a new todo: ")
        todos.append(user_input + "\n")
        write_todo(todos) 
    
    elif user_choice == "show":
        todos = get_todo()    
        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1} -- {todo}")
    
    elif user_choice == "complete":
        num_todo = int(input("Enter the number of the todo completed: "))
        num_todo = num_todo -1
        todos = get_todo()
        todos.pop(num_todo)
        write_todo(todos)
    
    elif user_choice == "edit":
        index = int(input("Enter the todo number to edit: "))
        index = index -1
        new_prompt = input("Enter the new todo: ")
        todos[index] = new_prompt + "\n"
        write_todo(todos)
    
    elif user_choice == "exit":
        break
    
    else:
        print("You entered a wrong prompt. Please try again.")
        continue
    
print("Thank you for using the App.")    
        
    