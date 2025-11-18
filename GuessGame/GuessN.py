import random

def guess_the_number():

    number = random.randint(1, 100)
    trys = 0

    while True:
        inp = int(input("Try to guess number: "))
        trys += 1

        if inp < number:
            print("The number is bigger")
        elif inp > number:
            print ("The number is lesser")
        else:
            print(f"wow actually you made it in {trys} tries")
            break


guess_the_number()
