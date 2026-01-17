# 1. print day name using day number (1-7).
Day = int(input("Enter day number(1-7) :"))
if Day == 1:
    print("Monday")
elif Day == 2:
    print("Tuesday")
elif Day == 3:
    print("wednesday")
elif Day == 4:
    print("Thursday")
elif Day == 5:
    print("Friday")
elif Day == 6:
    print("Saturday")
elif Day == 7:
    print("Sunday")
else:
    print("Not a valid Day")



# 2. print month name using month number.

month = int(input("Enter month number(1-12) :"))

if month == 1:
    print("January")
elif month == 2:
    print("Febuary")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("invalid month")


# 3. display grade based on percentage.

percentage = int(input("Enter percentage :"))

if percentage >= 75:
    print("Grade A")
elif percentage >= 60:
    print("Grade B")
elif percentage >= 40:
    print("Grade C")
else:
    print("fail")    


# 4. Display bonous percentage based on experience year.

Experience = int(input("Enter Experience year(15-20) :"))

if Experience == 15:
    print("bonous = 5%")
elif Experience == 16:
    print("Bonous = 6%")
elif Experience == 17:
    print("Bonous = 7%")
elif Experience == 18:
    print("Bonous = 8%")
elif Experience == 19:
    print("Bonous = 9%")
elif Experience == 20:
    print("Bonous 10%")
else:
    print("Invalid Experience")



# 5. Identify traffic signal meaning.

signal = int(input("Enter signal colour(Red =1,Yellow =2,Green =3) :"))
if signal == 1:
    print("print stop")
elif signal == 2:
    print("Ready to stop")
elif signal == 3:
    print("Go")
else:
    print("Ivalid signal meaning")




# 6. Catogories temperature as Cold / warm / Hot.

Temp = int(input("Enter temperature :"))

if Temp >= 0 and Temp <= 15:
    print("cold")
elif Temp >= 16 and Temp<= 30:
     print("warm")
elif Temp > 30:
    print("hot")
else:
    print("Invalid temperature")


# 7. Catogories employee based on salary range.

range = int(input("Enter employee catagory :"))

if range >= 75000 and range <= 100000:
    print("Catagory A")
elif range >=50000 and range < 75000:
    print("Catagory B")
elif range < 500000:
    print("Catagory C")
else:
    print("Invalid catagory") 




# 8. print discount percentage based on purchage ammount.

amount = float(input("Enter purchage amount :"))

if amount >= 5000:
    discount = 20
    print("discount percentage",discount,"%")
elif amount >= 3000:
    discount = 15
    print("discount percentage",discount,"%")
    
elif amount >= 1000:
    discount = 10
    print("discount percentage",discount,"%") 
else:
    print("No discount")




# 9. Identify number type single-digit / double-digit / multi-digit.

num_type = (input("Enter number type :"))

if len(num_type) == 1:
    print("single digit number")
elif len(num_type) == 2:
    print("double digit number")
elif len(num_type) >= 3:
    print("multi digit number")
else:
    print("Invalid number")



# 10. assign performance rating: poor / Average / Good / Excellent.

performance = int(input("Enter performance :"))

if performance >=1 and performance <= 39:
    print("poor")
elif performance >= 40 and performance <= 59:
        print("average")
elif performance >= 60 and performance <= 79:
    print("Good")
elif performance >= 70 and performance <= 100:
    print("Excellent")
else:
    print("out of range")




   
    
    
    
    
    

