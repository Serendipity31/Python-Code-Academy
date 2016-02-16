#Function that sums the digits within a (positive) number

#Simple way
def digit_sum(n):
    string = str(n)
    total = 0
    for i in string:
        total += int(i)
    return total

print digit_sum(40)

#Challenging way
def digit_sum(n):
    digit = n % 10
    while n > 0:
        n = n // 10
        digit = digit + n % 10
    return digit
 
print digit_sum(4343)

#Interactive way
number = raw_input("Please input an integer.")

print digit_sum(abs(int(number)))

def digit_sum(n):
    digit = n % 10
    while n > 0:
        n = n // 10
        digit = digit + n % 10
    return digit