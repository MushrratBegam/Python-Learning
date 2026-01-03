# 1- import the random module
import random


# 2- create subjects
subjects = [
    "Shahrukh khan",
    "Virat kohli",
    "Nirmala sitharaman",
    "A mumbai cat",
    "A group of monkeys",
    "Prime minister modi",
    "Auto ricksaw driver from delhi",
]

actions = [
    "lunches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
]

places_or_thing = [
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL match",
    "at india gate",
]

# 3- start the headline generator loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_thing)
    
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    
    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break
    
# 4- print goodbye message

print("\nThanks for using the Fake News Headline Generator. Have a fun day")