#setup

import random

fish = {
    'bass' : [2,5], 
    'king_crabs' : [2,3], 
    'pike' : [2,2],
    'guppy': [10,1], 
    'marlin': [5,4], 
    'salmon': [4, 9]
    }
casts_left = 10
points = 0
#cast function
def cast():
    global casts_left
    if casts_left == 0:
        print ("Sorry! Your game is over!")
        return
    if casts_left > 0:
        catch = [random.choice(i) for i in fish.values()]
        #catch = random.choice(fish.keys())
        print (catch)
        '''points += catch[2]
        print 
        casts_left -= 1      
        print (casts_left)'''         
        return

#for x in range(11):
cast()
        