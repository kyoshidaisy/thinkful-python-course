# main.py -- main file for the Bicycle Industry assignment -- #

from bicycles import Wheel, Frame, Bicycle, Bikeshop, Customer

# Wheel data
Wheel1 = Wheel("Wheel1", 2, 5)
Wheel2 = Wheel("Wheel2", 1.5, 10)
Wheel3 = Wheel("Wheel3", 0.5, 22)

# Frame data
Frame1 = Frame("Aluminum", 10, 380)
Frame2 = Frame("Carbon", 6, 700)
Frame3 = Frame("Steel", 15, 100)

# Bicycle data#
Cruiser = Bicycle("Cruiser", Wheel1, Frame3)
BMX = Bicycle("BMX", Wheel2, Frame3)
Hybrid = Bicycle("Hybrid", Wheel3, Frame3)
Hardtail = Bicycle("Hardtail", Wheel1, Frame1)
Aluroad = Bicycle("Aluroad", Wheel2, Frame1)
Carbonracer = Bicycle("Carbonracer", Wheel3, Frame2)

# shop data#
PythonCyclery = Bikeshop("PythonCyclery",
                         {
                             Cruiser: 5,
                             BMX: 7,
                             Hybrid: 4,
                             Hardtail: 3,
                             Aluroad: 4,
                             Carbonracer: 2,
                         },
                         0.20)

# Customer data#
Dave = Customer("Dave", 200)
Paul = Customer("Paul", 500)
Matt = Customer("Matt", 1000)

customers = [Dave, Paul, Matt]
bike_purchases = {}

print("\nWelcome our bike shop {}!\n".format(PythonCyclery.shopname))

# print1
# name of the customer (each) and list of bikes in their budget
bikelist = []
for customer in customers:
    print("\n\n{} Current Inventory for {}\n".format(PythonCyclery.shopname, customer.custname))
    # print(PythonCyclery.show_inventory(9999))
    # PythonCyclery.show_inventory(customer.budget)
    bikelist.extend(PythonCyclery.show_inventory(customer.budget))
    # print(bikelist)
    # bike purchase dialog -- ask customer which bike he wants from the list and return bike_purchases
    bike_to_buy = input("\n{}, Which bike are you going to buy?   : \n".format(customer.custname))
    if bike_to_buy in bikelist:
        bike_purchases[customer] = eval(bike_to_buy)
        bikelist = []
    else:
        print('please select a bike from the list')

# print2
# initial inventory of the shop
print("\nShop: {} -- Initial Inventory\n".format(PythonCyclery.shopname))
PythonCyclery.show_inventory(9999)
print('\n\n')

# print3
# have each of the customer purchase a bike
# print the name of bike, cost, rest of his fund
PythonCyclery.reset_profit()
# bike_purchases = {Dave: Cruiser, Paul: Hardtail, Matt: Carbonracer, } # For test
# print(bike_purchases) # For test
for customer in bike_purchases:
    bike_sold = bike_purchases[customer]
    bikeprice = PythonCyclery.getBikeprice(bike_sold)
    customer.purchase(bike_sold, bikeprice)
    PythonCyclery.sell_bike(bike_sold)
    print("  ")

# after each purchase, update inventory
print("{} Updated inventory".format(PythonCyclery.shopname))
PythonCyclery.show_inventory(9999)
print("   {} Total Profit is ${}".format(PythonCyclery.shopname, PythonCyclery.profit))

