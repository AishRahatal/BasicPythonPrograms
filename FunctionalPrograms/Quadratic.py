'''	
@Author: Aishwarya
@Date: 2021-11-18 
@Last: Modified: 2021-11-19
@Title : a program to find the roots of the equation a*x*x + b*x + c.
'''
########################################################################################################
#importing Regex liabrary 
import re
import math

def get_root(a,b,c):

    delta=b*b-4*a*c
    #condition for real and different roots and sqrt() for getting squareroot
    if delta > 0 :
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("root1 = ", round(root1,2),"and root2 =", round(root2,2))
    #condition for real and equal roots
    elif delta == 0 :
        root1 = root2 = -b/(2 * a)
        print("root1 = root2 = ",root1)

    # if roots are not real and round() allowing at least 2 two digits after decimal
    else :
        realNumber = -b / (2 * a)
        imagNumber= math.sqrt(-delta) / (2 * a)
        print("root1 =   ",round(realNumber,2)," , ",round(imagNumber,2),"i")
        print("root2 =   ",round(realNumber,2)," , ",round(imagNumber,2),"i")
   

if __name__=='__main__':
    # Taking input from the user
    a=float(input("Enter value for a :"))
    b=float(input("Enter value for b :"))
    c=float(input("Enter value for c :"))
    
    if a>0 and b>0 and c>0:
        #calling function
       get_root(a,b,c)
    else:
        print("Invalid Input")