'''Write a Python program to remove duplicate elements from a list without using the set() function.'''

l1=[]
l1_unique=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    l1.append(elem)
for elem in l1:
    if elem not in l1_unique:
        l1_unique.append(elem)
print("List after removing duplicates:", l1_unique)