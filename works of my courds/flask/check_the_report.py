import requests
import pandas as pd
from bs4 import BeautifulSoup

import sqlite3


dbname = "Test.db"
with sqlite3.connect(dbname) as conn:
    cur = conn.cursor()
    cur.execute("")
    cur.commit()


"""
url = "https://www.nature.com/articles/s41467-021-22236-7"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
print(soup.find("div", id="Abs1-content").get_text())
"""
