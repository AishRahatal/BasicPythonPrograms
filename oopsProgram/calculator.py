
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def addition(self):
        print("Addition =",self.a+self.b)

    def subtraction(self):
        print("Subtraction =",self.a-self.b)

    def multiplication(self):
        print("Multiplication =",self.a*self.b)

    def division(self):
        print("Division =",self.a/self.b)

if __name__ == '__main__': 
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    obj=calculator(a,b)
    choice=1
    try:
        while choice != 0:
            print("---------------")
            print("1. ADDITION")
            print("2. SUBTRACTION")
            print("3. MULTIPLICATION")
            print("4. DIVISION")
            print("---------------")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                obj.addition()
            elif choice == 2:
                obj.subtraction()
            elif choice == 3:
                obj.multiplication()
            elif choice == 4:
                obj.division()
            else:
                print("Invalid choice")
    except:print("Entered wrong ..please try again")
        
