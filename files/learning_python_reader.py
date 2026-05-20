from pathlib import Path
file=Path('files/learning_python.txt')
contents=file.read_text()
print(contents)
contents=contents.replace('Python', 'C++')
for line in contents.splitlines():
    print (line)