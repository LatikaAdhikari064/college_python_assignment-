print("Write a python program that calculates the factorial of a given number. ")
#n!=n*(n-1)*(n-2)*(n-3)*(n-4).......

num=int(input("Enter any number:"))
fact=1
while(num>0):
    fact=num*fact
    num=num-1
print('factorial of the given number is :',fact)    
