

for i in range(1, 101):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")  
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    

#Bonus1

user = int(input("Please pick a number 1-10. "))
word = input("Please give me a word to replace the multiple of the word you gave me. ")

for i in range(1, 101):
    if i % user == 0:
        print(word)
    else:
        print(i)


#Bonus Prime(not a success)

num = int
for i in range(1, 101):
    if i > 1:
        for x in range(2, int(i/2)+1):
            if (i % x) == 0:
        else:
            print("prime")
else:
        print(i)




for i in range(1, 101):
    if i 



