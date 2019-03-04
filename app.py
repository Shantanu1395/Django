from __future__ import division

#TODO - put items inside the inventory & create a mongo and create mapping for the same
class Item():
    def __init__(self, name, quantity, name):
        self.type = type
        self.quantity = quantity
        self.name = name 

    def decreaseQuantity(decreaseUnit):
        self.quantity -= decreaseUnit 


class Inventory():
    def __init__(self):
        self.inventory = {}

    def pushItem(item):
        

inventory = {
    'vegetables':{
        'available':[],
        'notAvailable':[]
    } 
}

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
    for key, value in things_day_basis_minutes.iteritems():
        key_percentage = ((things_day_basis_minutes[key]/60)/24)*100
        #print(str(key_percentage*time_left/100) + "years spend doing " + key)
        t -= key_percentage*time_left/100

    #Weekly Basis
    for key, value in things_5_days_a_week_hours.iteritems():
        #Computing per month
        percentage = (((things_5_days_a_week_hours[key]*5*4 + things_5_days_a_week_hours[key]*2)*12)*t)/24/365 
        t -= percentage
    

    return t 

def getBreakfast():
    #TODO - get the recepie list from some third part API
    breakfast_list = {
        'BoiledEggs' : ["eggs"],
        'OatsSweet' :  ["oats"]'
        'OatsMasala' : ["oats"],
        'SujiUthhapam': ["suji", "eno", "curd", inventory.getVeggies()]
    }

def optimal_time_table():
    time_table = {
        '0700': ['WakeUp'],
        '0730': [getBreakfast, 'bath_washroom', 'room_clean']
    }

if __name__ == "__main__":
    
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