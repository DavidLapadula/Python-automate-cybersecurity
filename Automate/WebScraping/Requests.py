import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

if not res.raise_for_status():
    playFile = open("RJ.txt", "wb")

for chunk in res.iter_content(10000):
    playFile.write(chunk)