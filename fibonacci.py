message1 = int(input("How many fibonacci sequence numbers do you want to see? "))


first = 0
second = 1
count = 0

for i in message1:
    print(first, second, end = "")

if message1 <= 0:
    print("Please enter a positive integer please. ")
elif message1 == 1:
    print(first)
else:
    while count < message1:
        print(first)
        sequence = first + second
        second = sequence
        count += 1
        
