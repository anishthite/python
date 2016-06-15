#Greet-Bot- says a customary greeting
'''
print('Hello there!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
'''


pyg = 'ay'

original = input("Enter a word")

if len(original) > 0 and original.isalpha():
    print (original)
    word = original.lower()
    first = word[0]
    new_word = word + first +  pyg
    new_word = new_word[1:]
else:
    print ('empty')

while 1 == 1:
    print ("blah")
