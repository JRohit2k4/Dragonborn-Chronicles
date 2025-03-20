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
print("\mSCENE: Getting ready for execution")
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
    elif race_choice == 3:
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
print(f"\nImperial Soldier: {name} the {race}, huh? Another prisoner for the list.")


print("\n====== Chaos Unleashed ======")

print("\nThe sky, once clear, now swirls with thick black smoke as shadows dance across the ground.")

print("\nA deafening roar pierces the air, sending chills down your spine.")

print("\nThe wind picks up suddenly, dust and ash blinding your vision. The ground beneath you trembles violently.")

print('\nA deep, guttural growl rumbles from above…')

print('\nAlduin(Dragon): "VEN MUL RIIK!"')

print("\nA monstrous shadow engulfs the town as massive wings beat against the air, sending townspeople and soldiers into panic.")

print("\nThe dragon lands atop the tower with an earth-shattering crash, stone crumbling beneath its weight.")

print("\nAlduin rears his head, his scales glistening in the firelight, eyes burning with ancient fury.")

print('\nAlduin (Dragon): "ROOOAAARRR!"')

print("\nA torrent of flame erupts from its jaws, consuming everything in its path.")

print("\nScreams of villagers and soldiers mix with the roar of the inferno. Chaos reigns.")

print("\nRalof: \"By the gods... It's really happening! We need to move! NOW!\"")
