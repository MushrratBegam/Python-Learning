# class student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
        
        
        
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) /3) + "%"
    
    
# stu1 = student(98,97,99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage) 




#---complex number---
# class complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
        
        
#     def showNumber(self):
#         print(self.real, "i+", self.img, "j")
        
#     def __add__(self , num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return complex(newReal , newImg)
    
# num1 = complex(1,3)
# num1.showNumber()

# num2 = complex(4,6)
# num2.showNumber()

# num3 = num1.__add__(num2)
# num3.showNumber()








#QUE-1 define a circle class to create a circle with radius r using the constructor. define an area() method of the class which calculates the area of the cirlce. define a perimeter() mrthod of the calss which allows you to calculate the perimeter of the circle.
# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius
    
# c1 = circle(21)
# print(c1.area())
# print(c1.perimeter())      





#QUE-2 Define a employe claas with attributes role, department and sallary. this class also has a showDetails() method. create an engineer class that inherits properties from employee and has additional attributes : name & age.
# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
        
#     def showDetails(self):
#         print("role=", self.role)
#         print("dept=", self.dept)
#         print("salary=", self.salary)
        
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "60000")
        
# engg1 = Engineer("Elon musk", 45)
# engg1.showDetails()






#QUE-3 create a class called order which store items and its price.use Dunder function __gt__() to concey that: order1 > order2 if price of order1 > price of order2
class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        
    def __gt__(self, ord2):
        return self.price > ord2.price
    
ord1 = order("chips", 20)
ord2 = order("tea", 15)

print(ord1 > ord2)        
                    
         

            



       