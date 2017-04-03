# main.py -- class file for the Bicycle Industry assignment -- #

from bicycle import Bicycle, Bikeshop, Customer

# Bicycle data#

Cruiser = Bicycle("Cruiser", 17, 150)
BMX = Bicycle("BMX", 16, 210)
Hybrid = Bicycle("Hybrid", 15, 300)
Hardtail = Bicycle("Hardtail", 12, 400)
Aluroad = Bicycle("Aluroad", 10, 600)
Carbonracer = Bicycle("Carbonracer", 7, 850)

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

# print1
# name of the customer (each) and list of bikes in their budget
for customer in customers:
    print("{} Current Inventory for {}".format(PythonCyclery.shopname, customer.custname))
    PythonCyclery.show_inventory(customer.budget)
    print('\n\n')

# print2
# initial inventory of the shop
print("Shop: {} -- Initial Inventory".format(PythonCyclery.shopname))
PythonCyclery.show_inventory()
print('\n\n')

# print3
# have each of the customer purchase a bike
# print the name of bike, cost, rest of his fund
PythonCyclery.reset_profit()
bike_purchases = {Dave: Cruiser, Paul: Hardtail, Matt: Carbonracer, }
print("Bike purchases")
for customer in bike_purchases:
    bike_sold = bike_purchases[customer]
    customer.purchase(bike_sold, PythonCyclery.price(bike_sold))
    PythonCyclery.sell_bike(bike_sold)
    print("  ")

# after each purchase, update inventory
print("{} Updated inventory".format(PythonCyclery.shopname))
PythonCyclery.show_inventory()
print("   {} Total Profit is ${}".format(PythonCyclery.shopname, PythonCyclery.profit))
