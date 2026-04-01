'''Write a recursive function to flatten a nested list (e.g., [1, [2, [3, 4], 5]] - [1, 2, 3, 4, 5])'''

list1=eval(input("Enter a nested list: "))
def flatten(list1,i=0,new_list=[]):
    if i>=len(list1):
        return new_list
    if isinstance(list1[i], list):
        flatten(list1[i], 0, new_list) 
    else:
        new_list.append(list1[i])
    return flatten(list1,i+1,new_list)
print(flatten(list1))