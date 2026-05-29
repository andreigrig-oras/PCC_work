from pathlib import Path
import csv
import plotly.express as px

path=Path("eq_data/MODIS_C6_1_Global_7d.csv")
lines=path.read_text(encoding='utf-8').splitlines()
reader=csv.reader(lines)
header_row=next(reader)

for index,header_row in enumerate(header_row):
    print (index,header_row)

lons,lats,brights=[],[],[]
for row in reader:
    try:
        bright=float(row[2])
        if bright<400:
            continue
        brights.append (float(row[2]))
        lons.append (float(row[1]))
        lats.append (float(row[0]))
    except ValueError:
       continue

big_title="Fires"
fig=px.scatter_geo(
    lat=lats,lon=lons, title=big_title,
    color=brights,
    color_continuous_scale="viridis",
    projection='natural earth',
    )
fig.show()