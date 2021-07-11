nums = []
while True:
    c = input()
    if c == ".":
        break
    else:
        nums.append(int(c))

sum_ = 0
for i in nums:
    sum_ += i

print(sum_ / len(nums))
