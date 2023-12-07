print("'Hello avdenturer' an old woman says as you enter a cabin. 'Welcome to the place where all adventures begin.'")
line1 = input("'What is your name?' ")
print("'I'm sure you are here to start your journey.' ")
print("You stare blankly at her.")
print(f"'Well,' she says, 'off with you now! There is no time to waste {line1}! Your adventure begins!")


player_health = 100
enemy_health = 100

import random
beast_list = ["Cyclops", "Goblin", "Werewolf"]
beast = random.choice(beast_list)


import random
awards_list = ["leash", "goblet", "eye"]
awards = (awards_list)



def attack_enemy():
    while True:
        if player_health > 0:
            your_attack = random.randint(10, 100)
            print(f"You attacked the enemy for {your_attack} damage!")
            enemy_health -= your_attack
        if enemy_health > 0:
            enemy_attack = random.randint(10, 100)
            print(f"You attacked the enemy for {your_attack} damage!")
            player_health -= enemy_attack
        if player_health <= 0:
            print("You died")
            break
        if enemy_health <= 0:
            print("You have vanquished your foe!")
            print("You have recieved an item and 25 health.")
            player_health += 25
            break


while player_health > 0:
    line2 = input("Press w to walk or i to check your inventory. ")
    if line2 in "i":
        print(f"This is your inventory {line1}. Your health is {player_health}.")
        if awards in awards_list:
            print(f"You have a {awards}.")
        else:
            print("You have no awards")
            print(f"You have a/ an {awards}.")
    elif line2 in "w":
        for beast in beast_list:
            chances = [(line2), (line2), (beast)]
            chance = random.choice(chances)
            if beast in chance:
                print(f"Oh no! It's a {beast}!")
                line3 = input("Would you like to run or fight great adventurer? ")
                if line3 in "fight":
                    print(attack_enemy(player_health, enemy_health))
                    
                break
        else:
            print("You are walking. ")
    else:
        print("Please enter 'w' or 'i'. "
    
        
#if fight_input == "fight":
 #   attack_enemy(player_health, enemy_health)



# need 3 evils. need them to be random(1/3 or 1/4 chance). 