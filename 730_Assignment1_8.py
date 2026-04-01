'''Problem 8: Password Strength Checker
Write a Python program to check whether a given password is **strong or not** based on the following conditions.

### Password Requirements
A valid password should satisfy the following criteria:
1. The password must contain **at least 8 characters**.
2. The password must contain **at least one uppercase letter** (`A-Z`).
3. The password must contain **at least one lowercase letter** (`a-z`).
4. The password must contain **at least one digit** (`0-9`).
5. The password must contain **at least one special character** from the following set:
! \ @ \ \# \ \$ \ \% \ \^ \ \& \ *

### Task
Write a Python program that:
1. Takes a **password as input from the user**.
2. Checks whether the password satisfies the above conditions.
3. Based on the number of conditions satisfied, classify the password as:
| Conditions Satisfied | Password Strength |
|---------------------|------------------|
| 1-2 conditions | Weak |
| 3-4 conditions | Moderate |
| All 5 conditions | Strong |
### Example
**Input**
Enter Password: P@ss1234
**Output**
Password Strength: Strong'''

# 1. input
password=input("Enter Password: ")
count=0

# 2.  conditions
if len(password)>=8: 
    count+=1
if any(c.isupper() for c in password): 
    count+=1
if any(c.islower() for c in password): 
    count+=1
if any(c.isdigit() for c in password): 
    count+=1
if any(c in "!@#$%^&*" for c in password): 
    count+=1

# 3.classify 
if count<=2:
    print("Password Strength: Weak")
elif count<=4:
    print("Password Strength: Moderate")
else:
    print("Password Strength: Strong")