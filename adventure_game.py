import time
import random

teams = ["time-travellers",
         "Time Jumpers",
         "Chrono Explorers",
         "Dimensional Drifters",
         "Time Wielders"]
artifacts = ['recorder', 'journal', 'diary', 'scroll']
villians = ['the Seekers',
            'the Time Bandits',
            'the Chrono Villains',
            'the Temporal Terrors',
            'the Dark Time Sorcerers']
weapons = ['knife', 'gun', 'sword', 'dagger']
team = random.choice(teams)
artifact = random.choice(artifacts)
villian = random.choice(villians)
weapon = random.choice(weapons)
location = {}
    

def theInput():
    location["result"] = input("1: an old bookstore in a hidden alleyway\n"
                               "2: a weird appliance store\n"
                               "3: a dusty old attic\n")


def end():
    print_pause("GAME OVER")


def print_pause(message):
    print(message)
    time.sleep(2)


def onWin():
    print_pause("Congratulations! Your determination and ")
    print_pause("choices have led to a triump")
    print_pause(f"The Future {artifact}'s power had led you on"
                "a thrilling adventure,")
    print_pause("You've safeguarded the timeline"
                "and ensured a better future for all.")


def onLoss():
    print_pause("Unfortunately, your journey ends in failure.")
    print_pause("The consequences of your actions ripple through time,")
    print_pause("leading to a bleak and uncertain future")
    print_pause("Your adventure has come to a somber conclusion.")


def intro():
    print_pause("It is a lazy Saturday afternoon")
    print_pause("You decided to take a walk around town")
    print_pause("You consider where to go, and you stumbled upon...")
    theInput()
    if location["result"] == '1':
        print_pause("an old bookstore nested in a hidden alleyway.")
        print_pause("Inside, you ...")
    elif location["result"] == '2':
        print_pause("You find yourself in a weird appliance store")
        print_pause("and decided to search for something intriguing.")
        print_pause("as you browse the store...")
    elif location["result"] == '3':
        print_pause("You find yourself in a dusty old attic")
        print_pause("It was surrounded by stacks of forgotten belongings.")
        print_pause("While rummaging through the clutter...")
    else:
        intro()
    print_pause(f"you stumbled upon a peculiar {artifact}"
                " with a futuristic design.")
    print_pause("On it is a holographic design that glows softly")
    print_pause("and a strange aura seemed to emanate from it.")


def startOver(callback):
    print_pause("Do you want to pick up where you left off or start over?")
    restart = input("1: Remake choice\n"
                    "2: Start Over\n")
    if restart == "1":
        callback()
    elif restart == "2":
        run_game()
    else:
        print_pause("Invalid Input: click 1 or 2")
        startOver()


def play_again(callback):
    prompt = input("Would you like to play again? yes/no\n")
    if prompt.lower() == 'yes':
        startOver(callback)
    elif prompt.lower() == 'no':
        print_pause("Ok, Goodbye!!")
    else:
        play_again(callback)


def pick_artifact():
    print_pause(f"you decide to buy the {artifact} and take it home,")
    print_pause("Excited by your purchase...")
    print_pause(f"you rush home to explore the {artifact}.")


def drop_artifact():
    print_pause(f"You leave the {artifact} and continue browsing the area.")
    print_pause(f"After scanning through the area for a while,")


def fight():
    fight = input(f"1: Face off with {villian}\n"
                  "2: Surrender to them\n")
    if fight == '1':
        print_pause(f"You Stand your ground and face off with {villian}")
        print_pause(f"You use the {artifact}'s predictions strategically")
        print_pause(f"Using the accurate predictions, you defeat {villian}")
        onWin()
        print_pause("You Win!")
        play_again(fight)
    elif fight == '2':
        print_pause(f"You decided to surrender to {villian}")
        print_pause(f"the {artifact} was taken from you,")
        print_pause("and its power remained hidden from the world")
        onLoss()
        end()
        play_again(fight)
    else:
        fight()


def confrontation():
    do = input("1: Confront the mastermind behind the plot.\n"
               "2: Evade the mastermind and try to rewrite history"
               "to prevent the manipulation.\n")
    if do == '1':
        print_pause("You confront the mastermind behind the plot")
        ambush()
    elif do == '2':
        print_pause("You decide to evade the masterminds")
        print_pause("and try to change the future")
        print_pause("Your plan to evade them failed")
        ambush()
    else:
        confrontation()


def allies():
    print_pause("With your new allies, you embark on a thrilling journey")
    print_pause("through time and space,")
    print_pause(f"uncovering the {artifact}'s hidden powers.")
    print_pause("As you explore different eras...")
    print_pause("you discover a sinister plot to manipulate history.")
    confrontation()


