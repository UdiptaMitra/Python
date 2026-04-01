'''Write a Python program to find the longest substring in a string without repeating characters'''
'''sample input - abcabcbb'''
string1=input("Enter a string: ")
substr=[]
no_rep=[]
final=[]
max=0
def isEligible(item):
    if len(item)==len(set(item)):
        return True
for i in range(len(string1)):
    for j in range(i,len(string1)):
        substr.append(string1[i:j+1])
for item in substr:
    if isEligible(item):
        no_rep.append(item)
for item in no_rep:
    if max<len(item):
        max=len(item)
for item in no_rep:
    if len(item)==max:
        if item not in final:
            final.append(item)
print("The required list of the longest substring in a entered string without repeating characters is: ",final)
