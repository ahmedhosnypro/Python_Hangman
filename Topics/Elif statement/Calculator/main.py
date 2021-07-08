fst_num = float(input())
snd_num = float(input())
operation = input()

division = ["/", "mod", "div"]

if operation == "+":
    print(fst_num + snd_num)
elif operation == "-":
    print(fst_num - snd_num)
elif operation == "*":
    print(fst_num * snd_num)
elif operation == "pow":
    print(pow(fst_num, snd_num))
elif operation in division:
    if snd_num == 0:
        print("Division by 0!")
    else:
        if operation == "/":
            print(fst_num / snd_num)
        elif operation == "mod":
            print(fst_num % snd_num)
        elif operation == "div":
            print(fst_num // snd_num)
