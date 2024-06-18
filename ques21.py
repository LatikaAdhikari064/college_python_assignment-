print("Write a python program that counts the occurrences of a specific element in a list.")
lst=[1,2,3,4,"latika","adhikari",1,20,"latika",1,4]
print("list element are :",lst)
element=input("Enter the element you want to count")
c=0
length=len(lst)
while(length>0):
    if(lst[length-1]==element):
        c=c+1
    length=length-1    
print(c)