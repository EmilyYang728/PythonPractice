import  random

number = random.randint(1,100)

guess = 1 # create variable guess

print("a random number is chosen, try guessing it")

guess = int(input("number from 1-100? "))

while guess != number:
                
    if guess < number:
        print("too low")
    elif guess > number:
        print("too high")

    guess = int(input("another guess? "))
        
print("yay u got it")
