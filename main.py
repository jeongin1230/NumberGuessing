import random

chance = 5
answer = ''
is_answer = False
random_number = random.randint(1, 100)

while not is_answer:
    print("You have " + str(chance) + " chances left")
    answer = int(input("Enter a number: "))

    if answer == random_number:
        print("Correct! The number is", random_number)
        is_answer = True

    else:
        chance -= 1
        if answer > random_number:
            print("Lower!")
        else:
            print("Higher!")
        print()

    if chance == 0:
        print("You failed! The number is", random_number)
        break



