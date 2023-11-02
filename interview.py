St1 = "Hello and welcome to your job interview for programming at ________ . My name is Maxwell."
print(St1)

Q1 = input("What is your name? ")
print(f"It's nice to meet you {Q1}. I've taken a look at your resume and it says you have worked in programming for a few years.")

Q2 = int(input("Oddly, you did list how MANY years you have dealt in programming. I was wondering if you could give me this information. "))

if Q2 < 5:
    print("Oh. I am afraid we are only looking for employees who have done programming for 4 or more years. Thank you for coming though.")
    print("If you get more experience in programming and we are still hiring, we might consider setting up another interview with you in the future.")
else:
    print("Wonderful! Your resume also says here that you have worked with a number of programming platforms.")
    Q3 = input("Have you used python before? ")
    if Q3 in "yes" or "Yes":
        print("Here at _______ we work a lot with codes that are similar to python. At the moment we are hiring a few positions.")
    else:
        print("Here at _______ we work quite a lot with codes similar to python so we need to hire people who have experience with this platform.")
        print("Since you do not have the required experience this interview is finished. Thank you and goodbye.")
    Q4 = input("What position are you interesting in having? ")
    if Q4 in "anaylist" or "senior developer" or "Analyst" or "Senior Developer" or "Senior developer":
        print("Great, that is one of the positions we are offering.")
    else:
        print("I am afraid we are not hiring for that position at the moment.")
        Qs1 = input("Is there different position you would be interested in? ")
        if Qs1 in "yes" or "Yes":
            print("Great, that is one of the posotions we are offering.")
        else:
            ("I'm sorry but that is not a position we are hiring for at the moment. The positions we are offfering right now are analyst and senior developer. ")
            Qs2 = input("Would be interessted in either of these positions?")
            if Qs2 in "Yes" or "yes":
                print("Great, let us continue with the interview.")
            else:
                print("I'm sorry we could not satisfy your interests. This interview is over. Thank you and goodbye.")
    Q5 = input(f"How effecient do you think you would be at being a {Q4}?"
    " You can answer in:"
    "1. I might be good at this job because of my amount of experience."
    "2. I do not know for sure but I will try my best.")
                    
        