# class car:
#     color = "blue"
    
#     car1 = Car()
#     print(car1.color)
    
    
class items:
    restaurent_name = "The Bihari Dhaba"
    name = "aalukapratha"
    def __init__(self, fullname,price):
         self.items = fullname
         self.price = price
         print("adding new dish in database..")
         
    def delicius(self):
        print("delicius" ,self.name)
    def swadkatadka(self):
       print("swad-ka-tadka",self.name)  
    def get_price(self):
        return self.price  
     
    
         
s1 = items("aalukapratha",49)
print(s1.items , s1.price)
s1.delicius()
print(s1.get_price())

       
s2 = items("tamatarkichatni",35)
print(s2.items, s2.price)
s2.swadkatadka()

print(s2.restaurent_name)

       
        
        
        