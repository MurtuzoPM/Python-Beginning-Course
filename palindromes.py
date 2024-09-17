string = input("Give me a word: ")
string = str(string)
reverse = string[::-1]
print(reverse)
if string==reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")