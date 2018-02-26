#Guessing number game

#!/usr/bin/env python3

import random
number = random.randint(1,10)
tries =1

uname=input("Hello, What's your name?")
print("Hello",uname + ".", )

question=input("Would you like to play a game? [Y?N]")
if question == 'N':
	print("Oh,okay :( ")
if question == 'Y':
	print("I have a number between 1 to 10. ")
	guess=int(input("Guess"))
	if guess > number:
		print("Guess lower")
	if guess < number:
		print("Guess higher")
	while guess != number:
		tries +=1
		guess = int(input("Try again!"))
		if guess < number:
			print("Guess higher")
		if guess > number:
			print("Guess lower")
		if guess == number:
			print("You're right! The number was",number,"and it only took ", tries , "tries")
