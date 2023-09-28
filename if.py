#net bonus amount
current_salary = int(input("Please tell me your current salary for our company. "))
year = int(input("How many years have you worked with our company? "))
if year > 5:
     print(f"Becuase you have worked with this company for more than five years, you get a bonus of ${current_salary * .05} ")
else:
     print("I'm sorry, you do not get a bonus. Work with us for more than five years and you will get this bonus.")


#rectangle or square
rectangle_length = (input("What is the length of your rectangle? "))
rectangle_breadth = (input("How wide is your rectangle? "))
if rectangle_length == rectangle_breadth:
    print("I'm sorry, but your rectangle is actually a square")
else:
    print("Congratulations! You have a rectangle!")


#prints greatest
number1 = int(input("Please enter a number "))
number2 = int(input("Please enter another number "))

if number1 > number2:
     print(number1)
else:
     print(number2)

#age

age1 = int(input("How old are you? "))
age2 = int(input("How old are you? "))
age3 = int(input("How old are you? "))


#oldest of the three
if age1 > age2 and > age3:
     print("The oldest person is ")
     print(age1)

if age2 > age1 and > age3:
     print("The oldest person is ")
     print(age2)

if age3 > age1 and > age2:
     print("The oldest person is ")
     print(age3)


#youngest of the three
if age1 < age2 and < age3:
     print("The youngest person is ")
     print(age1)

if age2 < age1 and < age3:
     print("The youngest person is ")
     print(age2)

if age3 < age1 and < age2:
     print("The youngest person is ")
     print(age3)


# student percentage


classes = int(input("How many classes have been held? "))
print(classes)
attendence = int(input("How many of these classes have you attended? "))
print(attendence)
percentage = 100 * classes / attendence
print(percentage)



