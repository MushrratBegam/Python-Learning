# from datetime import datetime

# date = datetime(2025, month=12, day=20, hour=19, minute=15, second=53)

# print(date)


# #Getting a specific property

# print(f"Year: {date.year}")
# print(f"Month: {date.month}")
# print(f"Hour: {date.hour}")
# print(f"Minute: {date.minute}")
# print(f"Second: {date.second}")


# print(date.now())
# print(date.day)
# print(date.month)



# __init__ is a constructor which allow us to create variable in class.
class person:
    def __init__(self):
        self.name = "mushrrat"
        self.age = 22
        self.location = "india"
    
    def talk(self):
        print("Hey, my name is muhrrat")
        
        
        
#Instance/object

mushrrat = person()
mushrrat.talk()        