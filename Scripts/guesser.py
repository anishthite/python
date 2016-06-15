maximum = 10
minimum = 1
answer = 5
print ("I am thinking of a number between " + str(minimum) + "and " + str(maximum))

while 1 == 1:
    guess = input("Hit enter to exit, or guess a number!")

    if int(guess) > answer:
        print ("Your guess is to high! Try again!")
    elif int(guess) == answer:
        print ("You got the right answer!")
        break
    elif guess == "":
        break
    else:
        print ("Your guess is to low! Try again!")
        
