# Task 1 Code Correction 
# Task 2 Venue Selection 
# Task 3 Catering Choices 


attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "small hall"
print(venue)

facilities = "audio" if venue == "large hall" else "projector"
print(facilities)

food = str(input("Would you like vegetarian food? (yes/no) "))
vegetarian = "Veggie Delight Caterers" if food == "yes" else "Gourmet Meals Caterers"
print(vegetarian)