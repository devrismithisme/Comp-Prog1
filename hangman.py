import random
wordlist = []
f =open("sowpods.txt","r")
for I in f:
    wordlist.append(I)
print (random.choice(wordlist))         



word = random.choice(wordlist)
letters_guessed = []

print("Welcome to HangMan.")


turns = 6

while turns > 0:
    def display_clue(word, letters_guessed):
        clue = ""
        for letter in word:
            if letter.lower() in letters_guessed or letter.upper() in letters_guessed:
                clue += letter + " "
            else:
                clue += "_ "
        return clue

    while True:
        print(display_clue(word, letters_guessed))
        guess = input("Guess a letter: ").upper()
        if guess in letters_guessed:
            print("Guess again. You have already geussed that letter.")
            continue
        letters_guessed.append(guess)
        if all(letter.lower() in letters_guessed or letter.upper() in letters_guessed for letter in word):
            print(f"Fantastic! You guessed my word: {word}")
            print("You are so awesome. You get a Gold Star!! YAY!!")
            break
        if guess not in word:
            turns -= 1
            print("Incorrect!That letter is not in the word. ")
            print(f"You have {turns} more turns left.")
            if turns == 0:
                print(f"You loose! The word was {word}")
                break




