my_name = "Devri Anne Smith"
test_score = 9/10
was_lunch_tasty = True
Bday_classes = ["Math Kedge", "11th Seminar", "Computer Programming", "Math 3"]

print(f"Hi, my name is {my_name}. I scored {test_score} on my last test in Computer Programming. My classes today are {Bday_classes}.")

print(f"I had chicken and rice for lunch today and it is {was_lunch_tasty} that lunch was tasty.")

print("My name is {my_name} and I am very tired because I worked very har to study for my test. I got {test_score}.")


def add_two_numbers(num1, num2):
    print(num1 + num2)

add_two_numbers(52, 94)


def add_two_numbers():
    print(5 + 3)

add_two_numbers()


def add_two_numbers2(num1, num2):
    print(num1 + num2)

user_number1 = int(input("Give me a number please: "))
user_number2 = int(input("Give me a second number please: "))

add_two_numbers2(user_number1, user_number2)

