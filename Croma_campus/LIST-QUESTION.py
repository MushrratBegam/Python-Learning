# BASIC LEVEL
#___________________________________________________________________________________________

# 1. write a python program to create a list of integer and print it's elements.
list = [23,45,67,88,98]
print(list)


# 2. write a program to find the sum and average of element in a list.
list = [4,5,12,67,78,90]
print(sum(list))
print(sum(list)/len(list))


# 3. write a program to find the largest and smallest element of a list.
list = [65,23,54,76,12,34]
print(max(list))
print(min(list))


# 4. write a python program to count the number of elements in a list without using len().
list = [45,32,12, 22, 56,80,20]
count = 0 
for i in list:
    count = count + 1
print(count)


# 5. write a program to reverse a list withount using built in function.
list = [23,65,20,38,94,78,21]
print(list)
print( list[: : -1])


# 6. write a program to check if an element exixt in a list.
list = [4,5,7,9,12,16,35,25]
element = int(input("Enter a element :"))

for i in list:
    if i == element:
        print("Element exist in the list")
        break
else:
    print("Element does not exist in the list")


# 7. write a python program to print a duplicate elements from a list.
list = [23,23,45,76,87,23,98,70,98,70]
print(list)
duplicate = []

for i in list:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)


# 8. write a program to sort a list in ascending and descending order.
list = [67,98,67,90,88,23,12,34,26]
print(list)
list.sort()
print(list)
print(list[: : -1])


#_________________________________________________________________________________________-
# INTERMEDIATE LEVE

# 9. write a program to merge two lists and remove duplicate.
list = [34,23,56,13,14,45,67,34,13]
print(list)
list2 = [1,2,3,4,7,9,1,2]
list.extend(list2)
print(list)

new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)  


# 10. write a program to find common elements between two lists.
list1 = [12,34,45,46,76]
list2 = [12,78,98,34,45]
for i in list1:
    if i in list2:
        print(i)    


# 11. write a program to split a list into even or odd number.
list = [12,13,14,6,9,4,8,11]
even = []
odd = []

for i in list:
    if i % 2 == 0:
        even.append(i)
        print("Even number =",even)
    else:
        odd.append(i)
        print("Odd number",odd)


# 12. write a program to rotate a list by n position.





# 13. write a python program to find a second largest number in a list.
list = [34,23,67,89,50,45]
list .sort()
print("second largest number is",list[-2])


# 14.write a program to flatten a nested list.




# 15. write a program to count frequency of each element in a list.
list = [1,1,9,9,9,7,6,4,4,8,5,1,2,]
for i in set(list):
    print(i,":",list.count(i))


# 16. write a program to replace all negative number with zero in a list.
list = [1,2,3,4,5,-9,-3,-6,-7]
for i in range(len(list)):
    if list[i] < 0:
        list[i] = 0
print(list) 

#______________________________________________________________________________________________

# ADVANCED LEVEL.

# 17. write a program to remove all occurences of a given element from a list.

list = [1,2,3,4,3,6,3,8,3,93,5,3,7]
element = 3

list2 = []
for i in list:
    if i != element:
        list2.append(i)
print(list2)  


# 18. write a program to check if a list is a palindrome.
list = [1,2,3,2,1]
if list == list[::-1]:
    print("list is palindrome")
else:
    print("list is not palindrome")

      











        
        




    