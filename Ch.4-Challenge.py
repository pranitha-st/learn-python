#This is an adventure game that involves choices and the player's input and a lot of other code.
Name = "Pranitha"
print(f"Welcome to {Name}'s Choose Your Own Adventure Game! As you follow the story, you will be presented with choices that decide your fate. Take care and choose wisely! Let's begin.")
print("You find yourself in a dark room with 2 doors. The first door is red, the second is white.")
DoorChoice = input("Which door do you want to choose? red=red door or white=white door")
if DoorChoice == "red":
    print("Great, you walk through the red door and are now in the future! You meet a scientist who gives you a mission of helping him save the world!")

    Choice1 = input("What do you want to do? 1=Accept ot 2=Decline")
    if Choice1=="1":
        print("""___________SUCCESS!__________
        You helped the scientist save the world! In gratitude, the scientist builds a time machine and sends you home!""")
    else: 
        print("""____________GAME OVER____________
    Too bad! You declined the scientist's offer and now you are stuck in the future forever!!!""")
else:
    
    print("Great, you walked through the white door and now you are in the past! You meet a princess who asks you to go on a quest.")
    QuestChoice = input("Do you want to accept her offer and go on the quest, or do you want to stay where you are? 1=Accept and go om the quest or 2=Stay")

    if QuestChoice=="1":
        print("The princess thanks you for accepting her offer. You begin the quest")
    else:
        print("""__________GAME OVER____________
        Well, I guess your story ends here""")
