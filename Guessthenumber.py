#Helder
#12/09/22
#guessTheNumber

import random #imports the random library

myname= ("Please enter your name :")
number = random.randint(1,10)#generates a random number between 1-10
print ("Well, ",myname,"I am thinking of a number between 1 and 10")
guess= int(input("Take a guess :"))
if guess == number:
    print ("Well done, ",myname, "You guessed my number")
else:
    print ("Incorrect, better luck next time")
                 
                 
