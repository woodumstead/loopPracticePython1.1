fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        break
    print(x)

fruits = ['apple', 'banana', 'cherry']
    for x in fruits:
         if x == 'cherry':
            break
        print(x)

fruits = ['apple', 'banana', 'cherry']
    for x in fruits:
        if x == 'apple':
            break
        print(x)

# within a range
for x in range (2, 9):
    print(x)

# Nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# pass statement for error handling
for x in [1, 5, 4]:
    pass


# While loops
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


i = 0 
while i < 6:
     i =+ 1
     if i == 3:
        continue
    print(i)

i = 0 
while i < 6;
    print(i)
    i += 1
else:
    print('< 6 now   8| ')