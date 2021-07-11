# string = input()
# string = string.replace(string[0], string[0].lower())
# new_string = string
#
# for letter in string:
#     if letter.isupper():
#         new_string = new_string.replace(letter, '_' + letter.lower())
#
# print(new_string)


text = input()
if text.islower():
    print(text)
else:
    out = []
    for c in text:
        if c.islower():
            out.append(c)
        else:
            if text.find(c) == 0:
                out.append(c.lower())
            else:
                out.append("_")
                out.append(c.lower())
    print(''.join(out))
