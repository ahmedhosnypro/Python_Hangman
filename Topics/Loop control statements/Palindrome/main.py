word = input()

Palindrome = True
for i in range(len(word)):
    if word[i] == word[-(i + 1)]:
        continue
    else:
        Palindrome = False
        break

if Palindrome:
    print("Palindrome")
else:
    print("Not palindrome")
