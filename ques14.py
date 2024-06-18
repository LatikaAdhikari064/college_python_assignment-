print("Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines. ")
txt=open('python.txt','r')
readtxt=txt.readline()
print(readtxt)

while(txt!=" "):
    readtxt_new=txt.readline()
    print(readtxt_new)