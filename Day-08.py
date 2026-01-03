#----Loop----
#---while Loop---
#print number from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1 


#print number 100 to 1

# i = 100
# while i >=1:
#     print(i)
#     i -= 1

# print a multiplication table of a number n.
# n = int(input("enter a number:"))
# i = 1
# while i <= 10: 
#     print(n*i)
#     i += 1



#print the element of the following list using the loop
#[1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print (nums[idx])
#     idx += 1


#search for a number X in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]
nums = (1,4,9,16,25,36,49,64,81,100,36)
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
        break
    else:
        print("finding..")
        i += 1
        