# Median Function

#Non-Interactive Version
def median(x):
    median = 0
    x.sort()
    print x
    if len(x) % 2 == 0:
        #print len(x) / 2
        #print ((len(x) / 2)- 1)
        #print 9 / float(2)
        median = (x[(len(x) / 2)] + x[((len(x) / 2)- 1)]) / float(2)
        return median
    else:
        median = x[((len(x) - 1) / 2)]
        return median

print median([4, 5, 5, 4])

#Interactive Version
string = raw_input("From what set of numbers - separated by spaces - should the median be calculated?")

def median(x):
    x = x.split()
    #print type(x)
    for l in range(0, len(x)):
        x[l] = int(x[l])
    median = 0
    x.sort()
    print x
    if len(x) % 2 == 0:
        #print len(x) / 2
        #print ((len(x) / 2)- 1)
        #print 9 / float(2)
        median = (x[(len(x) / 2)] + x[((len(x) / 2)- 1)]) / float(2)
        return median
    else:
        median = x[((len(x) - 1) / 2)]
        return median

print median(string)