import random

print(random.random())

random.seed(20)
print(random.random())

print(random.uniform(5, 9000))

print(random.randint(5, 9000))

print(random.choice("Voldemort"))

print(random.randrange(3, 100, 5))
print(random.randrange(1, 5))
print(random.randrange(100))

tiny_list = ['a', 'apple', 'b', 'banana', 'c', 'cat']
random.shuffle(tiny_list)
print(tiny_list)

print(random.sample(range(100), 3))
