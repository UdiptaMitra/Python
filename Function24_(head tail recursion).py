'''head recursion'''
#even after recursion call there are some statements to execute after calling
def head(n):
    if n==0:
        return #0 not print 
    head(n-1) #recursive call occurs first
    print(n) #preocessing occurs after the recursion
head(5)

'''tail recursion'''
#recursion call is the last statement sob statemnet tar aage execute
def tail(n):
    if n==0:
        return #0 not print 
    print(n) #rprocessing occurs first
    tail(n-1) #recursive call is the last step
tail(5)