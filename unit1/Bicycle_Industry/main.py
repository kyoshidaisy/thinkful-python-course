# main.py -- class file for the Bicycle Industry assignment -- #

from bicycles import Bicycle, Bikeshop, Customer

# Bicycle data#

Cruiser = Bicycle("Cruiser", 17, 150)
BMX = Bicycle("BMX", 16, 210)
Hybrid = Bicycle("Hybrid", 15, 300)
Hardtail = Bicycle("Hardtail", 12, 400)
Aluroad = Bicycle("Aluroad", 10, 600)
Carbonracer = Bicycle("Carbonracer", 7, 800)

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
    print("{} Current Inventory for {}".format(PythonCyclery.shopname, customer.custname))
    # print(PythonCyclery.show_inventory(9999))
    PythonCyclery.show_inventory(customer.budget)
    print('\n\n')
    bikelist.extend(PythonCyclery.show_inventory(customer.budget))
    print(bikelist)
    # bike purchase dialog -- ask customer which bike he wants from the list and return bike_purchases
    bike_to_buy = str(input("\n\n{}, Which bike are you going to buy?   :".format(customer.custname)))
    if bike_to_buy in bikelist:
        bike_purchases[customer.custname] = bike_to_buy
    else:
        print('please select a bike from the list')

# print2
# initial inventory of the shop
print("Shop: {} -- Initial Inventory".format(PythonCyclery.shopname))
PythonCyclery.show_inventory(9999)
print('\n\n')

# print3
# have each of the customer purchase a bike
# print the name of bike, cost, rest of his fund
PythonCyclery.reset_profit()
# bike_purchases = {Dave: Cruiser, Paul: Hardtail, Matt: Carbonracer, }
print(bike_purchases)
for customer in bike_purchases:
    bike_sold = bike_purchases[customer]
    customer.purchase(bike_sold)
    PythonCyclery.sell_bike(bike_sold)
    print("  ")

# after each purchase, update inventory
print("{} Updated inventory".format(PythonCyclery.shopname))
PythonCyclery.show_inventory(9999)
print("   {} Total Profit is ${}".format(PythonCyclery.shopname, PythonCyclery.profit))

