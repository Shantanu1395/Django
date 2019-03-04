import random

UNITS = 'units'
ML = 'ml'
L = 'l'
KG = 'kg'
G = 'gm'
FOOD = 'food'


#TODO - put items inside the inventory & create a mongo and create mapping for the same
class Item():
    #TODO - make a classifier for type and it should be a property of Item itself
    def __init__(self, name, quantity, unit, type):
        self.type = type
        self.quantity = quantity
        self.name = name
        self.unit = unit

    def decreaseQuantity(decreaseUnit):
        self.quantity -= decreaseUnit

    def __str__(self):
        return self.name + " : " + str(self.quantity) + " " + str(self.unit)


#TODO - get list of items based on recipie from some third party API
def computeItems(recipie):

    if recipie == "Boiled Eggs":
        return [Item("Egg", 6, UNITS, FOOD)]
    if recipie == "Oats Sweet":
        return [Item("Oats",50, G, FOOD), Item("Milk", 200, ML, FOOD)]
    if recipie == "Oats Masala":
        return []
    if recipie == "Suji Utthapam":
        return [Item("Semolina", 200, G, FOOD), Item("Curd", 100, G, FOOD), Item("Onion", 0.5, UNITS, FOOD), Item("Capsicum", 0.5, UNITS, FOOD), Item("Carrot", 0.5, UNITS, FOOD), Item("Beans", 10, UNITS, FOOD), Item("Beetroot", .25, UNITS, FOOD), Item("SweetCorn", 0.5, UNITS, FOOD)]


class Recipie():
    def __init__(self, recipie):
        self.recipieName = recipie
        self.itemsNeeded = computeItems(recipie)

class Inventory():
    def __init__(self):
        self.inventory = {
            'food' : []
        }

    def pushItem(self,item):
        if(item.type == "food"):
            self.inventory["food"].append(item)

    def getVeggies(self):
        return self.inventory["food"]


def take_input():
    return int(input())

def computeAgeForTimeLeft(expectancy):
    return expectancy - age

def computeSleepTime(time_you_sleep_per_day, time_left):
    return time_left*(time_you_sleep_per_day)/24

def removeUnavoidableThings(time_left):
    t = time_left
    things_day_basis_minutes = {
        'bath_washroom' : 30,
        'breakfast' : 20, 
        'excersize' : 60,
        'using_phone' : 30,
        'news' : 40,
        'self_learning': 60
    }

    things_5_days_a_week_hours = {
        'office' : 9.5
    }

    #Day basis
    for key, value in things_day_basis_minutes.items():
        key_percentage = ((things_day_basis_minutes[key]/60)/24)*100
        #print(str(key_percentage*time_left/100) + "years spend doing " + key)
        t -= key_percentage*time_left/100

    #Weekly Basis
    for key, value in things_5_days_a_week_hours.items():
        #Computing per month
        percentage = (((things_5_days_a_week_hours[key]*5*4 + things_5_days_a_week_hours[key]*2)*12)*t)/24/365 
        t -= percentage
    

    return t 

def getBreakfast():
    #TODO - get the recepie list from some third part API
    breakfast_list = [
        Recipie("Boiled Eggs"),
        Recipie("Oats Sweet"),
        Recipie("Oats Masala"),
        Recipie("Suji Utthapam"),
    ]
    return random.choice(breakfast_list)

def optimal_time_table():
    time_table = {
        '0700': ['WakeUp'],
        '0730': [getBreakfast(), 'bath_washroom', 'room_clean']
    }

if __name__ == "__main__":

    inventory = Inventory();
    inventory.pushItem(Item("Eggs", 5, UNITS, FOOD))
    inventory.pushItem(Item("Oil", 100, ML, FOOD))
    inventory.pushItem(Item("Barbeue Sauce", 300, ML, FOOD))
    inventory.pushItem(Item("Maggi", 4, UNITS, FOOD))

    for k,v in inventory.inventory.items():
        print(k)
        for i in v:
            print(i)

    #age = take_input()
    age = 25
    expectancy = 60
    sleep_hours = 7

    time_left_years = computeAgeForTimeLeft(expectancy)
    print("Time left if your expectancy is "+ str(expectancy) +":" + str(time_left_years) + " years")  

    sleep_time_in_years = computeSleepTime(sleep_hours, time_left_years)

    time_left_years -= sleep_time_in_years
    print("Time left after having "+ str(sleep_hours) +" hours of sleep per day:"+ str(time_left_years)  + " years")

    time_left_years = removeUnavoidableThings(time_left_years)
    print("Time left after doing unavoidable tasks :"+ str(time_left_years)  + " years")

recipie = getBreakfast()
itemNeeded = recipie.itemsNeeded
print(recipie.recipieName)
for i in itemNeeded:
    print(i)