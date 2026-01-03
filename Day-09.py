#---For Loop---

# str = "mushrrat"

# for char in str:
#     print(char)
# else:
#     print("END")



# QUE-1--- print the element of the following list using the loop:

# nums = [1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)



# QUE-2---search for a number X in this tuple usong loop:

# nums = (1,4,9,16,25,36,49,64,81,100,49)

# x = 49
# idx = 0

# for el in nums:
#     if (el == x):
#         print("number found at idx", idx)
#         idx += 1


#----Range----

# seq = range(10)

# for i in seq:
#     print(i)


#---start?, stop, step?---
# range(stop?)
# for i in range(10):
#     print(i)


# range(start, stop)
# for i in range(2,18):
#     print(i)


# range(start, stop, step)

# for i in range(3,30,1):
#     print(i)




# QUE-1 print numbers from 1 to 100.
# for i in range(1,101):
#     print(i)



# QUE-2 print numbers from 100 to 1.
# for i in range(100,0,-1):
#     print(i)



# QUE-3 print the multiplication table of a number n. 
n = int (input("enter a number: "))
for i in range(1,11):
    print(n * i)


