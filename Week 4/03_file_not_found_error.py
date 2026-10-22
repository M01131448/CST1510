# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
try: #attempts to open the file.
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    """ if the file is not found, the program does not crash"""
    print("The file records.txt is not found.")