
start = '''
Your name is Janie and You wake up one morning to recieve a suprise text from your crush. You have had a crush since 7th grade.
You are now both in the 11th grade. You are a little frustrated that he just now noticed you after such a long time.
Do you ignore his text or respond? '''

end_of_story = ("The end!")

print(start)
done = False
while not done:
    print("Type 'ignore' to ignore or 'respond' to respond.")
    user_input = input()

    if user_input == "ignore" :
        print("You decide to ignore his text he never appreciated you anyway. You go back to sleep ") # finished the story by writing what happens
        print(end_of_story)
        done = True
    elif user_input == "respond":
        print("You respond to his text")
        done=True
    else:
        print("Wrong Option")
        done = False

done = False
while not done:
    print("You say Wow I would love to go out with you at 8pm. See you then. ")
    print("You text everyone you know the good news!")
    print("You have two dress options.")
    print(" The green dress is low-cut and shows a lot of skin while the blue one is very casual and flowy")
    print(" Which one do you pick?")
    print("Type 'green' to pick the green dress or 'blue' to pick the blue dress.")
    user_input = input()

    if user_input == "green":
        print("Wow thats a lot of skin im showing!  But i'm going all out.")
        done = True

    elif user_input == "blue":
        print("I don't want to seem like I'm trying too hard.")
        done = True
    else:
        print("Wrong Option")
        done = False

done = False
while not done:
    print("So for my makeup,I'm going barefaced.")
    print("I'm way too tired for all of this.")
    print("i'm calling greg to pick me up")
    print("Type 'call greg' now.")
    user_input = input()

    if user_input == "call greg":
        print("Hey I'm ready.")
        done = True
    else:
        print("Wrong Option")
        done = False

done = False
while not done:
    print("Greg picks you up. \nHe then drives you to the most disgusting resturant in town.")
    print("You are afraid to even breathe the air inside.")
    print("Greg pulls out a chair for you.")
    print("Its time to order.")
    print("Type 'Salad' to order salad or 'Steak' to order.")
    user_input = input()

    if user_input == "Salad":
        print("Your Salad arrives and it looks extremely disgusting")
        print("You manage to swallow down some of it.")
    elif user_input == "Steak":
        print("Your waiter drops your steak into your lap and Greg laughs.")
        print("You see a man collapse after eating it.")
    else:
        print("Wrong Option")
        done = False

done = False
while not done:while not done:
    print("Greg finally drives you home after you cried for 20 mins.")
    print("Time to reflect how did your date go?")
    print("Type 'Amazing date' or 'nightmarish date' to choose.")

    user_input = input()

    if user_input == "Amazing date":
        print("Apart from everything looking disgusting his cuteness made everything better.")
        print("Cant wait to do it again.")
    elif user_input == "nightmarish date":
        print(" I will never talk to him ever again.")
        print(" What a cheapskate.")
    else:
        print("Wrong Option")
        done = False
