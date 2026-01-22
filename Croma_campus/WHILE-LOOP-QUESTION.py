# 1. write a program to print numbers from 1 to 50 using a while loop.
num = 0
while num < 50:
    num = num+ 1
    print(num)

    
# 2. write a program to print all odd number between 1 and 50.
num = 0
while num <= 50:
    if num % 2 != 0:
        print(num)
    num = num + 1

    
# 3. write a program to calculate the sum of digits of a number.
num = int(input("Enter a number:"))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("digit sum =",sum)


# 4. write a program to reverse a number using a while loop.
num = int(input("Enter a number :"))
add = 0
a = 1
while a <= num:
    rem = num % 10
    add = add * 10 + rem
    num = num // 10
print(add)


# 5. write a program to calculate the factorial of a number using while loop.
num = int(input("Enter a number :"))
fact = 1
while num > 0 :
    fact = fact * num
    num = num - 1
    print("factorial :",fact) 


# 6. write a program to keep taking input from the user until the user enter 0.
num = 1
while num != 0:
    num = int(input("Enter a number :"))
else:
    print("Bye")


# 7. write a program to find the largest digit of a number.
num = int(input("Enter a number :"))
largest = 0
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
        num = num // 10
        print("Largest digit =",largest)


# 8. write a program to check whether a number is palindrome.
num = int(input("Enter a number :"))
original = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if original == rev:
    print("palindrome number") 
else:
    print("not palidndrome") 


# 9. write a program to print the fabbonacci series up to n terms.
num = int(input("Enter a number :"))
a = 0
b = 1
count = 0
while count < num:
    print(a,end="")
    c = a + b
    a = b
    b = c
    count += 1  


# 10. write a program to implement a number gussing game using a while loop.
import random
num = random.randint(1,6)
ch = 0
while True:
    ch = int(input("we generate the number guess the number :"))
    if ch == num:
        print("you win")
    else:
        print("Try again!!!")   
    
    
    

    

        
    
    
        