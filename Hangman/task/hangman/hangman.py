import random

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']

secret = random.choice(words)
not_guessed_secret = secret
attempts = 8
guessed = False

p = '-' * len(secret)

print()
print(p)
i = 0

while attempts > 0 and not guessed:
    # for styling output
    if i == 0:
        guessed_letter = input("Input a letter ")
        i += 1
    else:
        print()
        print()
        print(p)
        guessed_letter = input("Input a letter ")

    if guessed_letter in secret:
        if guessed_letter not in not_guessed_secret:
            attempts -= 1
            print("No improvements")
        while guessed_letter in not_guessed_secret:
            position = not_guessed_secret.find(guessed_letter)
            not_guessed_secret = not_guessed_secret.replace(guessed_letter, '*', 1)
            new_character = guessed_letter
            p = p[:position] + new_character + p[position + 1:]
    else:
        attempts -= 1
        print("That letter doesn't appear in the word")

    if not_guessed_secret == '*' * len(secret):
        guessed = True

if guessed:
    print("""You guessed the word!
You survived!""")
else:
    print("You lost!")
