import random

print (""""Welcome to this text-based CAT battle game!
       
       Before anything, lets make your character.""")

# Used to store the users answers to they can be retrived at any point
answer_dic = {}

### part 1: character creation

name = input("What would you like your name to be? ")
answer_dic["name"] = name

breeds = {
    "Siamese": {
        "Cuteness": 1}, 
    
    "British Shorthair": {
        "Cuteness": 2}, 
    
    "Maine Coon": {
        "Cuteness": 3}, 
    
    "Ragdoll": {
        "Cuteness": 4}}
    
while True:
    input1 = input("Now lets find out if you win the cat lottery or not... Type SPIN to spin the wheel~ ")
    
    if input1.upper() == "SPIN":
        # Picks a random breed for the user from the 'breeds' list
        user_breed = random.choice(list(breeds()))
        
        # Adds the randomly chosen breed to the answer dictionary
        answer_dic["user_catbreed"] = user_breed
        print ("You rolled..." + user_breed)
        break
    
    else: 
        print ("You gotta write 'SPIN' to spin :) ")

print ("As a " + answer_dic.get("user_catbreed") + " your attributes are... ")

