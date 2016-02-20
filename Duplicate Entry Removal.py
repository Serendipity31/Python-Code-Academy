# Falseunction to remove duplicates from a list

#Non-Interactive
def remove_duplicates(x):
    # creates copy of input list
	new = list(x)
	# sorts the copy of the input list
    new.sort()
	# prints to check it's working
    print new
	# creates two empty lists - one for holding duplicate values, 
	# one for holidng the unique values
    dups = []
    unique = []
    for i in range(0, len(new)):
		#if the number in question is any number except the last one
		# then if the number equals the next one in the list, append it
		# to the duplicates list. Otherwise, append it to the unique list
        if i < (len(new) - 1): 
            if new[i] == new[i+1]:
                dups.append(new[i])
            elif new[i] != new[i+1]:
                unique.append(new[i])
        # if the number in question is the last number in the list (i.e. if i == len(new) - 1)
		# then append that number to the unique list, since it is by definition unique at this point
		else: 
            unique.append(new[i])
                    
    # Code academy answer requires simply returning the new list
	return unique
	#My version will return the following sentence
    #return "the duplicate numbers are %s, and the unique numbers are %s" % (dups, unique)
                       
print remove_duplicates([5, 4, 6, 2, 1, 1, 1, 2])

#Interactive Version
string = raw_input("Input a list of numbers - separated by spaces - from which you want the duplicate numbers removed:")

def remove_duplicates(x):
    lst = x.split()
    for l in range(0, len(lst)):
        lst[l] = int(lst[l])
    new = list(lst)
    new.sort()
    print new
    dups = []
    unique = []
    for i in range(0, len(new)):
        if i < (len(new) - 1): 
            if new[i] == new[i+1]:
                dups.append(new[i])
            elif new[i] != new[i+1]:
                unique.append(new[i])
        else: #i == len(new) - 1:
            unique.append(new[i])
                    
    #return unique
    return "the duplicate numbers are %s, and the unique numbers are %s" % (dups, unique)
                    
print remove_duplicates(string)
            