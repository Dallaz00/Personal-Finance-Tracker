import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description  #importing from the "data_entry" file into this one

class CSV: 
    CSV_FILE = "finance_data.csv"  # The name of the CSV file
    COLUMNS = ["date", "amount", "category", "description"]  # The column headers for the CSV file
#Variables
    FORMAT = "%d-%m-%Y"     # The format for dates in the CSV file

    @classmethod  # A class method to initialize the CSV file
    def initialize_csv(cls):
        """
        Initialize the CSV file if it doesn't exist.
        If the file exists, do nothing.
        """
        try:
            # Try to read the CSV file
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame with the column headers
            df = pd.DataFrame(columns=cls.COLUMNS)  
            # Write the DataFrame to the CSV file
            df.to_csv(cls.CSV_FILE, index=False)  

    @classmethod  # A class method to add an entry to the CSV file
    def add_entry(cls, date, amount, category, description):
        """
        Add a new entry to the CSV file.
        :param date: The date of the transaction
        :param amount: The amount of the transaction
        :param category: The category of the transaction
        :param description: The description of the transaction
        """
        # Create a new dictionary to represent the entry
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }

        # Open the CSV file in append mode
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            # Create a DictWriter to write the entry to the CSV file
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            # Write the entry to the CSV file
            writer.writerow(new_entry)
        # Print a success message
        print("Entry added successfully")

    @classmethod  # A class method to get transactions within a date range
    def get_transactions(cls, start_date, end_date):    
        """
        Get all transactions within a date range.
        :param start_date: The start date of the range (inclusive)
        :param end_date: The end date of the range (inclusive)
        """
        # Read the CSV file into a DataFrame
        df = pd.read_csv(cls.CSV_FILE)      
        # Convert the 'date' column to datetime format
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        # Convert the start and end dates to datetime format
        start_date = datetime.strptime(start_date, CSV.FORMAT)      
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        
        # Create a mask to filter the DataFrame
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        # Filter the DataFrame using the mask
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            # If no transactions were found, print a message
            print('No transactions found in the given date range')
        else:
            # Print the transactions
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
                )
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

def add():
    """
    Add a new transaction to the CSV file.
    """
    # Initialize the CSV file
    CSV.initialize_csv()
    # Get the date of the transaction
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or press 'Enter' for today's date: ", 
        allow_default=True,
        )
    # Get the amount of the transaction
    amount = get_amount ()
    # Get the category of the transaction
    category = get_category()
    # Get the description of the transaction
    description = get_description()
    # Add the transaction to the CSV file
    CSV.add_entry(date, amount, category, description)

# Initialize the CSV file
CSV.initialize_csv()    
# Add a test entry to the CSV file
CSV.add_entry("14-07-2024", 125.65, "Income", "Salary")

# Add a new transaction
add()