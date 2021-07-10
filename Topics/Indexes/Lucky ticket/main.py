# Save the input in this variable
ticket = int(input())

# Add up the digits for each half
fstHalf = ticket // 1000
half1 = fstHalf % 10
fstHalf //= 10
half1 += fstHalf % 10
fstHalf //= 10
half1 += fstHalf % 10

sndHalf = ticket % 1000
half2 = sndHalf % 10
sndHalf //= 10
half2 += sndHalf % 10
sndHalf //= 10
half2 += sndHalf % 10

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
