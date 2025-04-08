from time import *
import random as rm

def mistakes(par,usertest):
    par = par.strip()
    usertest = usertest.strip()
    mistakes=0
    
    for i in range(len(par)):
        try:
            
            if par[i] != usertest[i]:
                mistakes=mistakes+1
            
            
        except IndexError:
            mistakes=mistakes+1
    return mistakes
    # else:
    #     print('Congratulations! You got all the characters right.')
        
def timespeed(beforetime,aftertime,testinput):
    timetaken=aftertime-beforetime
    timerounnd=round(timetaken,3)
    speed=len(testinput)/timerounnd
    return round(speed,3)



    return wrapper

def score(speed,mistakes):
    base_score = speed *10
    pen=mistakes * 2
    final_score=base_score-pen
    final_score1=final_score
    if final_score1 > 75:
        return (f"Excellent! Your score is {round(final_score,4)}")
    elif final_score1 > 50:
        return (f"Good! Your score is {round(final_score,4)}")
    elif final_score1 > 25:
        return (f"Average! Your score is {round(final_score,4)}")
    elif final_score1 < 25 and final_score > 0:
        return (f" Below Average! Your score is {round(final_score,4)}")
    elif final_score1 <0:
        return (f"practice more on typing! Your score is {round(final_score,4)}")
   
    return round(final_score,3) 
    
    
    
    


type=["Excellence is not a skill, it's an attitude.",
      " It can be used to control the behavior",
      " of the player and the game logic and the ",
        "game world.",
        " It can be used to make the game more enjoyable",
        " and less frustrating.",
        " It can be used to make the game more challenging",
        " and more exciting.",
        " It can be used to make the game more fun and",
        " more engaging.",
        " It can be used to make the game more predictable",
        " and more predictable."]

type1=rm.choice(type)
print('---typing Test----')
print(type1)
print()
print()

beforetime=time()

testinput=input(" Enter: ")

aftertime=time()

print(f'Time taken: {aftertime-beforetime} seconds')

print()

speed=timespeed(beforetime,aftertime,testinput)

mistakes_count = mistakes(type1,testinput)

score=score(speed,mistakes_count)
print("Speed:" ,timespeed(beforetime,aftertime,testinput),"W/Sec")
print("Mistakes: " ,mistakes(type1,testinput))
print(f"Score:{score}")
# print(len(testinput))
