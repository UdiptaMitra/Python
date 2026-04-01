'''Write a recursive function to find the product of elements in a list'''
list1=[]
n_list=int(input("Enter total number of elements in the list: "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    list1.append(elem)
print("The original list is: ",list1)
product=1
def product_list(list1,product):
    if len(list1)==0:
        return product
    else:
        product*=list1.pop()
        return product_list(list1,product)
print("The required product is: ",product_list(list1,product))