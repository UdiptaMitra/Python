'''Write a Python program to create a new list containing only even numbers from a given list.'''
list1=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    list1.append(elem)
list2=list(filter(lambda x:x%2==0,list1))
print(list2)
