# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class car(vehicle):
#         def start(self):
#             print('car start with a key')
            
# class bike(vehicle):
#         def start(self):
#             print('bike start with a button')
                    
# car = car()
# bike = bike()

# car.start()
# bike.start()




#_______________________________________

def check_password(password):
    if len(password) <8:
        raise Exception("Error: password must be >=8 character")
    print('password is strong')
    
try:
    password = input('enter a password =')
    check_password(password)
except Exception as e:
    print(e)
        