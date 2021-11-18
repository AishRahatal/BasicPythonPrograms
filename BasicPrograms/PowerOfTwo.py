'''	
@Author: Aishwarya
@Date: 2021-11-15 
@Title : Power of 2
'''
########################################################################################################
"""
Description:
 This program takes a command-line argument N and prints a table of the
 powers of 2 that are less than or equal to 2^N.
 The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int

Parameter:
none

Return:
none

"""
########################################################################################################
#importing Regex liabrary
import re
if __name__=='__main__':
    # Taking input from the user
    number=input("Enter Number :")
     #Regex for  number is positive and less than 32 
    pattern="^([0]|3[01]|[12][0-9]|[1-9])$"
    result=re.match(pattern,number)
   
    number=int(number)
    if result:
        #using inbuilt math function pow()
        power=pow(2,number) #  can be modified with #

        print(number," to power of 2 = ",power)
    else:
        print("Invalid number")