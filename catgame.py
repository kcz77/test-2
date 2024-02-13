import random

breeds = {
    "Siamese": {
        "Cuteness": 1}, 
    
    "British Shorthair": {
        "Cuteness": 2}, 
    
    "Maine Coon": {
        "Cuteness": 3}, 
    
    "Ragdoll": {
        "Cuteness": 4}
}

user_breed = random.choice(list(breeds.keys()))
print("You rolled..." + user_breed)
