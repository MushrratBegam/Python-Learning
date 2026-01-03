#---Type conversion---

# a= float("2")
# b=4.25
# sum=a+b
# print(type(a))
# print(a+b)



num_1 = float(input('enter number 1 ='))
num_2 = float(input('enter number 2 = '))

choice = input('enter your choice + - *  ** = ')

if choice == '+':
    print(f'addition:{num_1 + num_2}')
    
elif choice == '-':
    print(f'substraction : {num_1 - num_2}')
    
elif choice == '*':
    print(f'multiplication : {num_1 * num_2}')
    
elif choice == '**':
    print(f'exponentiation : {num_1 ** num_2}')
    
else:
    print('in-valid choice')