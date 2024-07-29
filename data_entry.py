# Een aparte file om alle fucnties te schrijven voor het krijgen van userdata
# zo blijft de main file wat cleaner

from datetime import datetime


date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income",
              "E": "Expense"} #dictionary

def get_date(prompt , allow_default = False):
    # default zodat je niet altijd een date moet ingeven, dan wordt vandaag gekozen
    date_str = input(prompt)
    if allow_default and not date_str: # als er niks wordt ingegeven
        return datetime.today().strftime(date_format) # format van hoe we onze data willen krijgen
    try:
        valid_date = datetime.strptime(date_str, date_format )
        return valid_date.strftime(date_format)
    except ValueError:
        print(" Invalid date format. Please enter teh data in dd-mm-yyyy format: ")
        return get_date(prompt, allow_default= False) #recursive functie
    

def get_amount():
    try:
        amount = float(input("enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a number higher than 0")
        return amount # return goede waarde
    except ValueError as e:
        print(e)
        return get_amount() # recursion totdat er een goede waarde wordt uitgevoerd.



def get_category():
    category = input("Please enter cat: 'I for income' or 'E for expense': " ).upper()
    if category in CATEGORIES:
        return CATEGORIES[category] #returnt de value in de dictionary by de key category
    print("invalid category, please enter 'I' or 'E' " )
    return get_category() # recursive

def get_description():
    return input("Enter a description (optional): ")

# Deze file importen in de main file zodat deze functies opgeroepen kunnen worden