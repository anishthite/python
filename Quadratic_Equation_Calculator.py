
#This is a calculator for the Quadratic Formula
#Enjoy

#Define input variables

a = input("What's the A coeffitient?")
b = input("What's the B coeffitient?")
c = input("What's the C coeffitient?")
 

#negate coeffitient B
neg_b= int(b)*-1


#creating the square root

radicand_1= (int(b)**2)-(4*int(a)*int(c))
radicand_2= radicand_1**.5

#creating the negative and positive options

negative_root= neg_b - radicand_2
positive_root= neg_b + radicand_2

#dividing by 2a

Answer_1= positive_root/2*int(a)
Answer_2= negative_root/2*int(a)

#Printing
print ("****Note: j is the imaginary unit****")
print ("Your A coeffitient is: " + a)
print ("Your B coeffitient is: " + b)
print ("Your C coeffitient is: " + c)
print ("Answer 1 is: " + str(Answer_1))
print ("Answer 2 is: " + str(Answer_2))
