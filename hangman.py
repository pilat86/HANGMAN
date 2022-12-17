import random
import time

print("\n****************************")
print("WELCOME TO THE HANGMAN GAME!\n")
name = input("What is your name?\n"
             "My name is: ")
print("****************************\n")

time.sleep(1)

print("****************************")
print(f"Hi, {name}!")
print(f"Please choose your level:\nEasy:       5 \u2764\uFE0F\nNormal:     4 \u2764\uFE0F\nHard:       3 \u2764\uFE0F\nImpossible: 1 \u2764\uFE0F\n")
level = input("Level: ")
print("****************************\n")

time.sleep(1)

level = level.upper()

if level == "EASY":
    level = 5
elif level == "NORMAL":
    level = 4
elif level == "HARD":
    level = 3
elif level == "IMPOSSIBLE":
    level = 1
else:
    print(f"{name}, you have to choose your level first.")


heart = "\u2764\uFE0F"
lives = []

for i in range(level):
    lives.append(heart)


def new_word():

    with open("words.txt") as f:
        words = f.read().splitlines()
        word = random.choice(words)
        word = word.upper()

    return word


word = new_word()
word_letters = []
symbol_letters = []
already_guessed = []


for i in word:
    word_letters.append(i)
    symbol_letters.append("-")


flag = False
while len(lives) > 0 and not flag:

    guess = input("Guess: ")
    guess = guess.upper()

    if guess in already_guessed:
        print("You already guessed that! ♻")

    elif guess in word_letters:

        print("Correct guess! ✅")
        already_guessed.append(guess)

        for i in range(len(word_letters)):
            if guess == word_letters[i]:
                symbol_letters[i] = guess
                if word_letters == symbol_letters:
                    print("You won! \U0001F389")
                    flag = True

    else:
        print("Wrong guess! ❌")
        lives.pop(0)
        already_guessed.append(guess)
        if len(lives) == 0:

            time.sleep(1)
            print("\n****************************")
            print("You lost! \U0001F61E")
            print(f"Your word was: {word}\nBetter luck next time!")
            print("****************************\n")
            break

    print(f"Your word is: {' '.join(symbol_letters)}")
    print(f"You already guessed: {', '.join(already_guessed)}")
    print(f"Lives: {'  '.join(lives)}")
    print("****************************")
