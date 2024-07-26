FILE_PATH = "todos.txt"
def get_todos(filepath=FILE_PATH):
    """Read a todo file and return the todos written in it"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath=FILE_PATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
         