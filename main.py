import requests

url = "https://www.activestate.com/blog/top-10-must-have-python-packages/"

davide = requests.get(url)
source_code = davide.text

with open("moduls.html", "w") as f:
    f.write(source_code)

