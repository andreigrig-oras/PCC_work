import requests
from operator import itemgetter
import json

url="https://hacker-news.firebaseio.com/v0/topstories.json"
r=requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids=r.json()
submission_dicts=[]
if not isinstance(submission_ids, list):
    print(f"Unexpected response: {submission_ids}")
else:
    for submission_id in submission_ids[:30]:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r=requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict=r.json()
        link=f"https://news.ycombinator.com/item?id={submission_id}"

        submission_dict={
            'title': response_dict['title'],
            'hn_link':link,
            'comments':response_dict['descendants'],
        }
        submission_dicts.append (submission_dict)

submission_dicts=sorted(submission_dicts,key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"\nDiscussion link: {submission_dict['hn_link']}")
    print(f"\nComments: {submission_dict['comments']}")