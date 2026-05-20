from pathlib import Path
try:
    cats=Path("files/cats.txt")
    cats_content=cats.read_text()
except FileNotFoundError:
    pass
else:
    print(cats_content)
try:
    dogs=Path("files/dogs.txt")
    dogs_content=dogs.read_text()
except FileNotFoundError:
    pass
else:
    print (dogs_content)