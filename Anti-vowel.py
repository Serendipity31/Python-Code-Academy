#Remove vowels from a string of letters

word = raw_input("What word would you like de-voweled?")

def anti_vowel(text):
    for t in text:
        if t in "aeiouAEIOU":
           text = text.replace(t, "")
    return text
    
print anti_vowel(word)