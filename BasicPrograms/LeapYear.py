'''	
@Author: Aishwarya
@Date: 2021-11-15 
@Title : Leap Year
'''
########################################################################################################
#importing Regex liabrary
import re
if __name__=='__main__':
  # Taking input from the user
  year=input("Enter year :")  
  #regex for positive number and has 4 digits
  pattern="^[1-9]{1}[0-9]{3}$"
  result=re.match(pattern,year)
  
  count=0
 # type casting year into integer for arithmetic operations
  year=int(year)
  #output
  if result:
        #checking if year is leap or not 
        if year % 4== 0 or year % 400==0:
        
            print(year," is a Leap year")
        else:
            print(year ," is not a Leap year")
  else    :
    print("Invalid year")

