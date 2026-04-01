'''Write a Python program to print elements of a list along with their indices using the enumerate() function'''
list1=[]
n_list=int(input("Enter total number of elements in the list: "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    list1.append(elem)
print("Index : Element")
for index, value in enumerate(list1):
    print(f"  {index}   :    {value}")
    
'''enumerate() function in Python is used to loop over an iterable and get both the index and the element at the same time. 
It returns an enumerate object that produces pairs in the form (index, element).'''