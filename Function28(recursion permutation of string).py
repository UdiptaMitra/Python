# recursion to find permutation of strings
string = input("Enter a string: ")
item_perm=""
perm=[]
def permutation(string, item_perm,perm):
    if len(string)==1:
        item_perm=string
        return [item_perm]
    else:
        result=[]
        for i in range(len(string)):
            firstlet = string[i]
            sub=permutation(string[:i]+string[i+1:],item_perm,perm)
            for j in range(len(sub)):
                temp=firstlet+sub[j]            
                result.append(temp)
    return result
perm=permutation(string,item_perm,perm)
print(set(perm))