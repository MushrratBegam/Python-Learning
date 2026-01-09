# 1. Write a python program to check if a number is positive

num = int(input("Enter a number :"))

if num > 0:
    print("Number is positive")
else:
    print("number is negative")
    


# 2. print "Eligible to vote" if age is 18 or above

age = int(input("Enter age :"))

if age >= 18:
    print("Eligible to vote")
else:
    print("not Eligible to vote")
    
    
# 3. check if a number is divisible by 7

num = int(input("Enter a number :"))

if num % 7 == 0:
    print("divisible number")
else:
    print("not divisible number")



# 4. print "pass" if mark are greater than 40

mark = int(input("Enter marks :"))

if mark >= 40:
    print("pass")
else:
    print("fail")
    
    
    
# 5. Check if a number is greater than 100

num = int(input("Enter number :"))
if num > 100:
    print("number is greater")
else:
    print("number is smaller")



# 6. Display a massege if temperature  exceeds 45 degree Celcius
Temp = int(input("Enter temperature exceeds :"))

if Temp > 45:
    print("temperature exceeds")
else:
    print("temperature not exceeds")





# 7. check if a string length is more than 8 character.

string_len = len(input("Enter character :"))

if string_len > 8 :
    print("congratulations")
else:
    print("please Enter your string more than 8 character") 




# 8. print "Logged in" if password matches "admin123"

password = (input("Enter your password :"))

if password == "admin123":
    print("logged in")
else:
    print("please...Enter correct password")




# 9. Check if a number is multiple of 10.

num = int(input("Enter number :"))

if num % 10 == 0:
    print("Number is correct")
else:
    print("Number is incorrect")



# 10. print a warning if balance is below minimum limit.
Total_amount = 50000
Balance = int(input("Enter amount :"))

if Balance > Total_amount:
    print(f"{Total_amount}")
else:
    print("Warning!!! your Balance is below the minimum limit ")
    


    
    
    
    