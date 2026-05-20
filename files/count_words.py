from pathlib import Path
path=Path("files/the_cia.txt")
content=path.read_text().lower()
num=content.count('romania')
print(num)