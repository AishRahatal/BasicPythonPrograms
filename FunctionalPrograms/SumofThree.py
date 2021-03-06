'''	
@Author: Aishwarya
@Date: 2021-11-18 
@Last: Modified: 2021-11-19
@Title : Sum of three Integer adds to ZERO
'''
########################################################################################################
#importing Regex liabrary and flag liabrary
from enum import Flag
import re
#function for trplet
def find_triplets(arr, n):
    """"
    Description: Brute Force approach to find distinct integer triplets which adds to zero
    Parameter: arr,n
    Return: none
    """
    Flag=False

    for i in range(0 , n-2):
      for j in range(i+1,n-1):
        for k in range(j + 1, n):
          if arr[i] + arr[j] +arr[k] == 0:
              print("There are Triplets !!")
              print(arr[i], "  ", arr[j] ," ",arr[k] , sep = " ") 
              print("------------------------------------")
              Flag=True
          else:
               Flag=False
               break
              
    if False:
        print("Tripletes not present in array")      
   
if __name__=='__main__':
   # Taking input from the user
    n=input("Enter number of elements in array :")
    #regex for integer number and maximum one digit 
    pattern= "^[1-9]{1}$"
    result=re.match(pattern,n)
    a=[]
    if result:
        n=int(n)
        # initialize the number of rows
        for i in range(0,n):
         a+= [0]
        print ("Enter elements in array: ")
        for i in range(n):
            print ("Enter",i+1," element: ")
            a[i]=int(input())
        print("-----------------------")   
        print ("Elements in array: ")
        for i in a:
         print(i)
          
        print("-----------------------")  
        find_triplets(a,n)
    else:print("Invalid Input")