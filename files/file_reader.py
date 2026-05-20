from pathlib import Path
path=Path('files/pi_digits.txt')
content=path.read_text().rstrip()
lines=content.splitlines()
pi_string=""
for line in lines:
    pi_string+=line.lstrip()

print (pi_string)
print (len(pi_string))