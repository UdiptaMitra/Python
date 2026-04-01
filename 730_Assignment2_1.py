'''Write a Python program to iterate over a list and print all its elements.'''

list1=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    list1.append(elem)
print("The elements are: ")
for i in range(len(list1)):
    print(f"Element {i+1} - {list1[i]}")
    
    
