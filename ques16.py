print("Write a program in python that counts the frequency of each character in a string.")

string=input("Enter a string :")
character=input("Enter an character yiou want to find in a string  :")

# by creating a function 
count=0
for i in string:
    if(i==character):
        count=count+1
print(count)        



# with  the help of a function 
print(string.count(character))