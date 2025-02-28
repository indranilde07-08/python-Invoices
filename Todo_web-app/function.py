import os

filepath ="todos.txt"

def get_todos(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:  # Create an empty file
            pass
    with open(filepath, 'r') as file_name:
        """ Read a text file and return the list of to-do items. """
        todos_local = file_name.readlines()
        return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_name:
        file_name.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")
    print(get_todos())