#paradigm
letters = ["p", "a", "r", "a", "d", "i", "g", "m"]

for item in letters:
    print(item)

#numbers 0-4
for l in range(5):
    print(l) 

#animals
animals = ["Cat", "Dog", "Tiger", "Cow"]

for item in animals:
    print(item) 

#flowers
flowers = ["Jasmine", "Lotus", "Rose", "Sunflower"]

for item in flowers:
    print(item)
else:
    print("Done")

#Vegetables

list1 = [5, 10, 15, 20]
list2 = ["Tomatoes", "Potatoes", "Carrots", "Cucumbers"]

for i in list1:
    for j in list2:
        print(i,j)

#Vehicles (Help)

vehicles = ["Car", "Cycle", "Bus", "Tempo"]

for item in vehicles:
    if item == "Bus":
        break
    print(item)

#car, cycle, and tempo 

vehicles = ["Car", "Cycle", "Bus", "Tempo"]

for item in vehicles:
    if item == "Bus":
        pass
    continue
print(item)

#counting numbers

numbers = [12, 3, 56, 67, 89, 90, 45]

print(sum(1 for i in numbers))

#adding numbers
numbers2 = [13, 3, 57, 68, 89, 90]
sum = 0

for i in numbers2:
    sum += i

print(sum)

#multiples of 5
numbers3 = [2, 5, 6, 10, 15, 20, 25]

for i in numbers3:
    if (i % 5 == 0):
        print(i) 

#fruit printing

list1 = ['Mango','Banana','Orange']

list2 = list1.copy()

print(list2)

#Max number
number = [1,4,50,80,12]
for i in number:
    print(max(number))
    break

#min number

numbers = [1,4,50,80,12]
for i in number:
    print(min(numbers))
    break

#least to greatest numbers

numbers5 = [1,4,50,80,12]
for i in numbers5:
    print(sorted(numbers5))
    break

#descending numbers

numbers6 = [1,4,50,80,12]
for i in numbers6:
    print(sorted(numbers6, reverse = True))
    break

#multiples of 3
for i in range(3, 21):
    if (i % 3 == 0):
        print(i) 

#multiples of 5, range
for i in range(5,20):
    if (i % 5 == 0):
        print(i)
    
#reverse order 10

for i in reversed(range(11)):
    print(i) 
    