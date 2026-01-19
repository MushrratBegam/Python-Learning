# 1. check whether a number  is divisible by 5 and 11.

num = int(input("Enter a number :"))

if num % 5 ==0 and num % 11 == 0 :
    print("Divisible by 5 and 11")
else:
    print("Not Divisible")



# 2. check if a person is eligible for loan.(.age >= 21, . salary >= 25000, . credit score >= 700)
age = int(input("Enter your age :"))
salary = float(input("Enter your salary :"))
credit_score = float(input("Enter your credit score :"))

if age >= 21 and salary >= 25000 and credit_score >= 700:
    print("Eligible")
else:
    print("Not Eligible")


# 3. validate login using username AND password.

username = input("Enter username :")
password = input("Enter password :")

if username == "admin123.com" and password == "admin123":
    print("login successfully",)
else:
    print("Invalid username and password")


# 4. check student pass condition.(all subject >= 40, Average >= 50)

math = int(input("Enter your marks :"))
science = int(input("Enter your marks :"))
English = int(input("Enter your marks :"))
if math >= 40 and science >= 40 and English >= 40 :
    print("Pass")
else:
    print("fail")


# 5. check if a number lies between 10 and 100.

num = int(input("Enter a number (10-100):"))

if num >= 10 and num <= 100:
    print("valid number")
else:
    print("invalid number")


# 6. check exam eligibility.(.attendence >= 75, or medical certificate available)

attendence = int(input("Enter attendence percentage :"))

if attendence >= 75 or "medical certificate available":
    print("Eligible")
else:
    print("Not eligible")
    