def ambush():
    print_pause(f"The masterminds were known as {villian}")
    print_pause(f"They demanded the {artifact},")
    print_pause("warning of dire consequences if you refused.")
    choice = input("What do you do ?\n"
                   f"1: Hand over the {artifact}\n"
                   f"2: Refuse to give up the {artifact}.\n")
    if choice == '1':
        print_pause(f"You decide to surrender the {artifact} to them")
        print_pause("You do so with hopes that they let you leave safely")
        print_pause("However, the Leader of the group comes at you")
        print_pause(f"and struck you with a {weapon}")
        end()
        play_again(ambush)
    elif choice == '2':
        print_pause(f"You decide,you are never giving the {artifact} up")
        print_pause("The leader of the group comes at you, what do you do?")
        fight()
    else:
        ambush()


def strangers():
    print_pause(f"You approach the strangers discussing the {artifact}.")
    print_pause(f"They introduce themselves as {team}")
    print_pause(f"and explained the {artifact}'s potential.")
    print_pause("They offer to help you decipher its secrets.")
    print_pause("You decide to...")
    decide = input("1: Accept their offer and join forces.\n"
                   "2: Decline their offer and leave.\n")
    if decide == '1':
        allies()
    elif decide == '2':
        end()
        play_again(strangers)
    else:
        strangers()


def onDrop():
    print_pause("As you continue to explore further...")
    print_pause("you overhear a conversation")
    print_pause(f"between two strangers about the {artifact}.")
    print_pause("It piques your interest.")
    print_pause("You decide to...")
    choice = input(f"1: Approach them and inquire about the {artifact}.\n"
                   f"2: Ignore the conversation and go home.\n")
    if choice == '1':
        strangers()
    elif choice == '2':
        print_pause("You decide to go home")
        end()
        play_again(onDrop)
    else:
        onDrop()


def trappedInTime():
    print_pause("You desperately search for a way back to your time")
    print_pause("but realize that you're trapped in this time forever.")
    print_pause(f"The {artifact}'s holographic message mocks you.")
    end()
    play_again(distant_future)


def expose():
    choice = input("1: Expose the conspiracy to the world.\n"
                   "2: Join the conspirators.\n")
    if choice == '1':
        print_pause("You decide to expose the consipracy to the world")
        print_pause("While trying to do so,"
                    "you come across the masterminds")
        ambush()
    elif choice == '2':
        print_pause("You decide to sought the conspirators")
        print_pause("With hopes of joining them for your protection")
        ambush()
    else:
        expose()


def commotion():
    print_pause("You select a date in the near future, and...")
    print_pause("you're transported to a world eerily similar to your own,")
    print_pause("but with some noticeable differences.")
    print_pause("You hear a distant commotion.")
    decide = input("1: Investigate\n"
                   "2: Ignore commotion\n")
    if decide == '1':
        print_pause("As you investigate the commotion..")
        print_pause("you stumble upon a conspiracy to control time itself.")
        print_pause("You must decide how to proceed.")
        expose()
    elif decide == '2':
        print_pause("Ignoring the commotion...")
        print_pause("You look for clues in the diary")
        print_pause("about differences in this world")
        print_pause("You try your best to get back to your own world")
        trappedInTime()
    else:
        commotion()


def distantFuture():
    robot = input("1: Trust and follow guide to explore.\n"
                  "2: Return to your own time by finding the diary.\n")
    if robot == '1':
        allies()
    elif robot == '2':
        trappedInTime()
    else:
        distantFuture()


def onBuy():
    print_pause("A holographic message pops up,"
                "asking for your name and a date to explore.")
    print_pause("You respond with your name and select a date at random.")
    print_pause("You chose to..")
    date = input("1: Choose a date in the distant future.\n"
                 "2: Choose a date in the near future.\n")
    if date == '1':
        print_pause("You select a date in the distant future, and suddenly...")
        print_pause("you're transported into a strange, advanced world.")
        print_pause("A robotic guide approaches you.")
        allies()
    elif date == '2':
        commotion()
    else:
        onBuy()


def explore():
    choiceL = input(f"1:explore the {artifact}\n"
                    f"2:leave the {artifact} in the attic\n")
    if choiceL == '1':
        onBuy()
    elif choiceL == '2':
        print_pause(f"You decide to leave the {artifact} in the attic")
        onDrop()
    else:
        print_pause("wrong input")
        explore()


def purchase():
    choice = input(f"1: Purchase the {artifact} and take it home.\n"
                   f"2: Leave the {artifact}.\n")
    if choice == '1':
        pick_artifact()
        onBuy()
    elif choice == '2':
        drop_artifact()
        onDrop()
    else:
        purchase()


def adventure_begins():
    print_pause(f"What do you want to do with the {artifact}?")
    if location["result"] == '3':
        explore()   
    else:
        purchase()


def run_game():
    global team
    global artifact
    global villian
    global weapon
    team = random.choice(teams)
    artifact = random.choice(artifacts)
    villian = random.choice(villians)
    weapon = random.choice(weapons)
    intro()
    adventure_begins()


run_game()
