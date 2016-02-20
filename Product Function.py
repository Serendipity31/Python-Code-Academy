#Function that returns product of numbers

#Non-interactive Version
def product(x):
    total = 1
    for i in range(0, len(x)):
        total = total * x[i]
    return total

print product([4, 5, 5])

#Interactive Version
'''This version takes a string of numbers separated by spaces,
turns them into a list of integers, and multiplies them together.'''

string = raw_input("Input a list of numbers - separated by spaces - that you want multiplied:")

def product(x):
    lst = x.split()
    for l in range(0, len(lst)):
        lst[l] = int(lst[l])
    total = 1
    for i in range(0, len(lst)):
        total = total * lst[i]
    return "The product of your numbers is: %d" % (total)
    #return total

print product(string)
