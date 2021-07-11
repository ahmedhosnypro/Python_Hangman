import random

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']

secret = random.choice(words)

guessed_secret = secret

p = '-' * len(secret)

print()
print(p)

for i in range(0, 8):
    guess = ''
    if i == 0:
        print("Input a letter ")
        guess = input("Input a letter ")
    else:
        print()
        print()
        print(p)
        print("Input a letter ")
        guess = input()

    if guess in secret:
        while guess in guessed_secret:
            position = guessed_secret.find(guess)
            guessed_secret = guessed_secret.replace(guess, '*', 1)
            new_character = guess
            p = p[:position] + new_character + p[position + 1:]
    else:
        print("That letter doesn't appear in the word")

print()
print("""Thanks for playing!
We'll see how well you did in the next stage""")
