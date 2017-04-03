## bicycle.py -- class file for the Bicycle Industry assignment -- ##
# Class


class Bicycle(object):
    """
    model -string: Bike model name
    weight - integer: Bike wight in lbs
    cost - integer: Bike production cost
    """

    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost


class Bikeshop(object):
    """
    shopname -string: Bile shop name = 'Python Cyclery'
    inventory -dic: Bile model [key] and inventory count [value] as integer
    margin - float - Percentage of bike sales price addition = 20%
    profit - integer: Total profit made on bile sales = (cost * margin) / 100.0
    """

    def __init__(self, shopname, inventory=None, margin=0.0):
        if inventory is None:
            inventory = {}
        self.shopname = shopname
        self.inventory = inventory
        self.margin = margin
        self.profit = 0

    def price(self, bicycle):
        """Return sale price for a bike"""
        bikeprice = int(bicycle.cost() + (bicycle.cost() * self.margin))
        return bikeprice

    def sell_bike(self, bicycle):
        """Sell bicycle with the price, return profit, and add to sales balance"""
        # Check if bike is available in inventory
        if self.inventory[bicycle] > 0:
            # Calc the bike profit
            bikeprofit = self.price(bicycle) - bicycle.cost()
            # Add profit to profit balance
            self.profit += bikeprofit
            # Remove bike from inventory stock
            self.inventory[bicycle] -= 1
            # Confirmation
            print("{} has successfully sold a {} for ${}.".format(self.shopname, bicycle.model, bikeprofit))
        else:bn
            print("{} bike is not in stock. Sorry.".format(bicycle))

    def show_inventory(self, price_limit=9999):
        """ Show inventory with bike name, sale price with optional price limit for customer budget"""
        print("Name    Count    Sale Price")
        for bicycle in self.inventory:
            bikeprice = self.price(bicycle)
            if bikeprice < price_limit:
                print("{}    {}    ${}".format(bicycle.model, self.inventory[bicycle], bikeprice))

    def reset_profit(self):
        """ Reset profit balance to zero """
        self.profit = 0


class Customer(object):
    """
    Bike customer with:
    custname -string: Customer Name
    budget -integer: Customer funds used for purchasing a bike
    custbike - bicycle class: Bike owned by customer
    """

    def __init__(self, custname, budget, bicycle=None):
        self.custname = custname
        self.budget = budget
        self.bicycle = bicycle

    def purchase(self, bicycle, bikecost):
        """Customer purchases bike and reduce budget"""
        self.bicycle = bicycle
        self.budget -= bikecost
        # Confirmation
        print("Congrats {}, you bought {} for ${}. It's nice bike! You have ${} remaining of your budget.".format(
            self.custname, bicycle.model, bikecost, self.budget))
