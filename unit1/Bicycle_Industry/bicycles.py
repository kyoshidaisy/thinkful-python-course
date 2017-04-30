# bicycles.py -- class file for the Bicycle Industry assignment --
# Classes

class Wheel(object):
    """
    Wheel class
    model - string: wheel model name
    weight - integer: single wheel weight
    cost - integer: produce cost
    """

    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost


class Frame(object):
    """
    Frame class
    model - string: frame model name - aluminum, carbon, or steel
    weight - integer: frame weight
    cost - integer: produce cost
    """

    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost


class Bicycle(object):
    """
    model -string: Bike model name
    weight - integer: Bike wight in lbs
    cost - integer: Bike production cost
    - Be comprised of two wheels of the same type and a frame
    - Have a weight equal to the sum of the weight of the frame and two wheels
    - Have a cost to produce equal to the sum of the two wheels' and frame's cost to produce
    """

    def __init__(self, model, wheeltype, frametype):
        self.model = model
        self.wheeltype = wheeltype
        self.frametype = frametype

    def weight(self):
        bikeweight = (self.wheeltype.weight * 2) + self.frametype.weight
        return bikeweight

    def cost(self):
        bikecost = (self.wheeltype.cost * 2) + self.frametype.cost
        return bikecost

class Bikeshop(object):
    """
    shopname -string: Bile shop name = 'Python Cyclery'
    inventory -dic: Bike model [key] and inventory count [value] as integer
    margin - float - Percentage of bike sales price addition = 20%
    profit - integer: Total profit made on bike sales = (cost * margin) / 100.0
    """

    def __init__(self, shopname, inventory=None, margin=0.20):
        if inventory is None:
            inventory = {}
        self.shopname = shopname
        self.inventory = inventory
        self.margin = margin

    def getBikeprofit(self, bicycle):
        return int(bicycle.cost() * self.margin)

    def getBikeprice(self, bicycle):
        return bicycle.cost() + self.getBikeprofit(bicycle)

    def sell_bike(self, bicycle):
        """Sell bicycle with the price, return profit, and add to sales balance"""
        # Check if bike is available in inventory
        if self.inventory[bicycle] > 0:
            # Call the bike profit
            bikeprofit = self.getBikeprofit(bicycle)
            # print(bikeprofit) # For test
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
            bikeprice = self.getBikeprice(b)
            if bikeprice < price_limit:
                bikelist.append(b.model)
                print("{}    {}    ${}".format(b.model, self.inventory[b], bikeprice))
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

    def __init__(self, custname, budget, bicycle=None):
        self.custname = custname
        self.budget = budget
        self.bicycle = bicycle

    def purchase(self, bicycle, bikeprice):
        """Customer purchases bike and reduce budget"""
        self.bicycle = bicycle
        self.budget -= bikeprice
        # Confirmation
        print("Congrats {}, you bought {} for ${}. It's nice bike! You have ${} remaining of your budget.".format(
            self.custname, bicycle.model, bikeprice, self.budget))
