import random
import string

print("H A N G M A N")


def play():
    # setting variables
    words = ['python', 'java', 'kotlin', 'javascript']  # list of words
    secret = random.choice(words)  # random word
    attempts = 8  # game tries
    guessed_secret = secret  # used to determine which letters guessed in the secret
    guessed_letters = set()  # storing letters which user tried
    guessed = False
    pattern = '-' * len(secret)

    print()
    print(pattern)

    i = 0  # for first try output style
    while attempts > 0 and not guessed:
        if i == 0:
            guess_letter = input("Input a letter ")
            i += 1
        else:
            print()
            print()
            print(pattern)
            guess_letter = input("Input a letter ")

        # check letter requirements
        if len(guess_letter) != 1:
            print("You should input a single letter")
            continue
        if guess_letter not in list(string.ascii_lowercase):
            print("Please enter a lowercase English letter")
            continue

        # playing
        if guess_letter in guessed_letters:
            print("You've already guessed this letter")
        else:
            guessed_letters.add(guess_letter)
            if guess_letter in secret:
                while guess_letter in guessed_secret:
                    position = guessed_secret.find(guess_letter)
                    guessed_secret = guessed_secret.replace(guess_letter, '*', 1)
                    pattern = pattern[:position] + guess_letter + pattern[position + 1:]
            else:
                attempts -= 1
                print("That letter doesn't appear in the word")

        if guessed_secret == '*' * len(guessed_secret):
            guessed = True

    if guessed:
        print("""You guessed the word!
    You survived!""")
    else:
        print("You lost!")


def menu():
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        play()
        return False
    elif choice == 'exit':
        return False
    else:
        return True


while menu():
    pass
