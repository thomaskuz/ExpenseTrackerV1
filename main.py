import pandas as pd #voor de csv file
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description

class CSV:
    CSV_FILE = "finance_data.csv" # Dit is een class variable
    COLUMNS=["date","amount","category","description"]

    @classmethod #dit is een decorator, deze heeft acces tot de class, maar niet tot de instance / Class (blueprint) >> Object (alle huizen gebouwd met de blueprint) >> Instance (het huis zelf)
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    @classmethod
    def add_entry(cls, date, amount , category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        } # python dictionary dat de input values van de methode mapt met de columns van de csv
        with open(cls.CSV_FILE, "a", newline="") as csvfile: # file handling syntax in python, na het grbuikt closed deze functie om memory leaks te voorkomen
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS) # dit is een csv writer, en die heeft een specifieke methode voor dictionaries te writen in csv
            writer.writerow(new_entry)
        print("entry added successfully")

def add():
    CSV.initialize_csv()
    date = get_date("Enter the data of teh transaction (dd-mm-YY) or enter for today's data: ",allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

CSV.initialize_csv()
#CSV.add_entry("20-07-2020", "5", "food", "helloooooo")

#https://youtu.be/Dn1EjhcQk64?t=916