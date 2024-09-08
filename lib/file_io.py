# lib/file_io.py

def write_file(file_name, file_content):
    """Writes the file_content to a new or existing file, overwriting any previous content."""
    with open(f"{file_name}.txt", 'w') as file:
        file.write(file_content)


def append_file(file_name, file_content):
    """Appends the file_content to the end of an existing file."""
    with open(f"{file_name}.txt", 'a') as file:
        file.write(file_content)


def read_file(file_name):
    """Reads the content of the file and returns it."""
    with open(f"{file_name}.txt", 'r') as file:
        return file.read()
