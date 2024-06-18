print("\n Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. \n")


var = input("Enter any string : ")
pre=input("Enter the prefix :")
sur=input("Enter the surfix :")

print(var.startswith(pre))
print(var.endswith(sur))