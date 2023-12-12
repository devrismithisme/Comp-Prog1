print("'Hello avdenturer' an old woman says as you enter a cabin. 'Welcome to the place where all adventures begin.'")
line1 = input("'What is your name?' ")
print("'I'm sure you are here to start your journey.' ")
print("You stare blankly at her.")
print(f"'Well,' she says, 'off with you now! There is no time to waste {line1}! Your adventure begins!")
print("You head out the door and off on your adventure.")



import random
beast_list = ["Cyclops", "Goblin", "Werewolf"]
beast = random.choice(beast_list)
awards_list = ["goblet","leash", "eye"]
awards = random.choice(awards_list)

player_health = 100
enemy_health = 100
inventory = []


def run_from_enemy(player_health, enemy_health):
    run_chance = random.randint(1,2)
    if run_chance == 1:
        print("you ran away!")
    elif run_chance == 2:
        while True:
            if player_health > 0:
                enemy_attack1 = random.randint(10,100)
                print(f"The enemy attacks you for {enemy_attack1} damage!")
                player_health -= enemy_attack1
            if player_health <= 0:
                print(f"You have died O' Cowardly {line1}!")
                exit()
            if enemy_health <= 0:
                print(f"You have vanquished your foe O' Great {line1}!")
                inventory.append(awards)
                break
        



def attack_enemy(player_health, enemy_health):

    while True:
        if player_health > 0:
            your_attack = random.randint(10, 100)
            print(f"You attack the enemy for {your_attack} damage!")
            enemy_health = enemy_health - your_attack
        if enemy_health > 0:
            enemy_attack = random.randint(10, 100)
            print(f"The enemy attacks you for {enemy_attack} damage!")
            player_health = player_health - enemy_attack
        if player_health <= 0:
            print(f"You have died a valiant death O' Great {line1}!")
            exit()
        if enemy_health <= 0:
            print(f"You have vanquished your foe O' Great {line1}!")
            inventory.append(awards)
            break


while player_health >= 0:
    line2 = input("Press w to walk or i to check your inventory. ")
    if line2 in "i":
        print(f"This is your inventory {line1}. Your health is {player_health}.")
        if awards in awards_list:
            print(f"You have a/an {awards}.")
        else:
            print("You have no awards")
    elif line2 in "w":
        for beast in beast_list:
            chances = [(line2), (line2), (beast)]
            chance = random.choice(chances)
            if beast in chance:
                print(f"Oh no! It's a {beast}!")
                line3 = input("Would you like to run or fight great adventurer? ")
                if line3 in "fight":
                    print(attack_enemy(player_health))
                    if player_health > 0:
                        print(f"You get an item! You got a/an {awards}")
                else:
                    print(run_from_enemy())
                break
        else:
            print("You are walking. ")
    else:
        print("Please enter 'w' or 'i'. ")
    
        
#if fight_input == "fight":
 #   attack_enemy(player_health, enemy_health)

#After you helped me, it did not work...


# need 3 evils. need them to be random(1/3 or 1/4 chance). hi