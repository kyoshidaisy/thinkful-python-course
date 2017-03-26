##Pirate Bartender Project Unit 1 Lesson3-2##

import random
#Create questions and ingredients dictionaries

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#Function: tasteq: q from dic - gather the response to new dic

#quetions from question dic: Boolearn
#per question, answered "yes" taste will be fragged
#get boolean as key value

def asking():
	"""I collect the user's prefs and put it into new dic"""
	answers = {}
	for key, value in questions.items():
		user_input = input(value + " (yes or no) ")
		answers[key] = (user_input == "y" or user_input == "yes")
	return answers

			
#function: drink: constract drink
def recipe(value):
	""" user the answers to make a drink.""" 
	your_drink = []
	for key, value in value.items():
		if value is True:
			your_drink.append(random.choice(ingredients[key]))
#return drink recipe
	return your_drink
	
#privide a main function

def main():
	results = asking()
	print("\n All right. From your answer, I made a drink with a:")
	for your_drink in recipe(results):
		print("    " + your_drink)

if __name__=='__main__':
	main()
