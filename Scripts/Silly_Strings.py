#Created to work with and test out string operators
#Author: Anish Thite, 2016

name = "Mike"
print "Hello %s" % (name)
#The % operator after a string is used to combine a string with variables. The % operator will replace a %s in the string with the string variable that comes after it.

print " What is your name "
name = raw_input("?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

#test out bug from 2.7 Python
Anish = "it's literal's"
print (Anish)

#first try is a success!

#test out way to see indexes

(A) = ("anish" [0])
print (A)

#first try is a success!



#Going to test out some string operators I leared"

Anish = ("Anish")
print (len(Anish))

#------------------
print(Anish.lower())

 #------------------
print (Anish.upper())
 #------------------
pi = 3.14
print (str(pi))
 #------------------

print ("Anish " + "is " + "cool!")



#--------------------

import(datetime)
