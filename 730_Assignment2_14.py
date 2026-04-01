'''Write a Python program to swap keys and values in a dictionary'''
dict1={}
n=int(input("Enter total number of key-value pairs in the dictionary: "))
print("Enter all unique keys and value")
for i in range(n):
    key=input("Key: ")
    value=input("Value: ")
    dict1[key]=value
keys=list(dict1.keys())
values=list(dict1.values())
print("The required dictionary with swapped keys and values is: ",dict(zip(values,keys)))