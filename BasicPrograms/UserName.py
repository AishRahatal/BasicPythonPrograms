
'''	
@Author: Aishwarya
@Date: 2021-11-15 
@Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''
########################################################################################################
#importing Regex liabrary
import re
if __name__=='__main__':
    # Taking input from the user
    UserName= input("Enter your name :")
    #regex for validation only allowed string and minimum 3 characters
    pattern="(.*[A-Z]|[a-z]){3,}"
    result = re.match(pattern,UserName)
    # Output 
    if result :
     print("Hello  "+ UserName +", How are you?")
    else :
     print("Invalid Name")        