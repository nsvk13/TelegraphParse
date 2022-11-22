import requests
import json

from os import system, path, mkdir, getcwd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from fake_useragent import UserAgent

class cs:
    INFO = "\033[93m"
    GREEN = "\033[92m"
    END = "\033[0m"

UserAgent =f"{UserAgent().random}"

_ = system("cls")
name = input(f"{cs.INFO}Name: ")
age = input("Age: ")
offset = input("Offset: ")
now = datetime.now()
start = int((now - timedelta(days=int(age)*30)).moth)
print("Search from: 01.{start:02}{cs,END}")

# parse function
def parse(name, day, month, offset):
    HEADERS = {
        "User-Agent": User_Agent
    }
    url = f"https://telegra.ph/{name}-{month}-{day}{offset}"
    response = requests.get(url, headers = HEADERS
    soup = BeautifulSoup(response.conent, "html.parser")
    items = soup.findALL("img")
    photos = []
    print(f"Search | Start | {day}.{month}{offset}")

for item in items:
        src = item.get("src")
        if not "http"" in src:
            photos.append(f"https://telegra.ph{src}")

if photos:
    print(f"{cs.GREEN}Download | Start | {day}.{month}{offset}{cs.END}")
    if not path.isdir(f"{getcwd()}\\images"):
        mkdir(f"{getcwd()}\\images")

    if not path.isdir(f"{getcwd()}\\images\\{name}"):
        mkdir(f"{getcwd()}\\images\\{name}")

    if not path.isdir(f"{getcwd()}\\images\\{name}\\{day}_{month}_{offset[1:]}"):
        mkdir(f"{getcwd()}\\images\\{name}\\{day}_{month}_{offset[1:]}")

    for i in range(len(photos)):
        try:
            response = requests.get(photos[i], headers = HEADERS)
            with open(f"images/{name}/{day}_{month}_{offset[1:]}/{month}_{day}_{offset[1:]}_{i}.jpg", "wb") as file:
                    file.write(response.content)
                    except: pass
                    print(f"{cs.GREEN}DOWNLOAD |  End  | {day}.{month}{offset}{cs.END}")