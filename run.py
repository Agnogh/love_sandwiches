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
# sales = SHEET.worksheet('sales')

# printing the list of tabs of that spreadsheet -
# just to Check if setup is OK
# print(SHEET.worksheets())

# picks up all the data from "sales" part of the sptreadsheet
# and then returns big list of rows and colums
# data = sales.get_all_values()

# prints out spreadsheet data in terminal (in list form)
# print(data)


def get_sales_data():
    """
    get sales figures input from user
    """
    while True:     # as long as it is "true" run
        print("Please enter sales data from the last market")
        print("Data should be 6 number seperated by commas")
        print("Example: 10. 20, 30, 40, 50, 60\n")

    # data_str is assigned value to wahatever user adds after
    # the text "Enter your..."
        data_str = input("Enter your Data here: ")

    # sales_data is assigned value previously assigned "data_str" but it
    # is seperated by comma (,)
        sales_data = data_str.split(",")
    # this is taking list of values user added in step before and send it to
    # 'validate_data' function
        validate_data(sales_data)
    # prints value of "sales_data"
        print(sales_data)

        print(f'The Data provided in the {data_str}')

        if validate_data(sales_data):       # run the "validate_data" func
            print("Data is valid!")     # print statement
            break       # break out of the "while" loop


def validate_data(values):
    """
    inside the try, convert all stirngs value into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """
# print(values) was jsut for checking the code
    try:
        # this line of code is used to convert value to integers
        # for each element in 'values'
        [int(value) for value in values]
        if len(values) != 6:    # if the length/number of value is NOT 6
            raise ValueError(   # raise error,text will show up insted
                f'Exactly 6 values requiered, you provided  {len(values)}'
            )
    except ValueError as e:     # except the value error as "e" and print out
        print(f'Invalid data: {e}, try again with actual numbers\n')
        return False        # return false as validation failed
    # return "true" which means data is valid
    return True

    print(values)


get_sales_data()
