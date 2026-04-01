'''Write a recursive function to check if a number is a palindrome without converting to string'''

num=int(input("Enter a number to check whether its palindrome or not: "))
copy=num
def num_pali(num,rev=0):
    if num<=0:
        if rev==copy:
            print("Yes palindrome")
        else:
            print("No palindrome")
    else:
        d=num%10
        rev=rev*10+d
        num_pali(num//10,rev) 
num_pali(num)