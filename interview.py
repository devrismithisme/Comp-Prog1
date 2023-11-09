St1 = "Hello and welcome to your job interview for programming at SnupDog. My name is Maxwell."
print(St1)

Q1 = input("What is your name? ")
print(f"It's nice to meet you {Q1}. I've taken a look at your resume and it says you have worked in programming for a few years.")

Q2 = int(input("Oddly, you did not list how MANY years you have dealt in programming. I was wondering if you could give me this information(in a number). "))

if Q2 < 5:
    print("Oh. I am afraid we are only looking for employees who have done programming for 4 or more years. Thank you for coming though.")
    print("If you get more experience in programming and we are still hiring, we might consider setting up another interview with you in the future.")
else:
    print("Wonderful! Your resume also says here that you have worked with a number of programming platforms.")
    Q3 = input("Have you used python before? ")
    if Q3 in "yes" or "Yes":
        print("Here at SnupDog we work a lot with codes that are similar to python. At the moment we are hiring a few positions.")
    else:
        print("Here at SnupDog we work quite a lot with codes similar to python so we need to hire people who have experience with this platform.")
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
    Q5 = int(input(f"How effecient do you think you would be at being a {Q4}? You can answer in: ""1. I might be good at this job because of my amount of experience. ""2. I do not know for sure but I will try my best.""3. I will most likely fail at this job because I have not worked in programming in 60 years.) "))
    if Q5 == 1 or Q5 == 2:    
        print("It IS just a geuss but you have a lot of experience and I do hope you will try your best.")
    else:
        print("That is a really long time since you have done programming. Unfortunately it is not soon enough for us to hire you, thank you for coming though. ")
    Q6 = input("According to the amount of experience you have, I believe you are worth, if we hire you, for $25,000 per year. Do you agree? ")
    if Q6 in "No" or "no":
        print("Really, why?")
    else:
        print("That was a test to see if you would stand up for your abilities. You have failed to see your value and so we cannot hire you. Thank you for coming. Goodbye.")
        exit()
    Q7 = int(input("(Options: 1. I believe I am worth more than $25,000 a year. 2. You are a big fat jerk for thinking I am not worth more money!) "))
    if Q7 == 1:  
        print("I see.")
    else:
        print("That is very rude and unproffesional. We will not handle such language in this company. This interview is finished.")
        exit()
    Q8 = input("How much money do you think you are worth? $")
    print(f"We will have to see if you are worth ${Q8}")
    Q9 = input("Are you interested in health insurance? ")
    if Q9 in "Yes" or "yes":
        print("Our options for healthcare are Google.health(pretty unreliable) and HealthyStealthy(a little more reliable). ")
        Qsstt = input("Which do you choose?(please answer in 'G' or 'HS')? ")
    else:
        print("Okay")
    Q10 = input("Do you have a dog? ")
    if Q10 in "yes" or "Yes":
        print("I love dogs. We sometimes program dog games. They are very fun.")
    else:
        print("Hm...well, we sometimes program dog games so I hope you are at least OK with dogs. ")
print("To recap our interview, we talked about your resume and clarified some points including how long you have been doing computer programming and if you'd worked with python.")
print(f"We also talked about the position you are wanting to be hired into which is {Q4}. You have determined you are worth ${Q8} per year and you would like the {Qsstt} for your healthcare. ")
    

       
        
        

        