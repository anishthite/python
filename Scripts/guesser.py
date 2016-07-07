#Random Number Generator 
#   By Anish Thite
#    /\
#   /  \
#  /    \
# /      \
#6/20/16

import random, sys
#Importing random and sys modules
correct_answer = random.randint(1,100)
#Setting the correct answer to a randowm output between 1 and 100, using random module
print ("I am thinking of a number between 1 and 100")
tries = 0
while True:
    print ("Guess a number, or type enter to exit:")
    guess = input(" ")
    #On one line the console prints the instructions, on the line blow it the user has option to quit, or input a number (which will be assigned to "guess")
    try:
        if int(guess) > correct_answer:
            print ("Your guess is to high! Try again!")
            tries = tries +1
            #If guess is greater than the answer, user will be notified they guessed to high. Code will reset at line 14 (the while loop)
        elif int(guess) == correct_answer:
            print ("You got the right answer!")
            print('You got the right answer in ' + str(tries) + " tries")
            sys.exit()
            #The guess and the correct_answer are equal to one another, the player has succeed and the code will terminate
        else:
            print ("Your guess is to low! Try again!")
            tries = tries +1
            #If guess is lower than the answer, user will be notified they guessed to low. Code will reset at line 14 (the while loop)
    except ValueError:
        print ("Thank you for playing!")
        sys.exit()
        #User-terminates program, displays thank you message




#
#
#old code is archived here!
#
## maximum = 10
# minimum = 1
# answer = 5
# print ("I am thinking of a number between " + str(minimum) + "and " + str(maximum))

# while 1 == 1:
#     guess = input("Hit enter to exit, or guess a number!")

#     if int(guess) > answer:
#         print ("Your guess is to high! Try again!")
#     elif int(guess) == answer:
#         print ("You got the right answer!")
#         break
#     elif guess == "":
#         break
#     else:
#         print ("Your guess is to low! Try again!")
        
#

