greeting1 = int(input("How many fibonacci sequence numbers do you want to see? "))


first = 0
second = 1

if greeting1 < 0:
    print(first)
else:
    print(first, second, end = " ")
    for x in range(2, greeting1):
        third = first + second
        print(third, end = " ")
        first = second
        second = third



how_deep = int(input("How deep into the fibonacci sequence would you like to go?"))

x = 0
y = 1
z = y
count = 1

while count <= how_deep:
    print(f"{z} ")
    count += 1
    x, y = y, z
    z = x + y




