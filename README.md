# MySQL dump to Google Sheets

Tool to make a dump of your MySQL tables to your Google Sheet document.

By default, it copies each table in a different worksheet.


## Requirements

Python 3+

Libraries:

`pip install mysql-connector` # MySQL Connector
`pip install gspread oauth2client PyOpenSSL` # Neccesary to connect with Google Sheets API

* [Getting Google API's credentials](http://gspread.readthedocs.io/en/latest/oauth2.html)



## Usage

1. Fill the files config.py with your MySQL parameters and the queries.py with the queries for each table in your database.

2. Create a GSheet document in your Google Drive account. You have to create different worksheets with the names of the tables of the previous step. Remind to share this document with edit permissions with the *client_email* parameter of your Google API's credentials. Wait a couple of minutes to make effective the propagation.

3. Run `python main.py` and magically, your worksheets are filled and with the name of columns too!




## Troubleshooting

- If there are datetime objects or None objects in the queries, maybe it's neccessary to convert to string.

*Example: CAST(`createdOn` as char) as createdOn*
