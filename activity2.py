def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if "islamabad"==city:
        return 183
    elif "tampa"==city:
        return 220
    elif "pittsburgh"==city:
        return 222
    elif "los Angeles"==city:
        return 457
def rental_car_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40* days
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)
print("total cost of the trip:",trip_cost( "los Angeles",7,500))