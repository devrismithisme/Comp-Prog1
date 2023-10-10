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



    
