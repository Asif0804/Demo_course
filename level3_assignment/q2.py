def count(file_path):
    try:
        with open(file_path, 'r') as file:
            c = sum(1 for line in file)
            return c
    except FileNotFoundError:
        return "File not found."

file_path = 'demo.txt'
print(count(file_path))