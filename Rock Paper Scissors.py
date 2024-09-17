import random

options = ["rock", "paper", "scissors"]

user_choice = input("Give me an option(rock, paper, scissors): ")
computer_coice = random.choice(options)
print(computer_coice)

if(user_choice==computer_coice):
    print("It's a tie")
elif(user_choice=="rock" and computer_coice=="scissors")or(user_choice=="scissors" and computer_coice=="paper")or(user_choice=="paper" and computer_coice=="rock"):
    print("You win!")
else:
    print("Computer wins!")


# while True:
#     command = input("Enter your command: ")
#     if(command=="quit"):
#         break
#     else:
#         print("You typed", command)