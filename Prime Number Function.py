#Prime Number Function (interactive)

number = raw_input("What number do you want checked for prime status?")

print is_prime(int(number))

def is_prime(x):
    if x == 2:
        Print "2 is a prime number. The first prime number in fact."
		return True
    elif x > 2:
        for n in range(2, x):
            if x % n == 0:
                print "There is no remainder when %d is divided by %d. %d is not prime." % (x, n, x)
                return False
        else:
            print "%d is a prime number" % (x)
            return True
    elif x < 2:
        print "%d is not a prime number" % (x)
        return False