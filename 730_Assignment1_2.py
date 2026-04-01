''' Problem 2: Set Operations (Using Functions)
Write a Python program that performs various **set operations** on sets entered by the user.
1. Take the elements of **two sets** from the user as input.
2. Perform the following **basic set operations**:
   - Union
   - Intersection
   - Set Difference
   - Symmetric Difference
3. If you are familiar with the concept of **function definition in Python**, implement each operation using **separate functions**.  
4. Each function should:
   - Accept the required sets as parameters
   - Perform the corresponding set operation
   - Return or display the result.
5. Extend the program to perform the following tasks:
      i.  Write a function to check whether one set is a **subset** of another set and whether it is a **superset**.
      ii. Ask the user to enter an element and check whether the element **exists in the given set**.
      iii. Write a function to compute and display the **number of elements** in the set.
      iv. Take a list of elements from the user and convert it into a **set** to remove duplicate values.
      v. Write a function that generates the **power set** (set of all possible subsets) of a given set.'''

# 1. input
print("Enter elements of set 1")
set1=set()
while True:
    elem=int(input("Enter an element in the set: "))
    set1.add(elem)
    opinion=input("Add more? Y/N: ")
    if opinion !='Y' and opinion!='y':
        break

print("Enter elelments of set 2")
set2=set()
while True:
    elem=int(input("Enter an element in the set: "))
    set2.add(elem)
    opinion=input("Add more? Y/N: ")
    if opinion !='Y' and opinion!='y':
        break

print()
#2. operations 3. functions 
def union(set1,set2):
    return set1|set2
def intersection(set1,set2):
    return set1&set2
def set_diff_1(set1,set2):
    return set1-set2
def set_diff_2(set1,set2):
    return set2-set1
def symm_diff(set1,set2):
    return set1^set2

# 4. result
print("The original set 1 is: ",set1)
print("The original set 2 is: ",set2)
print("The union of two sets is: ",union(set1,set2))
print("The intersection of two sets is: ",intersection(set1,set2))
print("The set differrence set1 - set2 is: ",set_diff_1(set1,set2))
print("The set differrence set2 - set1 is: ",set_diff_2(set1,set2))
print("The symmetric difference of two sets is: ",symm_diff(set1,set2))

print()
#5. i. subset superset
def subset_superset(set1,set2):
    if set1.issubset(set2):
        print("Set1 is a subset of set2")
    elif set1.issuperset(set2):
        print("Set1 is a superset of set2")
    else:
        print("Set1 is neither a subset nor a superset of set2")
    if set2.issubset(set1):
        print("Set2 is a subset of set1")
    elif set2.issuperset(set1):
        print("Set2 is a superset of set1")
    else:
        print("Set2 is neither a subset nor a superset of set1")
subset_superset(set1,set2)

print()
#5. ii. check elem
def check(set1,set2):
    elem=int(input("Enter an element to check whether its present in either of the sets: "))
    if elem in set1:
        print("Found in set1")
    elif elem in set2:
        print("Found in set2")
    else:
        print("Not found")
check(set1,set2)

print()
#5. iii. number of elements
def count(set1,set2):
    print("The number of elements in set 1 is: ",len(list(set1)))
    print("The number of elements in set 2 is: ",len(list(set2)))
count(set1,set2)

print()
#5. iv. remove duplicate
def duplicate():
   print("Enter elements of a new list")
   list1=[]
   while True:
      elem=int(input("Enter an element in the list: "))
      list1.append(elem)
      opinion=input("Add more? Y/N: ")
      if opinion !='Y' and opinion!='y':
         break
   print("The new list with removed duplicate elements is: ",list(set(list1)))
duplicate()

print()
#5. v. power set
def power(set1,set2):
    list1=list(set1)
    list2=list(set2)
    power1 = [[]]  
    for elem in list1:
      new_subsets = []
      for subset in power1:
         new_subset = subset + [elem]
         new_subsets.append(new_subset)
      power1 = power1 + new_subsets
    print("The power set of set 1 is: ",power1)
    power2 = [[]]  
    for elem in list2:
      new_subsets = []
      for subset in power2:
         new_subset = subset + [elem]
         new_subsets.append(new_subset)
      power2 = power2 + new_subsets
    print("The power set of set 2 is: ",power2)    
power(set1,set2)