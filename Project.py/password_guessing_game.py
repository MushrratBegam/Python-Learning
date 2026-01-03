import random

easy_words = ["irfan", "talish", "rizwan", "ajaj","inaya","mussu"]
medium_words = ["patna", "madhubani", "darbhanga", "kolkatta", "delhi"]
hard_words = ["kinder-joy", "aalu-ka-pratha", "gorilla", "kanjivram", "zingalala-hu-hu"]

print("welcome to the passwoed guessing game")
print("choose a difficulty level: easy, medium or hard")

level = input('Enter difficulty:' ).lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
     print("Invalid choice. Defaulting to easy level")
     secret = random.choice(easy_words)
     
attempts = 0
print("\nGuess the secret password")
     
while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1
    
    if guess == secret:
        print(f'conguratulation! you guessed it in{attempts} attempts.')
        break
    hint = ""
    
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
         hint += guess[i]
    else:
        hint += "_"
        
    print("Hint:", hint)
print("Game over.")