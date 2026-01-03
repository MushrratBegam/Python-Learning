print("Welcome to my computer quiz!")
playing = input("Do you want to play?")

if playing != "yes":
    quit()
    
print("okay! lets play :)")

answer = input("what does CPU stand for?")
if answer == "central processing unit":
    print('correct!')
    score = +1
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for?")
if answer == "Graphics processing unit":
    print('correct!')
    score = +1
    
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for?")
if answer =="random access memory":
    print('correct!')
    score = +1
else:
    print("Incorrect!")
    
print("you got" + str(score) + "questions crrect!")
print("you got" + str((score / 4) * 100) + "%")
            
