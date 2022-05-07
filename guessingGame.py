import random

list1 = [1,2,3,4,5,6,7,8,9]
number = random.choice(list1)
guess = int(input("Enter Your Choice:"))

chances = 0
while chances<5:
    
    if guess == number:
        print("Your is right")
        chances+=1
        break
    elif guess > number:
        print("Yout guess is higher")
        chances+=1
        break
    else:
        print("Your guess is lower")
        chances+=1
        break
if chances == 5:
    print("You lost!!", number)


