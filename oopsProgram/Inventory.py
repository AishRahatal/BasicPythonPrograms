'''	
@Author: Aishwarya
@Date: 2021-11-21
@Last MOdified:2021-11-22
@Title : Address Book
'''
########################################################################################################
import json
import os

class Innventory:

    def __init__(self,stock):
        """"
        Description: It is counstructor wich point instance of class
        Parameter: self,stock
        Return: none
        """
        self.stock=stock  

    def printstock(self):
        """"
        Description: printing records using json object which are stored in  json file
        Parameter: none
        Return: none
        """ 
       
        with open('sample.json', 'r') as f:
            jsonData = json.load(f)
            print("Type of JSON Object: ", type(jsonData))
            
        # Traversing the json file
        for id in jsonData:
            print("Id :",id)
            print("Product: ", jsonData[id]["name"])
            print("Price: ", jsonData[id]["price"])
            print("Category: ", jsonData[id]["category"])
            print("Quantity: ", jsonData[id]["quantity"])
            print()

    def addtostock(self,stock):
        """"
        Description: adding product details from  user and storing into  stock and writing to json file
        Parameter: self,stock
        Return: id, stock
        """ 
        temp={}
        try:
            id=int(input("Enter product id"))
            temp['name'] = input("Product:")
            temp['price'] = int(input("Price:"))
            temp['category'] =input("Category: ")
            temp['quantity']= int(input("Quantity :"))
            print(temp)
            return(id,temp)
        except Exception as e:
            print("Error...",e)

    def delete(self,stock):
        """"
        Description: delete a record from  stockionary  and json file
        Parameter: self,stock
        Return: none
        """
        try:
            did=int(input("Enter product id to delete"))
            r=stock.pop(did,"Not found the record")
            if r =="not":
                print(r)
            else:
                print("Deleted the record successfully")
                print("---Updated Stock-----")
                print(stock)
            with open('sample.json','w') as f:
                json.dump(stock, f, indent=2)
                print("Deleted from json Successfully!!")  
            f.close()    
        except: print("There is an error...")

    def search(self):
         
        keyVal = input("Enter  id to search product: ")

        # load the json data
        with open('sample.json' ,'r') as f:
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

    def edit(self,stock):
        """"
        Description: editing record which are stored in stockionary and in json file
        Parameter: self,stock
        Return: none
        """ 
        temp={}
        try:
            
            print("Enter the contact product id to edit")
            eid = input("Enter the product id: ")
            key = eid
        
            p=input("Product:")
            pr=int(input("Price:"))
            c= input("Category: ")
            q= int(input("Quantity :"))
            temp[eid]=p,pr,c,q
            with open('sample.json' ,'r') as f:
                data = json.load(f)  
            if key in data:
                stock.update(temp)
                print("Updated the record successfully!!")
                print("---Updated stock-----")
                print(temp)
                with open('sample.json','w') as f:
                    json.dump(stock, f, indent=2)
                    print("Edited in json Successfully!!") 
                f.close()     
            else:
                print("Record not found...")
        except  Exception as e:
            print("There is an error",e)   
                
            
       

if __name__ == "__main__":
    stock={}
    p=Innventory(stock)
    choice =1
    while choice !=0:
        print("---------Menu------------")
        print("1.Add a product to stock")
        print("2.Print stock") 
        print("3.Edit product details")
        print("4.Delete product from stock ")
        print("5.Search product in stock ")
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
                        id, d = p.addtostock(stock)
                        stock[id] = d
                        with open('sample.json','w') as f:
                            json.dump(stock, f, indent=2)
                            print("Added record successfully to json file")
                            print("-------------------------------")
                            f.close()
            elif choice ==2: 
                 p.printstock()
                 print("-------------------------------")
            elif choice ==3:      
                 p.edit(stock)
                 print("-------------------------------")
            elif choice ==4: 
                p.delete(stock)
            elif choice ==5:
                p.search()
            else:
                print("Exiting....")
        except:
            print("Entered wrong value")





    
    

            
            
            

    
                   
      
    


   
   
    
    