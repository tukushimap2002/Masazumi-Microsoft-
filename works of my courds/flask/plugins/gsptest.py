import gspread
import json
import pathlib
from oauth2client.service_account import ServiceAccountCredentials 

def get_wordlist():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    json_path = pathlib.Path(__file__).joinpath(
        "..", "yoshida-308915-2643f6a6642a.json"
    ).resolve()

    credentials = ServiceAccountCredentials.from_json_keyfile_name(str(json_path), scope)

    gc = gspread.authorize(credentials)

    SPREADSHEET_KEY = '1M8ftIyUvRuyHMXizMU4CvhQj2vM7TqPQ3t6CHKSdHNc'

    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    word_list = worksheet.col_values(2)
    # word_list => ["covid19","the U.S.", ....]   
    return word_list
