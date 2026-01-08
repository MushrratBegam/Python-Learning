# #QUE-1 create a new file "practice.txt" using python.add the following data in it:
# #---Hi everyone
# #---we are learning file I\O
# #---using java.
# #---I like programming in java
# with open("practice.txt", "w") as f:
#     f.write("Hi rveryone\nwe are learning file I\O\n")
#     f.write("using java\nI like programming in java.")
    
    
    
# #QUE-2 write a function that reolaces all occurences of "java" with "python" in above file.
# with open("practice.txt", "r") as f:
#     data = f.read()
    
# new_data = data.replace("java", "python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)
    
    
# #QUE-3 Search if the word "learning" rxist in the file or not.
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")    
        
        
        
        
# #QUE-4 write a function to find in which line of the file does the word "learning" occure first . print -1 if word not found.
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()




#QUE-5 from a file containing numbers seperated by comma, print the count of even numbers.
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count +=1
    print(count)