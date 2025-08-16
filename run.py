# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
# from pprint import pprint
# import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# creds = json.load(open('creds.json'))

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
    get sales figures input from user.
    Run as long as user doesn't provide 6 values that can be
    converted as integers
    """
    while True:     # as long as it is "true" run
        print("Please enter sales data from the last market")
        print("Data should be 6 number seperated by commas")
        print("Example: 10. 20, 30, 40, 50, 60\n")

    # data_str is assigned value to wahatever user adds after
    # the text "Enter your..."
        data_str = input("Enter your Data here: \n")

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
            #  break       # break out of the "while" loop
            return sales_data


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


"""
def update_sales_worksheet(data):
    """ """
    update sales worksheet, add new row with the list data provided.
    """ """
    print("Updating sales worksheet... \n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully. \n")


def update_surplus_worksheet(data):
    """ """
    update surplus worksheet, add new row with the list data provided.
    """ """
    print("Updating surplus worksheet... \n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated successfully. \n")
"""


def update_worksheet(data, worksheet):
    """
    recieves a list of integers to be insterted itno a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f'Updatind {worksheet} worksheet...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet update sucessuflly')


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - positive surplus inidcates waste
    - negative surplus indicate extra made when the stocks was sold out.
    """
    print("Calculating surplus data...\n")
    # getting the data from Stock sheet and get all values
    stock = SHEET.worksheet("stock").get_all_values()
    # pprint(stock)
    stock_row = stock[-1]
    # print(f'stoc row: {stock_row}')
    # print(f'sales wor: {sales_row}')

    surplus_data = []
    # we are going through sales and stock rown
    for stock, sales in zip(stock_row, sales_row):
        # then caluclate surplus by substracting sales form stock
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data


def get_last_5_entry_sales():
    """
    collects collumns of data from sales worksheet, collecting
    the last 5 entries for each sandwiches and returns the data
    as a list of lists
    """
    sales = SHEET.worksheet("sales")
    # column = sales.col_values(3)
    # print(column)

    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        # we want last 5 items, and colons for multiple items
        columns.append(column[-5:])
    # we do not need pprint anymore
    # pprint(columns)

    return columns


def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating Stocks Data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    # print(new_stock_data)
    return new_stock_data


def main():
    """
    run all program function
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    # calling the function "calculate_surplus_data" with sales_data variable
    # calculate_surplus_data(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    print(new_surplus_data)
    sales_colums = get_last_5_entry_sales()
    stock_data = calculate_stock_data(sales_colums)
    update_worksheet(stock_data, "stock")
    # return stock_data


print("Welcome to Love sandiches data automation")
# calling out my main function
main()
# stock_data = main()

# get_last_5_entry_sales()
