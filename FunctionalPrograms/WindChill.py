'''	
@Author: Aishwarya
@Date: 2021-11-18
@Last: Modified: 2021-11-19 
@Title : A program that takes two double command-line arguments t and v and prints the wind chill.
'''
########################################################################################################
#importing Regex liabrary 
import re
import math

def wind_chill(t,v):
    """"
    Description: Mathmatical operation 
    Parameter: t,v
    Return: none
    """
    t=float(t) # string input casting into float
    v=float(v)
    t=abs(t) #for absolute value
    W=35.74 + 0.6215*t +(0.4275*t-35.75)*pow(v,0.16)
    print("Wind Chill = ",W)

if __name__=='__main__':
   # Taking input from the user
    print()
    t = input("Enter Temprature :")
    v = input("Enter Speed of wind :")
   
    #regex for t is not larger than 50 in absolute value 
    pattern1="^(?:-[0-4][0-9]|-50|[1-4][0-9]|50)$"
    #regex for v is larger than 120 or less than 3
    pattern2="^(12[0]|1[01][0-9]|[1-9]?[3-9])$"
    result1=re.match(pattern1,t)
    result2=re.match(pattern2,v)
    if result1 and result2:
         #calling function
        wind_chill(t,v)
    else:
        print("Invalid Input")
