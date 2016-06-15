#A Calculator for Geometry, specifically Area and Premeter
#Printing instructions:
#update lists: MAKE MORE AUTOMIZE


#user input shape solving for:

shape = input("What shape are you solving for?")

#changes to lower to check as standard system

shape_check = shape.lower()

while 1==1:

    #checks that they inputed right one

    if shape_check == "square" or "rectangle" or "parallelogram" or "triangle" or "trapezoid" or "circle":

        print ("You inputed %s " % (shape_check) )
        print ("Moving on...")

        #user input: formula

        Formula = input("What formula are you solving for? Please input either Area or Perimeter")

        # checks formula as standard system

        Formula_check = Formula.lower()

        #checks
        if Formula_check == "area" or "perimeter":

            print ("You inputed %s " % (shape_check) )

                #all code for solving for area
                if Formula_check == "area":

                    #square/rectangle code
                    if shape check == "square" or "rectangle" or "parallelogram":

                        #inputing the length/width to solve for rectangl
                        length = input("What is the numerical length?")
                        width = input("What is the numerical width?")
                        unit = input("What is the unit of the length/width?")

                        #solving for area
                        answer = int(length) * int(width)

                        #attaining units
                        unit =

                        print (answer)


                if Formula_check == "perimeter":

        else:

            print ("We couldn't undertand what you were typing. Please check to see if it is properly spelled!")


    else:

        print ("We couldn't undertand what you were typing. Please check to see if it is properly spelled!")
