cafe = ''
max_ = 0
while True:
    in_ = input()
    if in_ == "MEOW":
        break
    else:
        list_ = in_.split(' ')
        if int(list_[1]) > max_:
            cafe = list_[0]
            max_ = int(list_[1])

print(cafe)
