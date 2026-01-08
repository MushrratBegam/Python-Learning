#QUE-1 create student class that takes name & marks of 3 subjects are argument in constructor. then create a method to print the average.
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is:",sum/3)
        
# s1 = student("tony stark", [99,98,97])
# s1.get_avg()            
 
 
 
 
 
            
# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
        
        
#     def start(self):
#         self.cluth = True
#         self.acc = True
        
#         print("car started..")
        
# car1 = car()
# car1.start() 



#QUE-2 create account class with 2 attributes-blance & account number.create methods for debit,credit and printing the balance
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
        
    def debit(self , amount):
        self.balance -= amount
        print("RS.",amount, "was debited")
        print("Total bslance=", self.get_balance())   
        
    def credit(self , amount):
        self.balance += amount
        print("RS-" , amount, "was credited")
        print("total balance", self.get_balance() )  
        
    def get_balance(self):
        return self.balance
    
    
acc1 = Account(10000, 1234)
acc1.debit(1000)
acc1.credit(500)  
acc1.credit(40000)                             