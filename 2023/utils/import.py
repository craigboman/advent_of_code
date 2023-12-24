import requests

def download(date: str):
    url = "https://adventofcode.com/2023/day/"+ date +"/input"
    data = requests.get(url) # missing AoC auth session token
    return data