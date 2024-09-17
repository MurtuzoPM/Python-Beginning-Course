import random

rd = random.randint(1, 9)
guess = 0
c = 0
while guess != rd and guess != "exit":
    guess = int(input("Enter a guess between 1 to 9: "))

    if guess == "exit":
        break

    c += 1

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        print("You took only", c, "tries!")
