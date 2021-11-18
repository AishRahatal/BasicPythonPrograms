'''	
@Author: Aishwarya
@Date: 2021-11-15 
@Title : Print Harmonic Series
'''
########################################################################################################
#importing Regex liabrary and random liabrary
import re

if __name__=='__main__':
    # Taking input from the user
    number=input("Enter number to print harmonic series till a number:")
    #regex patter for accepting positive integer and maximum two digits 
    pattern="^[1-9]{1,2}$"
    result=re.match(pattern,number)
    #type casting number into integer value
    number=int(number)
    print("H(n)=",end=" ")
    if result:
      for i in range(1,number+1):
         print("1/",i,end="")
         if i != number:
            print(" + ",end="")    
    else :
        print("Please enter number grater than zero")