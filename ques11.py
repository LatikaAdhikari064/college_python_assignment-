print("Write a python program that generates the first n numbers in the Fibonacci sequence. ")
# 0 1 1 2 3 5 8 13 

n=int(input("Enter the number of terms "))
num1=0
num2=1
print(num1)
print(num2)
while(n>0):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3)
    n=n-1
    
    