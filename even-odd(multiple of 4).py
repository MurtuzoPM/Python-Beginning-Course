number = int(input("Input a number n: "))
if(number%4==0):
    print("The", number,"is a multiple of 4")
elif(number%2==0):
    print("The", number, "is even")
else:
    print("The", number, "is odd")