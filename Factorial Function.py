#Factorial function

#Function
def factorial(x):
    output = x
    while x > 1:
        output = output * (x - 1)
        x = x - 1
    return output

print factorial(4)

#Interactive version
number = raw_input("What number do you want me to calculate the factorial for?")

print factorial(abs(int(number)))

def factorial(x):
    output = x
    while x > 1:
        output = output * (x - 1)
        x = x - 1
    return output
