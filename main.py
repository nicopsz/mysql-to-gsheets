import mysql.connector, os, json, gspread, queries
from oauth2client.service_account import ServiceAccountCredentials

from config import MYSQL_CONFIG


# --- Google Account Authorization --- #

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('XXXXXXX.json', scope) # TODO: Put your json keyfile name
gc = gspread.authorize(credentials)


# --- MySQL --- #

# Connection
cnx = mysql.connector.connect(user = MYSQL_CONFIG['user'],
              password = MYSQL_CONFIG['pass'],
              host = MYSQL_CONFIG['host'],
              database = MYSQL_CONFIG'db'])

cursor = cnx.cursor(dictionary = True)

# ------------- #

# Update worksheets

for i in (queries.tables.keys()):

    cursor.execute(queries.tables[i])
    rows = cursor.fetchall()

    wks = gc.open("dbdump").worksheet(i)
    wks.clear() # Clear all data first


    #     Add columns names and rows

    columns = list(rows[0].keys())
    cell_list = wks.range(1, 1, len(rows) + 1, len(columns))

    j = 0

    for i in range(len(columns)):
        cell_list[i].value = columns[i]
        j += 1

    for row in rows:
        for i in range(len(columns)):
            cell_list[j].value = row[columns[i]]
            j += 1

    wks.update_cells(cell_list)


cursor.close()
cnx.close()
