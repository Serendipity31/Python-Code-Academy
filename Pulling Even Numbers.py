#Pulls even numbers out of string of numbers 

string = raw_input("Input list with spaces between numbers:")

def purify(lst):
    num = map(int, string.split())
    print num
    evn = [] 
    for x in num:
        if x % 2 == 0:
            evn.append(x)
    return evn

print purify(string)