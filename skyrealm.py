import time

print("\n====== Skyrealm: Unbound ======")
time.sleep(3)
print("\n## Opening eyes with blurred vision ##")
time.sleep(2)
print("\n SCENE: The Prisoner Cart - Helgen Arrival")
time.sleep(2)
print("\nPrisoner: Hey, you. You're finally awake.")
time.sleep(2)

print("\n1. Who are you? \n2. Where are we going? \n3. Just my luck...")
time.sleep(2)
try:
    first_dialogue = int(input("Choose an option (1/2/3): "))  # Convert input to integer
    if first_dialogue == 1:
        print("\nPrisoner: I am Ralof, of Riverwood, fighting for Skyrealm\'s freedom.")
        time.sleep(2)
    elif first_dialogue == 2:
        print("\nPrisoner: We\'re on our way to Helgen, to our deaths...")
        time.sleep(2)
    elif first_dialogue == 3:
        print("Prisoner: 'Aye, we all are… *he looks ahead, lost in thought*")
        time.sleep(2)
        print("\nRalof: Damn these Imperials...")
        time.sleep(2)
        print("Imperial Guard: One more bad word about us Imperials, and you’ll meet your death here.") 
        time.sleep(2)
    else:
        print("\nPrisoner: Huh? Are you alright? Must be the bump on your head.")
        time.sleep(2)
except ValueError:
    print("\nPrisoner: Huh? You didn't say anything? Guess you're still waking up.")
    time.sleep(2)

print("\n\n====== Arrived at Helgen ======")
time.sleep(3)
print("\nSCENE: Getting ready for execution")
time.sleep(2)
print("\nImperial Soldier: What is your race")
time.sleep(2)
print("\n1. Nord \n2. Khajiit \n3. Dark Elf \n4. Argonian")

try:
    race_choice = int(input("Choose an option (1/2/3/4/5): "))  # Convert input to integer
    if race_choice == 1:
        race = "Nord"
        print("\nImperial Soldier: A fellow Nord? Perhaps we can make an exception....")
        time.sleep(2)
    elif race_choice == 2:
        race = "Khajiit"
        print("\nImperial Soldier: A Khajiit? Probably a thief… You’re not supposed to be here.")
        time.sleep(2)
    elif race_choice == 3:
        race = "Dark Elf"
        print("\nImperial Soldier: A Dark Elf? The Empire doesn’t care about you either!")
        time.sleep(2)
    elif race_choice == 4:
        race = "Argonian"
        print("\nImperial Soldier: An Argonian? Strange to see one this far north.")
        time.sleep(2)
    else:
        race = "Unknown"
        print("\nImperial Soldier: It doesn't matter anyway.")
        time.sleep(2)
except ValueError:
    race = "Unknown"
    print("\nImperial Soldier: Huh? You didn't say anything? Guess you're still waking up.")
    time.sleep(2)

name = input("\nImperial Soldier: What is your name: ")
time.sleep(1)
print(f"\nImperial Soldier: {name.capitalize()} the {race}, huh? Another prisoner for the list.")

#Entry of Alduin the Dragon:-
print("\n====== Chaos Unleashed ======")
time.sleep(1)

print("\nThe sky, once clear, now swirls with thick black smoke as shadows dance across the ground.")
time.sleep(2)

print("\nA deafening roar pierces the air, sending chills down your spine.")
time.sleep(2)

print("\nThe wind picks up suddenly, dust and ash blinding your vision. The ground beneath you trembles violently.")
time.sleep(3)

print('\nA deep, guttural growl rumbles from above…')
time.sleep(2)

print('\nAlduin(Dragon): "VEN MUL RIIK!"')
time.sleep(1.5)

print("\nA monstrous shadow engulfs the town as massive wings beat against the air, sending townspeople and soldiers into panic.")
time.sleep(3)

print("\nThe dragon lands atop the tower with an earth-shattering crash, stone crumbling beneath its weight.")
time.sleep(3)

print("\nAlduin rears his head, his scales glistening in the firelight, eyes burning with ancient fury.")
time.sleep(3)

print('\nAlduin (Dragon): "ROOOAAARRR!"')
time.sleep(2)

print("\nA torrent of flame erupts from its jaws, consuming everything in its path.")
time.sleep(3)

print("\nScreams of villagers and soldiers mix with the roar of the inferno. Chaos reigns.")
time.sleep(3)

print("\nRalof: \"By the gods... It's really happening! We need to move! NOW!\"")
time.sleep(3)

print("\n*Soldiers starts to attack the dragon*")
time.sleep(3)

# Choice of faction
while True:
    print("\nGo to hideout inside tower")
    print("\nSelect which side you want to be on: ")
    print("\n1. Join the Imperials\n2. Follow Ralof (Stormcloaks)\n3. Find your own way (Not recommended)")
    
    try:
        sidewith_choice = int(input("Choose an option (1/2/3): "))  # Convert input to integer
        if sidewith_choice == 1:
            sidewith = "Imperials"
            print("\nImperial Soldier: Oh, so you want to join the fight.")
            time.sleep(2)
            print("\nImperial Soldier: Here take this..")
            time.sleep(2)
            print("\nYou got Bow and 20 Arrows(damage: 09)")
            time.sleep(2)
            print("\nLevel Increased 1-->2")
            break  # Exit loop
        elif sidewith_choice == 2:
            sidewith = "Stormcloaks"
            print("\nRalof: We need to stick together! Come on, let's move!")
            time.sleep(2)
            print("\n##You enetred in the tower with Ralof##")
            time.sleep(2)
            print("\n#You find dead Imperial soldiers under the debris of tower#")
            time.sleep(2)
            print("\nRalof: Here take this, it will be useful..")
            time.sleep(2)
            print("\nYou got Steel sword(damage: 12) \nYou got Steel armor(armor: 11) \nYou got Steel helmet(armor: 6) \nYou got Steel boots(armor: 6)")
            time.sleep(2)
            print("\nLevel Increased 1-->2")
            print("\nImperial soldier: Hey you two, you cannot escape.")
            time.sleep(2)
            print("\nRalof attack that soldier with his sword.")
            time.sleep(2)
            print("\nHelp him or left him alone:")
            time.sleep(2)
            save = int(input("\nChoose your action: \n(1.Help him) \n(2.Leave him)"))
            time.sleep(2)
            if save == 1:
                save = "1"
                print(f"\nRalof: There, you have a spirit of a {race}")
                time.sleep(2)
                print("\nYou both killed Imperial soldier")
                time.sleep(2)
                print("\nLevel increased 2-->3")
                time.sleep(2)
            else:
                sidewith = "2"
                print("\nRalof: Hey where are you going?...")
                time.sleep(2)
                print("\nRalof: AAAAHH")
                time.sleep(2)
                print("\nRalof got overhelmed and killed.")
                time.sleep(2)               
            break  # Exit loop
        elif sidewith_choice == 3:
            print("\nYou attempt to escape alone, running through the fire and smoke...")
            time.sleep(3)
            print("\nAlduin notices you and locks his gaze upon you...")
            time.sleep(3)
            print("\nBefore you can react, a torrent of fire engulfs you.")
            time.sleep(3)
            print("\nYOU DIED.")
            time.sleep(3)
            print("\nChoose wisely this time.")
            time.sleep(2)
        else:
            print("\nInvalid choice. Pick again.")
            time.sleep(2)
    except ValueError:
        print("\nInvalid input. Choose 1 or 2.")
        time.sleep(2)

print(f"\nYour journey continues as {name.capitalize()} the {race}, who side with {sidewith}. \n")
time.sleep(2)
