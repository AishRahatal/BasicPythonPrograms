import re
import json

class AddressBook:
    def __init__(self,dict):
        """"
        Description: It is counstructor wich point instance of class
        Parameter: self,dict
        Return: none
        """
        self.dict=dict    
        
    def accept(self,dict):
        """"
        Description: accepting input from  user and storing into dictionary and writing to json file
        Parameter: self,book
        Return: name,dict
        """ 
        dict =  {}
        name = input("Name: ")
        #regex for validation only allowed string and minimum 8 characters and max 20
        pattern1="(.*[A-Z]|[a-z]){3,20}"
        regexname = re.match(pattern1,name)
        dict['phone'] = input("Phone:")
        #regex for phone numbers for all countries with country code and pattern
        phone_pattern="((?:\+|00)[17](?: |\-)?|(?:\+|00)[1-9]\d{0,2}(?: |\-)?|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))"
        regexphone = re.match(phone_pattern,dict['phone'])
        dict['email'] = input("E-mail Address: ")
        email_pattern = "^[a-zA-Z0-9]+([.#_$+-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+[.][a-zA-Z]{2,3}([.][a-zA-Z]{2})?$"
        regexemail = re.match(email_pattern,dict['email'] )
        dict['city']= input("City :")
        regexcity=re.match(pattern1,dict['city'])
        dict['state']= input("State :")
        regexstate=re.match(pattern1, dict['state'])
        dict['zip']= input("zip :")
        #regex for zip code  for all countries range
        pattern_zip= "^[1-9]{4,7}$"
        regexzip=re.match(pattern_zip,dict['zip'])
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
            return(name,dict)

    def print_fromjson(self):
        """"
        Description: printing records which are stored in dictionary and json file
        Parameter: self,book
        Return: none
        """      
    # We can straight away open the json file in 'read' mode, 
        print("Printing records from json file")
        with open("book.json","r") as file:
            jsonData = json.load(file)
    
        print("Type of JSON Object: ", type(jsonData))
    
        # Traversing the json file
        for name in jsonData:
            print("Name: ", name)
            print("Email-Address: ", jsonData[name]["phone"])
            print("Email-Address: ", jsonData[name]["email"])
            print("City: ", jsonData[name]["city"])
            print("State:",jsonData[name]["state"])
            print("Zip: ", jsonData[name]["zip"])
            print()
        file.close() 

    def edit(self,dict):
        """"
        Description: editing record which are stored in dictionary and in json file
        Parameter: self,dict
        Return: none
        """
        temp={}
        print("Enter the contact name to edit")
        update_name = input("Enter the name: ")
        key = update_name
        pattern1="(.*[A-Z]|[a-z]){3,20}"
        validate = re.match(pattern1,update_name)
        if validate:
            try:
                newnumber=int(input("Enter  new phone number: "))
                newemail=input("Enter  new email address: ")
                newcity= input("Enter new city :")
                newstate= input("Enter new state :")
                newzip= int(input("Enter new zip :"))
                temp[update_name]=newnumber,newemail,newcity,newstate,newzip
                if key in dict:
                    dict.update(temp)
                    print("Updated the record successfully!!")
                    print("---Updated Address BOOK-----")
                    print(temp)
                    with open('book.json','w') as f:
                        json.dump(dict, f, indent=2)
                        print("Edited in json Successfully!!") 
                    f.close()     
                else:
                    print("Record not found...")
            except  Exception as e:
                print("There is an error",e)        
        else:
            print("Please enter correct name")
      
    def delete(self,dict):
        """"
        Description: delete a record from  dictionary  and json file
        Parameter: self,book
        Return: none
        """
        try:
            print("Enter the  name to delete record:")
            name1 = input("Enter the name : ")
            #regex for validation only allowed string and minimum 8 characters and max 20
            pattern1="(.*[A-Z]|[a-z]){3,20}"
            validate = re.match(pattern1,name1)
            if validate:
                r=dict.pop(name1,"Not found the record")
                if r =="not":
                    print(r)
                else:
                    print("Deleted the record successfully")
                    print("---Updated Address BOOK-----")
                    print(dict)
                with open('book.json','w') as f:
                    json.dump(dict, f, indent=2)
                    print("Deleted from json Successfully!!")  
                f.close()      
            else:
                print("Please enter correct name")
        except: print("There is an error...")

    def search(self):
        """"
        Description: Search a record from  dictionary  and json file
        Parameter: self
        Return: none
        """
         
        keyVal = input("Enter a key value: ")

        # load the json data
        with open('book.json' ,'r') as f:
            data = json.load(f)        
                # Search the key value using 'in' operator
        if keyVal in data:
            # Print the success message and the value of the key
            print("  found in JSON data" ,keyVal)
            print("The value of", keyVal,"is", data[keyVal])
        else:
            # Print the message if the value does not exist
            print(" is not found in JSON data" ,keyVal)
        f.close()
    
        

if __name__ == "__main__":
    dict = {}
    obj=AddressBook(dict)
    choice =1
    while choice !=0:
        print("---------Menu------------")
        print("1.Accept record in AddressBook")
        print("2.Print record of AddressBook") 
        print("3.Edit record of  AddressBook")
        print("4.Delete record in AddressBook ")
        print("5.Search record in AddressBook ")
        print("0.Exit")
        print("-------------------------")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1: 
                while True:
                        exit = input('Do you want to add another input (y/n)? ')
                        if exit.lower() == 'n':
                            break
                        else:
                            name, d =obj.accept(dict)
                            dict[name] = d
                            with open('book.json','w') as f:
                                json.dump(dict, f, indent=2)
                            print("Added record successfully to json file")
                            print("-------------------------------")
                            f.close()
            elif choice ==2: 
                obj.print_fromjson()
                print("-------------------------------")
            elif choice ==3:      
               obj.edit(dict)
               print("-------------------------------")
            elif choice ==4: 
                obj.delete(dict)
            elif choice ==5:
                obj.search()
            else:
                print("Exiting....")
        except:
            print("Entered wrong value")

    

    
    
    

   
        
   
            
        
      