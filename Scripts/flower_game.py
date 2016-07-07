import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'They love you'
    elif answerNumber == 2:
        return 'They do not love you'
r = random.randint(1, 2)
status = getAnswer(r)
print ("Enter the name below")
question = input("Does ____ love me:    ")
print(status)


# def multiply(a, b):
#   a * b
# c= 5
# d= 10
# product = multiply(c, d)
# print (product)
