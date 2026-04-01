'''Write a recursive function to generate all subsets of a set (power set)'''
set1=eval(input("Enter a set of numbers enclosed by braces separated by , : " ))
def power_set(set1, current=set(),power=[]):
    if not set1:
        power.append(current)
        return power
    elem=next(iter(set1))
    remaining=set1-{elem}
    power_set(remaining,current|{elem},power)
    power_set(remaining,current,power)
    return power
print(power_set(set1))
