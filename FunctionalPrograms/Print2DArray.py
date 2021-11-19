'''	
@Author: Aishwarya
@Date: 2021-11-17 
@Last: Modified: 2021-11-19 
@Title : Print 2D Array of different data types
'''
########################################################################################################
#importing Regex liabrary 
import re

def accept_integers(arr,m,n):
 """"
Description: entering integer values in rows and columns of 2D Array
Parameter: arr,m,n
Return: none
"""
# initialize the number of rows
 for i in range(0,m):
     arr+= [0]
# initialize the arr
 for i in range (0,m):
    arr[i] = [0]*n

 for i in range (0,m):
    for j in range (0,n):
     print ('entry in row: ',i+1,' column: ',j+1)
     arr[i][j] = int(input())

def accept_float(arr,m,n):
    """"
    Description: entering float values in rows and columns of 2D Array
    Parameter: arr,m,n
    Return: none
    """
    # initialize the number of rows
    for i in range(0,m):
        arr+=[0.0]
    # initialize the arr
    for i in range (0,m):
        arr[i] =[0.0]*n

    for i in range (0,m):
        for j in range (0,n):
         print ('entry in row: ',i+1,' column: ',j+1)
         arr[i][j]=float(input())
        
def accept_bool(arr,m,n):
    """"
    Description: entering bool values in rows and columns of 2D Array
    Parameter: arr,m,n
    Return: none
    """
    # initialize the number of rows
    for i in range(0,m):
        arr+=[None]
    # initialize the arr
    for i in range (0,m):
        arr[i] =[None]*n

    for i in range (0,m):
        for j in range (0,n):
         print ('entry in row: ',i+1,' column: ',j+1)
         arr[i][j] =bool(input())

def accept_string(arr,m,n) :
   """"
    Description: entering string values in rows and columns of 2D Array
    Parameter: arr,m,n
    Return: none
    """
    # initialize the number of rows
   for i in range(0,m):
        arr+=[None]
     # initialize the arr
   for i in range (0,m):
        arr[i] =[None]*n

   for i in range (0,m):
        for j in range (0,n):
         print ('entry in row: ',i+1,' column: ',j+1)
         arr[i][j] =input()
 

def display(arr,m,n):
    """"
    Description: printing different type of 2D Array
    Parameter: arr,m,n
    Return: none
    """
    print("Print 2D Array in matrix format:")
    for i in arr:
        print()   
        for j in i:
            print(j,end = " ")
            
     

if __name__=='__main__':
   # Taking input from the user
    row=input("Enter number of rows :")
    column=input("Enter number of columns :")
    #regex for integer number and maximum one digit 
    pattern= "^[1-9]{1}$"
    result1=re.match(pattern,column)
    result2=re.match(pattern,row)
    arr=[]
    if result1 and result2:  
        #type casting string into integer
        row=int(row)
        column=int(column) 
        #Choices
        print("------------------")
        print("Array with different data types:")
        print(  "1:'Integer Array'")
        print(  "2:'Float Array'")
        print(  "3:'Bool Array'")
        print(  "4:'String Array'")
        print("-------------------")
        ch=int(input("Enter Choice:"))
        if ch==1:
             #calling accepting Integer Array and printing function:
                accept_integers(arr,row,column)
                display(arr,row,column)
        elif ch==2:
            #calling accepting Float data type Array and printing function:
                accept_float(arr,row,column)
                display(arr,row,column)
        elif ch==3:
             #calling accepting Bool data type Array and printing function:
                accept_bool(arr,row,column)
                display(arr,row,column)
        elif ch==4:
             #calling accepting string data type Array and printing function:
                accept_string(arr,row,column)
                display(arr,row,column)
        else:print("Invalid Choice")
         
    else: print("Invalid Input")
        

          
   


