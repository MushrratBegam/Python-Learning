# 1. write a python program to print a square star pattern.
for i in range(1,6):
    for j in range(1,6):
        print("*", end = "")
    print("") 


# 2. write a python program to print a write angle triagle star pattern.  
for i in range(1,7):
    for j in range(1,i+1):
        print("*",end = "")
    print() 


# 3. write a python program to print an inverted right-angle triangle.
for i in range(6,0,-1):
    for j in range(1,i+1):
        print("*",end = "")
    print() 


# 4. write a python program to print a pyramid star pattern.
for i in range(1,6):
    for k in range(5,i,-1):
        print(" ", end = "")
    for j in range(1,i+1):
        print("* ",end = "")
    print()    


# 5. write a python program to print an inverted pyramid star pattern.
for i in range(5,0,-1):
    # space ke liye...
    for k in range(5,-1):
        print(" ",end = "")
    for j in range(2*i-1):
        print("*",end = "")
    print()      


# 6. write a python program to print a left aligned triangle pattern.
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end = "")
    print()    

# 7. write a python program to print a house-shaped star pattern.
for i in range(1,6):
    for k in range(5,i,-1): 
      print(" ", end = "")
    for j in range(1,i+1):
      print("* ",end = "") 
    print()  
    
for q in range(1,6):
    for p in range(1,6):
      if p == 1 or p == 5:
        print("* *    ", end = "")
    print()


# 8. write a python program to print a right-aligned triangle pattern.
for i in range(1,6):
    print(" "*(6-i),"*"*i)   


# 9. write a python probram to print a number triangle pattern.
variable = ""
for i in range(1,6):
    variable = variable + str(i)
    print(variable)


# 10. write a python program to print a same number triangle pattern.
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end = "")
    print(i)   


# 11. write a python program to print a floyd's triangle.
num = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(num,end = "")
        num += 1
    print()    
 

# 12. write a python program to print a binary pattern (0 and 1).
a = 1
b = 0
for i in range(1,6):
    for j in range(1,i+1):
        print(b , a,end = "")
        a = a + b
        b = -b
    print()     
       
                        