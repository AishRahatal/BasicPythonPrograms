'''	
@Author: Aishwarya
@Date: 2021-11-15 
@Title : Factors of number
'''
########################################################################################################
#importing Regex liabrary
import re
if __name__=='__main__':
# Taking input from the user
   n=input("Enter Number :")
   #regex for positive number and maximum two digit
   pattern= "^[1-9]{1,2}$"
   result=re.match(pattern,n)
   #type casting string into integer
   n=int(n)
   print("Prime factors of ",n ,":")
   i = 2
   while i<=n:
        if n%i == 0:
            print(i) #printing factors
            n=n//i
        else:
            i += 1



