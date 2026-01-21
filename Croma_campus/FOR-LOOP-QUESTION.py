# 1. write a program to print numbers from 1 to 100.
for i in range(1,101):
    print(i)

# 2. write a program to print all even number between 1 and 50.
num = 0
for i in range(1,51):
    if i % 2 == 0:
        num = i + 1
        print(i)


# 3. write a program to print the sum of first n natural numbers.
n = int(input("Enter n :"))
sum = 0
for i in range(1,n+1):
    sum = sum+i
    print("sum of first",n,"natural numbers=",sum)


# 4. write a program to print the multiplication table of a given number.
num = int(input("Enter a number :"))
for i in range(1,11):
        print(num,"X",i,"=", num*i)


# 5. write a program to print all element of list using a for loop.





# 6. write a program to count a number of vowel in a string.
string = input("Enter a string :")
vowels = "aeiouAEIOU"
count = 0

for ch in string:
    if ch in vowels:
     count += 1
    print("Number of vowels =",count)
    

# 7. write a program to find the largest number in a list.






# 8. write a program to print all prime numbers between 1 and 100.
for num in range(2,100):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
     print(num)            
    
        
# 9. write a program to calculate the factorial of a number using for loop.
n = int(input("Enter a range from 1 to :"))
for i in range(1,n+1):
    if n % i == 0:
        print(i)


# 10. write a program to print the reverse of a string using a for loop.
string = input("Enter a string :")
reverse = ""
for ch in string:
    reverse = ch + reverse
    print(reverse)

 
    
    
   

    