import random
wordlist = []
f =open("sowpods.txt","r")
for I in f:
    wordlist.append(I)
print (random.choice(wordlist))         
