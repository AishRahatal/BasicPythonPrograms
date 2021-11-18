'''	
@Author: Aishwarya
@Date: 2021-11-15 
@Title : Flip Coin and print percentage of Heads and Tails
'''
########################################################################################################
#importing Regex liabrary and random liabrary
import random
import re
def Flip(num):
    """""
    Description:
    Use of Random Function to get value between 0 and 1
    print Percentage of Head vs Tails

    Parameter:
    num
    Return:
    none
    """
    head=0 # for head count
    tail=0 # for tail count
    #iterating until input number
    for i in range(num): 
        #using random() inbuilt function for getting value 0 and 1
        coinside=random.randint(0,1)
        #if coinside is 1 then it is head
        if coinside == 1:
            print("\n Heads !!")
            #increment head count
            head=head+1
            #incrementing  count of flipping coin
            i=i+1
        #if coinside is 0 then it is tails
        elif coinside == 0:
            print("\n Tails !!")
            #incrementing  tail count
            tail=tail+1 
            #incrementing  count of flipping coin
            i=i+1

 # Output 
 #printing total number of heads and tails occured
    print("\n----------------------")
    print("Total Heads :",head)
    print("Total Tails :",tail)
    print("Total flip count :",i)
    print("\n----------------------")
    #calculating percentage of heads 
    print("Percentage :")
    percent_head=(head/num)*100
    print("Percentage of head : ",percent_head)
    #calculating percentage of tails 
    percent_tail=(tail/num)*100
    print("Percentage of head : ",percent_tail)


if __name__=='__main__':
    # Taking input from the user
    number=input("Enter how many number of time want to flip a coin :")
    #regex patter for accepting positive integer and maximum two digits 
    pattern="^[1-9]{1,2}$"
    result=re.match(pattern,number)
    #type casting number into integer value
    number=int(number)
    if result:
     #calling function with parameter
     Flip(number)
    else :
        print("Please enter number grater than zero")