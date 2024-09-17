weight = int(input("Weight: "))
lbs = 2.2
kgs = 0,453592
convert_weight = input("(L)bs or (K)g: ")
if(convert_weight == "L" or convert_weight == "l"):
    convert_weight = weight * lbs
    print(f"You are {convert_weight} pounds ")
elif (convert_weight == "K" or convert_weight == "k"):
    convert_weight = weight / lbs
    convert_weight = int(convert_weight)
    print(f"You are {convert_weight} kilograms")
else:
    print("Your input is wrong!!!")