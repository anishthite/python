#A Calculator for Geometry, specifically Area and Premeter
#Printing instructions:



#Getting input data

shape = input("What shape are you solving for?")
shape_check = shape.lower()

if shape_check == "square":
    print ("You inputed s% " % shape_check)
elif shape_check == "rectangle":

elif shape_check == "triangle":

elif shape_check == "trapezoid":

elif shape_check == "circle":

else:
    print ("We couldn't undertand what you were typing. Please check to see if it is properly spelled!")
