print("Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result. ")
num1=int(input("Enter your first  number :"))
num2=int(input("Enter your second number :"))
operation=input("Enter the operation you want to perform :")

if(operation=="+"):
    print("summation of two number is :",num1+num2)
elif(operation=="-"):    
        print("subtraction of two number is :",num1-num2)
elif(operation=="*"):    
        print("multiplication of two number is :",num1*num2)
elif(operation=="-"):    
        print("Division of two number is :",num1/num2)
else:
    print("You have enters a wrong operation")                