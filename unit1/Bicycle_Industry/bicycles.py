# bicycles.py -- class file for the Bicycle Industry assignment --
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

    def price(self):
        """Return sale price for a bike"""
        bikeprice = int(self.cost * 1.20)
        # bikeprice = 8
        return bikeprice


class Bikeshop(object):
    """
    shopname -string: Bile shop name = 'Python Cyclery'
    inventory -dic: Bike model [key] and inventory count [value] as integer
    margin - float - Percentage of bike sales price addition = 20%
    profit - integer: Total profit made on bike sales = (cost * margin) / 100.0
    """

    def __init__(self, shopname, inventory=None, margin=0.0):
        if inventory is None:
            inventory = {}
        self.shopname = shopname
        self.inventory = inventory
        self.margin = margin
        self.profit = 0

    def sell_bike(self, bicycle):
        """Sell bicycle with the price, return profit, and add to sales balance"""
        # Check if bike is available in inventory
        if self.inventory[bicycle] > 0:
            # Calc the bike profit
            bikeprofit = (Bicycle.price(bicycle) - bicycle.cost)
            # Add profit to profit balance
            self.profit += bikeprofit
            # Remove bike from inventory stock
            self.inventory[bicycle] -= 1
            # Confirmation
            print(
                "({} has successfully sold a {} and made ${} profit.)".format(self.shopname, bicycle.model, bikeprofit))
        else:
            print("{} bike is not in stock. Sorry.".format(bicycle))

    def show_inventory(self, price_limit):
        """ Show inventory with bike name, sale price with optional price limit for customer budget"""
        if price_limit is None:
            price_limit = 9999
        print("Name    Count    Sale Price")
        bikelist = []  # available bike list: use for bike purchase selection
        for b in self.inventory:
            saleprice = Bicycle.price(b)
            if saleprice < price_limit:
                bikelist.append(b.model)
                print("{}    {}    ${}".format(b.model, self.inventory[b], saleprice))
        return bikelist

    def reset_profit(self):
        """ Reset profit balance to zero """
        self.profit = 0


class Customer(object):
    """
    Bike customer with:
    custname -string: Customer Name
    budget -integer: Customer funds used for purchasing a bike
    bicycle - bicycle class: Bike owned by customer
    """

    def __init__(self, custname, budget):
        self.custname = custname
        self.budget = budget

    def purchase(self, bicycle):
        """Customer purchases bike and reduce budget"""
        bikeprice = Bicycle.price(bicycle)
        self.bicycle = bicycle
        self.budget -= bikeprice
        # Confirmation
        print("Congrats {}, you bought {} for ${}. It's nice bike! You have ${} remaining of your budget.".format(
            self.custname, bicycle.model, bikeprice, self.budget))
