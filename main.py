import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description  #importing from the "data_entry" file into this one

class CSV: 
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod        #initialize the CSV file
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)  
            df.to_csv(cls.CSV_FILE, index=False)    

    @classmethod        #add the entry
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")


def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction ()")
    amount = get_amount ()

CSV.initialize_csv()    #TEST to see if it creates the directory "finance_data.csv"
CSV.add_entry("14-07-2024", 125.65, "Income", "Salary")