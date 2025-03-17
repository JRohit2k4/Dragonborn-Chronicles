print("\n====== Skyrealm: Unbound ======")
print("\n## Opening eyes with blurred vision ##")
print("\n SCENE: The Prisoner Cart - Helgen Arrival")
print("\nPrisoner: Hey, you. You're finally awake.")

print("\n1. Who are you? \n2. Where are we going? \n3. Just my luck...")
try:
    first_dialogue = int(input("Choose an option (1/2/3): "))  # Convert input to integer
    if first_dialogue == 1:
        print("\nPrisoner: I am Ralof, of Riverwood, fighting for Skyrealm\'s freedom.")
    elif first_dialogue == 2:
        print("\nPrisoner: We\'re on our way to Helgen, to our deaths...")
    elif first_dialogue == 3:
        print("Prisoner: 'Aye, we all are… *he looks ahead, lost in thought*")
        print("\nRalof: Damn these Imperials...")
        print("Imperial Guard: One more bad word about us Imperials, and you’ll meet your death here.")
    else:
        print("\nPrisoner: Huh? Are you alright? Must be the bump on your head.")
except ValueError:
    print("\nPrisoner: Huh? You didn't say anything? Guess you're still waking up.")

print("\n\n====== Arrived at Helgen ======")
print("SCENE: Getting ready for execution")
print("\nImperial Soldier: What is your race")
print("\n1. Nord \n2. Khajiit \n3. Dark Elf \n4. Argonian")

try:
    race_choice = int(input("Choose an option (1/2/3/4/5): "))  # Convert input to integer
    if race_choice == 1:
        race = "Nord"
        print("\nImperial Soldier: A fellow Nord? Perhaps we can make an exception....")
    elif race_choice == 2:
        race = "Khajiit"
        print("\nImperial Soldier: A Khajiit? Probably a thief… You’re not supposed to be here.")
    elif race_choice == 3:
        race = "Dark Elf"
        print("\nImperial Soldier: A Dark Elf? The Empire doesn’t care about you either!")
    elif race_choice == 3:
        race = "Argonian"
        print("\nImperial Soldier: An Argonian? Strange to see one this far north.")
    else:
        race = "Unknown"
        print("\nImperial Soldier: It doesn't matter anyway.")
except ValueError:
    race = "Unknown"
    print("\nImperial Soldier: Huh? You didn't say anything? Guess you're still waking up.")

name = input("\nImperial Soldier: What is your name: ")
print(f"\nImperial Soldier: {name} the {race}, huh? Another prisoner for the list.")
