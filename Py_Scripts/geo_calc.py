#A Calculator for Geometry, specifically Area and Premeter
#Printing instructions:



#user input shape solving for:
shape = input("What shape are you solving for?")
shape_check = shape.lower()
#changes to lower to check
while 1==1:
    #checks that they inputed right one
    if shape_check == "square" or "rectangle" or "triangle" or "trapezoid" or "circle":
        print ("You inputed %s " % (shape_check) )
        print ("Moving on...")
        #user input: formula
        Formula = input("What formula are you solving for? Please input either Area or Perimeter")
        # checks formula
        Formula_check = Formula.lower()
        # changes to lower to check
        if Formula_check == "area" or "perimeter":
            #one more check
            print ("You inputed %s " % (shape_check) )
                if Formula_check == "area":
                    if shape check == "square" or "rectangle":
                        length = input("What is the numerical length?")
                        width = input("What is the numerical width?")
                        unit = input("What is the unit of the length/width?")
                        answer = int(length) * int(width)
                            if
                        print (answer)
                if Formula_check == "perimeter":
        else:
            print ("We couldn't undertand what you were typing. Please check to see if it is properly spelled!")

    else:
        print ("We couldn't undertand what you were typing. Please check to see if it is properly spelled!")
