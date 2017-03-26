##bicycle.py -- class file for the Bicycle Industry assignment -- ##
#Class

class Bicycle(object):
	model = ' '
	weight = 0
	cost = 0
	
	def __init__(self, model, weight, cost):
		self.model = model
		self.weight = weight
		self.cost = cost
		

class Bikeshop(object):
	shopname = 'Python Cyclery'
	inventory = {}
	margin = 20
	profit = (cost * margin) / 100.0
	
	def __init__(self, shopname):
		self.inventory = inventory
		self.margin = margin
		self.profit = profit
	
	def show_inventory(self):
		stock = model
		price = cost + profit
		for k, v in inventory.items():
			inventory[stock] = price
			print(k, v)
		print
	
	
	def sales(self):
		revenue = ()
		sold = custbike()
		revenue = revenue + profit(sold)
		print(sum(revenue))
		
class Customer(object):
	custname = ' '
	budget = 0
	custbike = ' '
	
	def __init__(self, custname):
		self.budget = budget
		self.custbike = custbike
	
	def list_bike(self):
		listing = {}
		for k, v in intentory.items():
			if inventory.value >= budget[custname]:
				listing[key] = inventory.value
				print(k,v)
			else:
				print("Sorry, No matched bike is available.")
		print()	
	
	def purchase(self):
		for k, v in listing.items():
			candidate_bike = listing[key]
			answer = raw_input("Would you like to take {}?    (yes or no)".format(candidate_bike))
            if answer.lower() == 'y' or answer.lower() == 'yes':
			    new_budget = (budget[custname] - price)
			    budget[custname] = new_budget
			    custbike = candidate_bike
			    del inventory[custbike]
			    print("Thank you! {0}, The bike {1} is good bike. The price is {2} Your fund is now {3} left.".format(custname, custbike, price, new_budget)
			
		    else:
				print("Okay.., Let's move on")
		return
			print(inventory.items)
			shopname.sales()



if __name__ == "__main__":
