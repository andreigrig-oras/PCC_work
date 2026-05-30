from python_repos import return_status
import pytest
import requests

def test_return_status():
    headers = {"Accept":"application/vnd.github.v3+json"}
    r=requests.get("https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000", headers=headers)
    test_name=return_status(r)
    assert test_name == "Status code: 200"