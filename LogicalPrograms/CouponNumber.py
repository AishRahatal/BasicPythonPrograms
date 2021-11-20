'''	
@Author: Aishwarya
@Date: 2021-11-18
@Last Modified:2021-11-20
@Title : Generate coupon numbers
'''
########################################################################################################
import random
import re

def generate_coupon(count,length):
   """"
   Description: generating different type of combinations of string
   Parameter: count,length
   Return: none
   """
   count=int(count)
   length=int(length)
   codepattern= "ABCDEFGHIJKLMNOPQRST1234567890#"
   try:
      print("Coupon Numbers :")
      for i in range(count):
         code = ""
         for j in range(length):
      #choice() will select random character from string codepattern
            code += random.choice(codepattern)
         print(code)
   except:
      print("Somethimg went wrong")
 
if __name__ == '__main__':
   
   codeCount=int(input("Enter number of coupons to be generated :"))
   codelength=int(input("Enter length of the coupon number:"))
   if codeCount>0 and codelength>0:
      generate_coupon(codeCount,codelength)
   else:
      print("Please eneter valid numbers")
   