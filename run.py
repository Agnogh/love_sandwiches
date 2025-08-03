# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# line below reads a special key file ("creds.json") and tellss Google
# that this script has permission to access that sheet
# "creds.json" is called a "ticket" to Google Sheet
# Credentials.from_service_account_file() -> loads login credentials
CREDS = Credentials.from_service_account_file('creds.json')

# this is a "scope" and it means what are we allowing
# Google to do (read spreadsheet, access files)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# this is used for logging in to the sheet - this will open spreadsheet
# gspread is called also robot assistant"
# gspread.authorize() = Logs into Google Sheets
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# this is "command" to open spreadsheet. this is the name of the 
# spreadsheet
# .open('love_sandwiches') = Opens spreadsheet by that name
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# we are specifying tab names "sales"
sales = SHEET.worksheet('sales')

# printing the list of tabs of that spreadsheet - 
# just to Check if setup is OK
print(SHEET.worksheets())

# picks up all the data from "sales" part of the sptreadsheet
# and then returns big list of rows and colums
data = sales.get_all_values()

# prints out spreadsheet data in terminal (in list form)
print(data)
