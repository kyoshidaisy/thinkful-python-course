##main.py -- class file for the Bicycle Industry assignment -- ##

from bicycle import Bicycle, Bikeshop, Customer

#Bicycle data#
	#model list
models = ["Cruiser", "Citybike", "Hybrid", "Hardtail", "Aluroad", "Carbonracer"]
	#weight dict
weight = {
		models[0]:17, 
		models[1]:16, 
		models[2]:15,
		models[3]:12,
		models[4]:10,
		models[5]:7,
		}
	#cost data#
cost = {
		models[0]:150, 
		models[1]:210, 
		models[2]:300,
		models[3]:400,
		models[4]:600,
		models[5]:750,
		}


	
#shop data#
shopname = "Python Cyclery"
margin = 20


#Customer data#
custnames = ["Dave", "Paul", "Matt"]
budget = {
		custnames[0]:200, 
		custnames[1]:500, 
		custnames[2]:1000,
		}		

#print1
#name of the customer (each) and list of bikes in their budget
for custname in custnames:
	print(custname)
	custname.list_bike()
#print2
#initial inventory of the shop
	print(shopname)
	shopname.show_inventory()

#print3
#have each of the customer purchase a bike
#print the name of bike, cost, rest of his fund
#after each purchase, update inventory
for custname in custnames:
	custname.purchase()
#after all three, print the shop's profit made.
shopname.sales()
	


