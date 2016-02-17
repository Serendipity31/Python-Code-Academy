#Function to print string of letters backwards

word = raw_input("What word would you like spelled backwards?")

print reverse(word)

def reverse(text):
    string = ""
    for t in range(0, len(text)):
        letter = text[len(text) - 1 - t]
        string = string + letter
    return string