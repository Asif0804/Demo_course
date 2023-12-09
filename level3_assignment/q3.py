def JtoI(file_path):
    try:
        with open(file_path, 'r') as file:
            b = file.read()
            a = b.replace('J', 'I').replace('j', 'i')
            return a
    except FileNotFoundError:
        print("File not found.")

file_path = 'words.txt'
print(JtoI(file_path))