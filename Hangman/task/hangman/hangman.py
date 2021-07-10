import random

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']

secret = random.choice(words)

tip = secret[:3]
length = len(secret) - len(tip)
hyphens = '-' * length

guess = input(f"Guess the word {tip}{hyphens}: ")

if guess == secret:
    print("You survived!")
else:
    print("You lost!")

