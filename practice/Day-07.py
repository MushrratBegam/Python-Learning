# # #---Tuples----

# # movies=[]
# # mov1 = input ("enter first movie:")
# # mov2 = input ("enter second movie:")
# # mov3 = input ("enter third movie:")

# # movies.append (mov1)
# # movies.append (mov2)
# # movies.append (mov3)

# # print (movies)


# #----tuples----
# list1 =[1,2,1]
# list2 =[1,2,3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")

# info = {
#     "name": "apnacollege",
#     "subjects": ["python", "c", "java"],
#     "topics": ("dict", "set"),
#     "age": 35,
#     "is_adult": True,
#     "marks": 95.6
# }


# set1 = {1,2,3}
# set2 = {2,3,4}

# print(set1.intersection(set2))

# subject = {
#     "python", "java", "c++", "python", "javascript", "python", "java", "c"
# }

# print(subject)

# print(len(subject))

marks = {}

x = int(input("enter phy:"))
marks.update({"phy" : x})

x = int(input("enter math:"))
marks.update({"math": x})

x = int(input("enter chem:"))
marks.update({"chem": x})

print(marks) 