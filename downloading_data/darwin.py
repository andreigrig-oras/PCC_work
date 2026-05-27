import csv
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

path= Path('darwin_todate.csv')
lines=path.read_text(encoding='utf-8').splitlines()

reader =csv.reader(lines)
header_row=next(reader)

for index, column_header in enumerate(header_row):
    print (index, column_header)

dates,precips,highs,lows=[],[],[],[]
for row in reader:
    current_date=datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(current_date)
    precip=float(row[3])
    precips.append(precip)
    try:
        high=int(row[4])
        low=int(row[5])
    except ValueError:
        print(f'missing data for {current_date}')
    highs.append(high)
    lows.append(low)
    

fig, ax = plt.subplots()
ax.plot(dates, precips, color='green')
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.set_ylim(0,120)

ax.set_title("Daily precipitations and temps in Darwin for the past year", fontsize=20)
fig.autofmt_xdate()

plt.savefig("darwin_temps.png")
plt.show()