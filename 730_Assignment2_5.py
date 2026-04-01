'''Write a Python program to traverse a tuple and count how many elements are even numbers.'''
list1=[]
n_list=int(input("Enter total number of elements in the tuple: "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    list1.append(elem)
tuple1=tuple(list1)
count=0
for i in range(len(tuple1)):
    if tuple1[i]%2==0:
        count+=1
print("The number of even elements is: ",count)
