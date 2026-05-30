import requests
from operator import itemgetter
import json
import plotly.express as px

url="https://hacker-news.firebaseio.com/v0/topstories.json"
r=requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids=r.json()
# submission_ids.sort()
submission_dicts, titles,comms=[],[],[]

for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict=r.json()

    submission_dict={
        'title': response_dict['title'],
        'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",
        'comments':response_dict['descendants'],
    }
    submission_dicts.append (submission_dict)

submission_dicts=sorted(submission_dicts,key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    comms.append(submission_dict['comments'])

title="Most active discussions"
labels={'x':'Title','y':'No. of comments'}

fig=px.bar(
    x=titles, y=comms,
    title=title,
    labels=labels,
           )

fig.show()

# for submission_dict in submission_dicts:
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"\nDiscussion link: {submission_dict['hn_link']}")
#     print(f"\nComments: {submission_dict['comments']}")