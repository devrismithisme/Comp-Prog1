sentence1 : int(input("Give me a number please "))
sentence2 : int(input("Give me another number please ")) 
sentence3 : int(input("Would you like to add, subtract, multiply, or divide? "))

if sentence3 in ["add"]:
    print("Your answer is ")
    print(sentence1 + sentence2)

if sentence3 in ["subtract"]:
    print("Your answer is ")
    print(sentence1 - sentence2)

if sentence3 in ["multiply"]:
    print("Your answer is ")
    print(sentence1 * sentence2)

if sentence3 in ["divide"]:
    print("Your answer is ")
    print(sentence1 / sentence2)








#notes
def print_my_name():
    print("name")

print_my_name('Bob')

def trip_planner(start, end, duration, mode):
    print(f"It looks like you are starting your trip from {start}")
    print(f"You are planning to go to {end}")
    print(f"It shoulld take you about{duration} hours.")
    print(f"I see you are traveling by {mode}")

trip_planner("Paradigm", "Salt Lake City", 9, "bike")


def trip_planner(start, end, duration, mode = "car"):      # this is a default and will run as the mode being "car". 
    print(f"It looks like you are starting your trip from {start}")
    print(f"You are planning to go to {end}")
    print(f"It shoulld take you about{duration} hours.")
    print(f"I see you are traveling by {mode}")

trip_planner("Paradigm", "Salt Lake City", 9, "bike") # it will not run as "bike". it will run as the default, "car". 