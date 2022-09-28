import random
for counter in range(2, 20, 3):
    print(counter)
    print("Hello, world!")

for letter in "Hello, world!":
    print(letter)


loop_counter = 0
while random.randrange(0, 100) < 80:
    # until it reacehs a number not less than 80, its going to keep going and printing the statement.
    print("Hello, world!")
    loop_counter += 1
print("Looped", loop_counter, "times")

i = 0
while i < 3:
    print(i)
    i += 1

s = "Hello, world!"
i = 0
while i < len(s):
    print(s[i])
    i += 1
