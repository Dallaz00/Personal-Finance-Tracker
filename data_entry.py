from datetime import datetime

date_format = "%d-%m-%Y"     #VARIABLE created for better simplicity date_time can not be called instead of "%d-%m-%Y"

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:      #If user just hit enter without any input - will return date/month/year
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)        #converting into a datetime object using this
        return valid_date.strftime(date_format)                       #converting back into a date/month/year
    except ValueError:
        print("Invalid date input. Please enter the date in the dd-mm-yyyy format.")        #if they user types something unrelated
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative, non zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    pass

def get_description():
    pass