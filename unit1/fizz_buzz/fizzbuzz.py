#get hard corded upperline: n
	#if user supplies a value in CL
	
import sys

try:
	if len(sys.argv) >= 2:

		for arg in sys.argv[1:]:
			n = int(arg)

	else: 
		n = int(input("Enter the number you like from 1 - 100?   "))
	
	if n > 100:
		print("Please enter number from 1 to 100")

	else:
		print("Your call is {}. Let's start!".format(n))

except ValueError:
	print("It's not a number! Please enter number from 1 to 100")
	n = int(input("Enter the number you like from 1 - 100?   "))
	
#Fizzbuzz counting up to n : num
num = 1
counting = True

while counting:
	if num <= n:
#condition to replace with Fizzes, Buzzes and Fizzbuzzes
		if num % 3 == 0 and num % 5 == 0:
			print("FizzBuzz!")

		elif num % 3 == 0:
			print("Fizz")
		
		elif num % 5 == 0:
			print("Buzz")		
			
#Print out each number from 1 to number		
		else:
			print(num)
		num += 1

	else:
		counting = False

print("done!")
		
