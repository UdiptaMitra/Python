'''Write a Python program to combine two lists into a dictionary using the zip() function'''

n=int(input("Enter total number of elements for the dictionary: "))
print("Enetr key elements (unique)")
key=[]
for i in range(n):
    elem=input("Enter element: ")
    key.append(elem)

print("Enetr value elements")
value=[]
for i in range(n):
    elem=input("Enter element: ")
    value.append(elem)

dict1=dict(zip(key,value))
print("The required dictionary is: ",dict1)