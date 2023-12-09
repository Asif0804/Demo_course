def level3_1(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()

            even_string = filter(lambda x: len(x) % 2 == 0, words)

            return ' '.join(even_string)

    except FileNotFoundError:
        return "file not found."

file_path = 'doc.txt'
print(level3_1(file_path))