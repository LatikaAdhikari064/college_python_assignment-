print("Write a python program that calculates the sum of the digits of a given number.")
num=int(input("Enter a number :"))
strr=str(num)
s=0
for i in strr:
    s=s+int(i)
print("sum of all the digits in a string is :",s )    