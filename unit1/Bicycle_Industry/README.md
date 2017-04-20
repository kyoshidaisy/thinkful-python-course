Bicycle Industry assignment

Model the Bicycle Industry
https://courses.thinkful.com/pip-001v3/project/1.3.4

04/19/2017

To do: 
1. fix the error of bike_purchases

2.  Disallow the purchase when the budget is negative: do after 1.5

3. start extention exercise


**Extension Exercise**

If the extra challenges were not a problem and you're running ahead of schedule then you could try to extend your model even further to add bicycle manufacturers.

Alter your classes
You should add one or more classes to represent:

Bicycle Manufacturers
Have a name
Produce three models of bikes each
Have a percentage over cost which they sell bikes to bike shops at
Then you should modify your Bicycle class again. The updated class should:

Bicycle
Have a manufacturer
Update your testing script
The testing script should be modified so that it:

Creates two bicycle manufacturers, which both produce three different bicycle models
Makes the bike shops stock their inventory by purchasing bikes from manufacturers

04/14/2017 create altclass branch for extra challenge task

04/14/2017 extend branch
Still no clue about the error:

Traceback (most recent call last):
  File "/home/koji/PycharmProjects/thinkful-python-course/unit1/Bicycle_Industry/main.py", line 67, in <module>
    customer.purchase(bike_sold)
AttributeError: 'str' object has no attribute 'purchase'


04/13/2017 extend branch
Added purchase selection dialog -- error line 67 of main.py --
line 49: bike_purchases[customer.custname] = bike_to_buy
-- expected like: bike_purchases = {Dave: Cruiser, Paul: Hardtail, Matt: Carbonracer, }
 however reality is {'Dave': 'Cruiser', 'Paul': 'Cruiser', 'Matt': 'Cruiser'} dic attributes became strings...


4/6/2017

Fixed the error

**To do:**

1. Add dialog purchase selection (Now purchase is fixed in main.py): added
1.5. error of bike_purchases fix needed

2.  Disallow the purchase when the budget is negative: do after 1.5

_**Work for extra challenge:**_ to create branch altclass done: 04/18/2017

Alter your classes
You should add new classes to represent the following bike parts:

Wheels
Have a model name
Have a weight
Have a cost to produce
There should be a total of three different wheel types
Frames
Can be made of aluminum, carbon, or steel
Have a weight
Have a cost to produce
Then you should modify your Bicycle class. The updated class should:

Bicycle
Be comprised of two wheels of the same type and a frame
Have a weight equal to the sum of the weight of the frame and two wheels
Have a cost to produce equal to the sum of the two wheels' and frame's cost to produce
You may also need to update your testing script to reflect the changes that you have made here.

