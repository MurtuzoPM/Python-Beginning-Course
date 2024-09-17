num = int(input("Input a number n: "))
check = int(input("The number to divide by num"))
if(num%4==0):
    print("The", num,"is a multiple of 4")
elif(number%2==0):
    print("The", num, "is even")
else:
    print("The", num, "is odd")
    
if(num%check==0):
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)