print("Write a python program that returns the minimum and maximum values in a list of numbers. ")

lst=[1,22,3,44,55,66,7]
length=len(lst)
print("length of the string is :",length)
min=lst[0]
max=lst[0]
for i in range(1,length):
    if(min>lst[i]):
        min=lst[i]
    if(max<lst[i]):
        max=lst[i]
        
print("Maximum number in the list is :",max,"Minimum number in the list is",min)    
    