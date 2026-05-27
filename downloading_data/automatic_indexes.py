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
    if column_header=="TMAX":
        max_temp_row = index
        print(f"max temp is number {max_temp_row}")
    elif column_header=="TMIN":
        min_temp_row = index
        print(f"min temp is number {min_temp_row}")
    elif column_header=="NAME":
        name_row = index
        print(f"name is number {name_row}")
    elif column_header=="PRCP":
        prcp_row = index
        print(f"precipitations is number {prcp_row}")
    elif column_header=="DATE":
        date_row = index
        print(f"date is number {date_row}")

name_source=next(reader)
city_name=name_source[name_row]
print(city_name)

dates,precips,highs,lows=[],[],[],[]
for row in reader:
    current_date=datetime.strptime(row[date_row],'%Y-%m-%d')
    dates.append(current_date)
    precip=float(row[prcp_row])
    precips.append(precip)
    try:
        high=int(row[max_temp_row])
        low=int(row[min_temp_row])
    except ValueError:
        print(f'missing data for {current_date}')
    highs.append(high)
    lows.append(low)
    
fig, ax = plt.subplots()
ax.plot(dates, precips, color='green')
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.set_ylim(0,120)

ax.set_title(f"Daily precipitations and temps in {city_name.title()} for the past year", fontsize=12)
fig.autofmt_xdate()

plt.savefig("darwin_temps.png")
plt.show()