list_of_students = ["Michele", "Sara", "Cassie"]

name = input("Type name to check: ")
if name in list_of_students:
    print("This student is enrolled.")
else:
    print("There is no such a student")