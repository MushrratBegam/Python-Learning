# 1. write a python program to calculate income tax using slabs.
Income = int(input("Enter Income :"))

if Income <= 40000:
    Tax = 0
elif Income <= 70000:
    Tax = (Income - 40000) * 0.10
    
else:
    Tax = (30000 * 0.10) + (Income - 70000) * 0.20
print("Tax",Tax)


# 2. create an ATM withdrawal program with balance check.
Balance = 10000
withdrawal = int(input("Enter withdrawal amount :"))

if withdrawal <= Balance:
    Balance = Balance - withdrawal
    print("withdrawal successful")
    print("Balance :",Balance)
    
else:
    print("Insufficient balance")


# 3. check promotion eligibility using experience and performance.
experience = int(input("Enter experience :"))
performance = int(input("Enter performance rating(1-4) :"))

if experience >= 5 and performance == 3:
    print("Eligible for permotion")
else:
    print("not eligible for permotion")


# 4. impliment a grading system using nested if-else.




    
     
