'''Write a recursive function to perform binary search on a sorted list'''

list1=eval(input("Enter a sorted list: "))
target=int(input("Enter an element to search for: "))

def binary(list1,low,high):
    mid=(high+low)//2
    if low>high:
        return False
    if target==list1[mid]:
        return True
    elif target<list1[mid]:
        return binary(list1,low,mid-1)
    elif target>list1[mid]:
        return binary(list1,mid+1,high)
if binary(list1,0,len(list1)):
    print("found")
else:
    print("not found")