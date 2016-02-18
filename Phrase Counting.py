#Takes a phrase/list and counts the appearence of an item in that phrase/list
phrase = raw_input("Input:")
word = raw_input("Item to count:")

def count(sequence, item):
    count = 0
    for x in sequence:
        if x == item:
            count = count + 1
    return count

print count(phrase, word)

