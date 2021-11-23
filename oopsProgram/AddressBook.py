'''	
@Author: Aishwarya
@Date: 2021-11-21
@Last MOdified:2021-11-22
@Title : Address Book
'''
########################################################################################################

import re

class AddressBook:
    def __init__(self,book):
     """"
    Description: It is counstructor 
    Parameter: self,book
    Return: none
    """
     self.book=book    
        
    def accept(self,book):
        """"
        Description: accepting input from  user and storing into dictionary
        Parameter: self,book
        Return: none
        """
        n=input("Enter  of person's contact to be add :")
        #regex patter for accepting positive integer and maximum one digit 
        pattern="^[1-9]{1}$"
        result=re.match(pattern,n)
        #type casting number into integer value
        n=int(n)
        if result:
            for i in range(n):
                name = input("Name: ")
                #regex for validation only allowed string and minimum 8 characters and max 20
                pattern1="(.*[A-Z]|[a-z]){8,20}"
                regexname = re.match(pattern1,name)
                phone = input("Phone No.: ")
                #regex for phone numbers for all countries with country code and pattern
                phone_pattern="((?:\+|00)[17](?: |\-)?|(?:\+|00)[1-9]\d{0,2}(?: |\-)?|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))"
                regexphone = re.match(phone_pattern,phone)
                email = input("E-mail Address: ")
                email_pattern = "^[a-zA-Z0-9]+([.#_$+-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+[.][a-zA-Z]{2,3}([.][a-zA-Z]{2})?$"
                regexemail = re.match(email_pattern,email)
                city= input("City :")
                regexcity=re.match(pattern1,city)
                state= input("State :")
                regexstate=re.match(pattern1,state)
                zip= input("zip :")
                #regex for zip code  for all countries range
                pattern_zip= "^[1-9]{4,7}$"
                regexzip=re.match(pattern_zip,zip)
                print("------------------------------------------------")
                if not regexname:
                    print("Please enter correct name")
                    if not regexphone:
                        print("Please enter correct phone")
                        if not regexemail:
                            print("Please enter correct email")
                            if not regexcity:
                                 print("Please enter correct city name")
                                 if not regexstate:
                                    print("Please enter correct state name")
                                    if not regexzip:
                                        print("Please enter correct zip code")
                else:
                    book[name]=phone,email,city,state,zip
        else :
            print("Please enter number grater than zero")

    def print_book(self,book):
        """"
        Description: printing records which are stored in dictionary
        Parameter: self,book
        Return: none
        """
        count=len(book)
        if count>0:
            print("Contacts in Address book = ", count)
            print("---Address BOOK-----")
            print(book)
            print("--------------------------")
        else:
            print("There no contact in Address book")
   
    def search(self,book):
        """"
        Description: search a record in dictionary
        Parameter: self,book
        Return: none
        """
        try:
            search_name = input("Enter Name you want to search: ")
            #regex for validation only allowed string and minimum 8 characters and max 20
            pattern1="(.*[A-Z]|[a-z]){3,20}"
            validate = re.match(pattern1,search_name)
            if validate:
                key = search_name
                if key in book:
                    print("Found the record!!",search_name)
                    print("--------------------------")
                    print(book)
                else:
                    print("Not found the record!!")
            else:
                print("Please enter correct name")
        except:print("There is an error...")

    def delete(self,book):
        """"
        Description: delete a record from  dictionary 
        Parameter: self,book
        Return: none
        """
        try:
            print("Enter the  name to delete record:")
            name1 = input("enter the name")
            #regex for validation only allowed string and minimum 8 characters and max 20
            pattern1="(.*[A-Z]|[a-z]){3,20}"
            validate = re.match(pattern1,name1)
            if validate:
                r=book.pop(name1,"Not found the record")
                if r =="not":
                    print(r)
                else:
                    print("Deleted the record successfully")
                    print("---Updated Address BOOK-----")
                    print(book)
            else:
                print("Please enter correct name")
        except: print("There is an error...")
    
    def edit(self,book):
        """"
        Description: editing record which are stored in dictionary
        Parameter: self,book
        Return: none
        """
        dict={}
        print("Enter the contact name to update")
        update_name = input("Enter the name: ")
        key = update_name
        pattern1="(.*[A-Z]|[a-z]){8,20}"
        validate = re.match(pattern1,update_name)
        if validate:
            try:
                newnumber=int(input("Enter  new phone number: "))
                newemail=input("Enter  new email address: ")
                newcity= input("Enter new city :")
                newstate= input("Enter new state :")
                newzip= int(input("Enter new zip :"))
                dict[update_name]=newnumber,newemail,newcity,newstate,newzip
                if key in book:
                    book.update(dict)
                    print("Updated the record successfully!!")
                    print("---Updated Address BOOK-----")
                    print(book)
                else:
                    print("Record not found...")
            except  Exception as e:
                print("There is an error",e)        
        else:
            print("Please enter correct name")    


if __name__ == "__main__":
    book={}
    obj=AddressBook(book)
    choice =1
    while choice !=0:
        print("---------Menu------------")
        print("1.Accept record in AddressBook")
        print("2.Print record of AddressBook") 
        print("3.Delete record of  AddressBook")
        print("4.Search record in AddressBook") 
        print("5.Update record in AddressBook ")
        print("0.Exit")
        print("-------------------------")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1: 
                obj.accept(book)
            elif choice ==2: 
                obj.print_book(book)
            elif choice ==3:      
                obj.delete(book)
            elif choice ==4: 
                obj.search(book)
            elif choice ==5: 
                obj.edit(book)
            else:
                print("Exiting....")
        except:
            print("Entered wrong value")

