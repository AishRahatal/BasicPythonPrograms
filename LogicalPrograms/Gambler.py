'''	
@Author: Aishwarya
@Date: 2021-11-19
@Last Modified:2021-11-20 
@Title : Gambler Problem
'''
########################################################################################################
import math
import random

def gamble(stake,goal,no_of_times):
    """"
    Description: calculating and printing bets and wins of gamber till it reach the goal
    Parameter: stake,goals, no_of_times
    Return: none
    """
    try:
        bets = 0
        wins = 0
        loss=0
        for i in range(no_of_times):
            cash=stake
            while cash>0 and cash<goal:
            # Simulate one bet
                bets+=1
                if random.randrange(0,2)==0:
                    cash+=1
                else:
                    cash-=1
                if cash==goal:
                    wins+=1
                else:
                    loss+=1

        w=(wins/no_of_times)*100
        l=(loss/no_of_times)*100
        print('Total Wins =',wins)
        print('Total Loss =',loss)
        print('Average wins: ',w)
        print('Average loss: ',l)
    except:
        print("Somethimg went wrong")    



if __name__=='__main__':
 
    stake = int(input("Put the money  :"))
    goal = int(input("Enter goal of money that gambler wants to win  :"))
    no_of_times = int(input("Enter no of trials :"))
    #checking if all input values are more than 0
    if stake>0 and goal>0 and no_of_times>0:
        #call function 
        gamble(stake,goal,no_of_times)
    else :
        print("Please enter stake,goal and no_of_times more than 0")

