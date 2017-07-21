from random import *



#Create the list of words you want to choose from.
Sides = ["Fries", "onionrings", "Salad", "Breadsticks","assorted fruits"]
Desserts = ["cookies", "Icecream", "peach_cobbler", "Cake", "Macaroons"]
Main_course = ["Chicken_nuggets", "Beef_wellington", "Burgers", "Pizza", "Steak"]

#Generates a random integer.
a = randint(0, len(Sides)-1)
b = randint(0, len(Desserts)-1)
c = randint(0, len(Main_course)-1)
print (Sides[a],Desserts[b],Main_course[c])
