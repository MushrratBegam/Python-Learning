# BASIC LEVEL
#_______________________________________________________________________________________

# 1. write a python program to create a tuple and print its element.
tuple = (1,2,3,4,5,6,7,8)
print(tuple) 


# 2. Write a program to find the length of a tuple. 
t = (4,4,6,9,8,45,78,89)
print(len(t))


# 3. Write a program to find the maximum and minimum element in a tuple. 
t = (67,89,90,35,69,12,23)
print(max(t))
print(min(t))


# 4. Write a program to convert a tuple into a list.
t = (56,45,78,89,13,39)
print([t])


# 5. Write a program to check if an element exists in a tuple. 
tuple = (45,78,34,67,89,12,38,47)
element = int(input("Enter element :"))

for i in tuple:
    if i == element:
        print("Element exist in tuple")
        break
else:
    print("Element does not exit in element")


# 6.Write a program to count occurrences of an element in a tuple. 
t = (45,89,56,12,24,35,35,35,67,35,90,35)
element = int(input("Enter a element :"))
count = 0
for i in t:
    if i == element:
        count += 1
print("Occurence :",count)   


# INTERMEDIATE LEVEL.
#______________________________________________________________________________________

# 7. Write a program to count occurrences of an element in a tuple. 
t = (78,23,46,89,14,19,16,17)
print(t[2:7])


# 8. Write a program to find repeated elements in a tuple. 





# 9. Write a program to merge two tuples. 
t1 = (3,5,6,7,8,9)
t2 = (6,9,8,3,23,78,56)
t1 += t2
print(t1)


# 10. Write a program to unpack elements of a tuple into variables.




# 11. Write a Python program to sort a tuple.
t = (7,8,9,45,23,67,49,12)
sort_t = tuple(sorted(t))
print("original tuole =",t)
print("sorted tuple =",sort_t)


# 12. Write a program to convert a list of tuples into a dictionary. 
list = [(1,'a'),(2,'b'),(3,'c')]
dictionary = dict(list)
print(dictionary)

#____________________________________________________________________________________

# Advanced Level 

# 13. Write a program to find the index of an element in a tuple. 
tuple = (65,78,98,45,23,49,13,18,48)
print(tuple.index(18))


# 14. Write a program to remove an element from a tuple (without directly modifying it). 


 
 
# 15. Write a program to find common elements between two tuples. 
t1 = (1,2,4,6,7,8,9)
t2 = (2,3,9,6,4,78,34)
common = set(t1) & set(t2)
print("common elements",tuple(common))


# 16. Write a Python program to check if a tuple is a palindrome. 
tuple = (6,7,8,7,6)
if tuple == tuple[::-1]:
    print("tuple is palindrome")
else:
    print("tuple is not palindome")


# 17. Write a program to find the element with maximum frequency in a tuple.
tuple = (3,3,3,4,7,8,9,3,2,4,3)
element = []
for i in tuple:
    element += 1
    print(element) 


# 18. Write a program to create a nested tuple and access its elements. 



    
        



