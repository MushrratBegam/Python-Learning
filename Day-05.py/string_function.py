#---str.Endswith---  #returns True if string ends with substr
str = "I am studying python from Apnacollege"
print(str.endswith("app"))
print(str.endswith("ege"))

#---str.capitalize---  #capitalizes 1st char
str = "i am studying pytho from apnacollege"
str = str.capitalize()
print(str)

#---str.replace(old,new)---  #replaces all occurence of old 
str = "I am studying python from Apnacollege"
print(str.replace("o" , "a"))
print(str.replace("studying" , "learning"))

#---str.find(word)---  #returns 1st index of 1st occurrer
str = "I am studying python from Apnacollege"
print(str.find("o"))  
print(str.find("t")) 

#---str.count("am")---  #counts the occurrence of substr
str = "I am studying python from Apnacollege"
print(str.count("t"))
print(str.count("o"))
 