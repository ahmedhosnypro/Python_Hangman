Units = int(input())

if Units >= 1000:
    print("legion")
elif Units >= 500:
    print("swarm")
elif Units >= 50:
    print("horde")
elif Units >= 10:
    print("pack")
elif Units >= 1:
    print("few")
else:
    print("no army")
