'''	
@Author: Aishwarya
@Date: 2021-11-18 
@Last: Modified: 2021-11-19
@Title : Write program for Euclidean distance from the point (x, y) to the origin (0, 0)
'''
########################################################################################################
#importing Regex liabrary 
import re
import math

def get_distance(x,y):
   #calculating distance from origin point O(0,0) an A(x,y)
    distance = math.sqrt(pow(x,2) + pow(y,2))
    #used trunc() for trimming decimal after decimal point
    print("Euclidean distance of given points O(0,0) an A(x,y) =", math.trunc(distance))


if __name__=='__main__':
# Taking input from the user
    print("Enter the first point A")
    x = input("Enter value of x coordinate =")
    y = input("Enter value of x coordinate =")
    print("The Origin point O(0,0) ")
    #regex for integer number and maximum two digit 
    pattern= "^[0-9]|-[0-9]{1,2}$"
    result1=re.match(pattern,x)
    result2=re.match(pattern,y)
    if result1 and result2:
        x=int(x)
        y=int(y)
        get_distance(x,y)  
    else:
        print("Invalid Input")
    