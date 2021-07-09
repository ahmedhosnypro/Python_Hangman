import random

print("H A N G M A N")
print("The game will be available soon.")

words = ['python', 'java', 'kotlin', 'javascript']

secret = random.choice(words)

guess = input()

if guess == secret:
    print("You survived!")
else:
    print("You lost!")

