
# task 1 code correction 
# task 2 setting the scene 
# task 3 default path 


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    light = input("Do you want to light a torch or proceed in the dark? ")
    if light == "light a torch":
        print("You find a hidden treasure!")    
    else:
        print("You might get lost, we cant see anything!")
    
else:
    pass 
    
    
    
