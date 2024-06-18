print("\n Write a program that copies the contents of one text file to another. \n")

fstfile= open('python.txt','r')
secfile=open('new.txt','w')
for line in fstfile:
    secfile.write(line)
txt=open('new.txt','r')
print(txt.read()) 