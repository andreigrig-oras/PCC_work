from pathlib import Path
import json
import plotly.express as px
from datetime import datetime

path=Path("eq_data/eq_1_day_m1.geojson")
contents=path.read_text(encoding='utf-8')
all_eq_data=json.loads(contents)
all_eq_dicts=all_eq_data['features']

mags,lons,lats,tits=[],[],[],[]
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    tits.append (f"Title: {eq_dict['properties']['title']} \n Date: {datetime.fromtimestamp(eq_dict['properties']['time']/1000)}")

big_title=all_eq_data['metadata']['title']
fig=px.scatter_geo(
    lat=lats,lon=lons, size=mags, title=big_title,
    color=mags,
    color_continuous_scale="viridis",
    labels={'color':'Magnitude'},
    projection='natural earth',
    hover_name=tits,
    )
fig.show()