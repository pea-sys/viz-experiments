import json, gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

print(os.getcwd())
path = os.path.expanduser("gspread_credentials.json")
scope = ["https://spreadsheets.google.com/feeds"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
client = gspread.authorize(credentials)

ss = client.open_by_key("1dPbsB4dx2rCFtPSBGUJeC5hZ4SRroS5PtlRlifqH7mM")

print(ss.worksheets())

ws = ss.worksheet("シート1")
print(ws.col_values(1))

df = pd.DataFrame(ws.get_all_records())
print(df.info())
