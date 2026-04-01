'''## Problem 6: Generate All Subsets Using Bit Masking
Given a set of elements, generate **all possible subsets using bit masking**.
Hint: Use numbers from:
0 to 2^n-1  to represent subsets.'''

s=[]
while True:
    elem=input("Enter an element: ")
    s.append(elem)
    opinion=input("Add more? Y/N: ")
    if opinion !='Y' and opinion!='y':
        break

n=len(s)
for i in range(2**n):
    subset=[]
    for j in range(n):
        if i & (1<<j):
            subset.append(s[j])
    print(subset)