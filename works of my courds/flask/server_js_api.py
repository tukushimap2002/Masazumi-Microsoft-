import requests
import pandas as pd
from flask import Flask, request
from bs4 import BeautifulSoup
from flask_cors import CORS

from plugins import gsptest

app = Flask(__name__)
# JSからのリクエストでエラーをはかないためのおまじない。
CORS(app)

@app.route('/', methods=["GET"])
def index():
    try:
        req = request.args
        load_url = req.get("load_url")
        html = requests.get(load_url)
        soup = BeautifulSoup(html.content,"html.parser")
        text = soup.get_text()
        # print("before gsptest")
        word_list = gsptest.get_wordlist()
        # print("after gsptest")
        print(text)
        for i in word_list:
            finding = text.find(i)
            counting = text.count(i)
            print(text[finding - 30:finding + len(i)])
            print(i)
            print(counting)
        # text.find(word_list)
    
    except:
        print("error")
    return "OK"        


if __name__ == "__main__":
    app.run(port=8000, debug=True)

# """
# url = "https://www.nature.com/articles/s41467-021-22236-7"
# r = requests.get(url)
# soup = BeautifulSoup(r.content, "html.parser")
# print(soup.find("div", id="Abs1-content").get_text())
# """
