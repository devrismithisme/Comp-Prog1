 #Controlled statements
car = "Blue"

if car == "Blue":
     print("My car is blue")

car2 = "blue"

if car2 == "Blue" or car2 == "blue":  
     print("My car is blue")

car3 = "Red"  # if it is "Red" it will do the elif. If "Blue" or "blue", then if car3. If empty, it will  print else. 

if car3 == "Blue" or car3 == "blue":  
    print("My car is blue")
elif car3 == "Red" :      # this is an "else if" statement that adds anohter condition
    print("My car is a ferrari")
else:
    print("I just have a bike") # this is an else. it is a default option. 

#Nested IF statements
#nesting is going down one path continuously like a pick your own adventure book.
car_color = "Blue"
car_make = "Tesla"

if car_color == "Blue":
    if car_make == "Tesla":
        print("My car is a Blue Tesla")
    else:
        print("My car is blue")
elif car_color == "Red":
    print("My car is a ferrari")
else:
    print("I just have a bike") #all this is a chain that can be altered based on the car_color and car_make. 

# # # For Loop
# # for i in range(10): #this will count from 0 through 9, not 10
# #     print(i)

# # for i in range(1, 10): # this gives the for loop a start. it will print 1 through 9
# #     print(i) 

# # sports = ["soccer", "basketball", "hockey", "football"]

# # for item in sports:
# #     print(item)   # this makes it to where the items on the list is seperated to there own lines

# # While Loop
# i = 1 #this is global variable becuse not in function or nested
# while i < 6:
#     print("I'm still going") # will print this 5 times
#     i += 1 