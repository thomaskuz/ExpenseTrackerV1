# Een aparte file om alle fucnties te schrijven voor het krijgen van userdata
# zo blijft de main file wat cleaner

from datetime import datetime

def get_date(prompt , allow_default = False):
    # default zodat je niet altijd een date moet ingeven, dan wordt vandaag gekozen
    date_str = input(prompt)
    if allow_default and not date_str: # als er niks wordt ingegeven
        return datetime.today().strftime("%d-%m-%Y") # format van hoe we onze data willen krijgen
    try:
        valid_date = datetime.strptime(date_str, "%d-%m-%Y" )
        return valid_date.strftime("%d-%m-%Y")
    except ValueError:
        print(" Invalid date format. Please enter teh data in dd-mm-yyyy format")
        return get_date(prompt, allow_default= False) #recursive functie
    

def get_amount():
    pass

def get_category():
    pass

def get_description():
    pass
