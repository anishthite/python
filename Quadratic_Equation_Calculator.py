"""
This is a calculator for the Quadratic Formula
Enjoy
"""
#Define input variables
a = input("What's the A coeffitient?")
b = input("What's the B coeffitient?")
c = input("What's the C coeffitient?")

#negate coeffitient B
neg_b= b*-1

#square B
B_sqr= b**2

#Define the 4ac part

fourac = 4*a*c

#creating the square root

radicand_1= B_sqr-fourac
radicand_2= radicand_1**.5

#creating the negative and positive options

negative_root= neg_b - radicand_2
positive_root= neg_b + radicand_2

#dividing by 2a

Answer_1= positive_root/2*a
Answer_2= negative_root/2*a

#Printing
print ("Note: j is the imaginary unit")
print ("Your A coeffitient is: " + str(a) )
print ("Your B coeffitient is: " + str(b) )
print ("Your C coeffitient is: " + str(c) )
print ("Answer 1 is: " + str(Answer_1))
print ("Answer 2 is: " + str(Answer_2))






