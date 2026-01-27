# 1. write a program to print a number pattern using loop.
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()


# 2. write a program to count the frequency of each character in a string.
text = input("Enter a string :")
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("character frequency :")
for char, count in freq.items():
    print(char,":",count)        


# 3. write a program to print all armstrong numbers between 1 and 1000.
num = 1
while num <= 1000:
    temporary = num
    sum = 0
    
    while temporary > 0:
        digit = temporary % 10
        sum = sum + (digit ** 3)
        temporary = temporary // 10
        
    if sum == num:
       print(num)
    num +=1


# 4. write a program to simulate an ATM menu using a while loop.
Balance = 10000
while True:
    print("\n \t \t \t ATM MACHINE")
    print("\n \t \t1. Check Balance")
    print("\t \t2. Deposite Balance")
    print("\t \t3. Withdrawal Balance")
    print("\t \t4. Exit")
    ch = int(input("\n\t\tEnter your choice :"))
    if ch == 1:
        print("\n\t\tcurrent Balance :",Balance)
        
    elif ch == 2:
        b = int(input("\n\t\tEnter amout to deposite :"))
        Balance = Balance + b
        print("Balance deposite suceesfully!!!")
    elif ch == 3:
        w = int(input("\n\t\tEnter amount to withdrawal :"))
        Balance = Balance - w
        print("Withdrawal successful!!!")
    elif ch == 4:
        print("Bye_Bye")
        break
    else:
        print("Invalid choice")


# 5. write a program to find the GCD of two number using loop
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

while b != 0:
    a,b = b,a % b
print("GCD", a)  