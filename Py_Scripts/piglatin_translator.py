#Piglatin translator

original = input("Type or copy words into here")


if len(original) == 0 and  original.isalpha() == False :
    print ("Please type in something")
    original = input("Try again here...")
else:
    print ("Hold on, your text is translating")

ay = "ay"
lat = (original [0])

print (lat)
print (ay)
print (original + ay)
print (original - lat )
