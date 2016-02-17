#Takes input phrase and censors a particular word within that phrase

'''My Solution. 
This works, but for some reason doesn't pass the CodeAcademy Screen
The error I get is "Oops, try again. Your function fails on censor("hey hey hey","hey"). It returns " *** *** ***" when it should return "*** *** ***"."
So I have no idea what's going on...'''

#ask for the word and phrase to be included
phrase = raw_input("What phrase do you want to censor?")
term = raw_input("What word in that phrase do you want to censor?")

#empty list to hold the individual words in the input phrase
text_lst = []

def censor(text, word):
    text = text.lower()
    word = word.lower()
	# define empty string to show censored phrase
    phrase_censored = ""
    text_lst = text.split()
    for w in text_lst:
        if w == word:
            w = (["*"] * len(word))
            w = "".join(w)
            print w
        phrase_censored = phrase_censored + " " + w
    return phrase_censored
            
print censor(phrase, term) 

'''Here are much more condensed and clever alternatives from the
online CodeAcademy Forum'''

'''First Solution'''
#function taking to str variables as input
#2nd variable is replaced w/asterisks equal to num of char in variable
def censor(text, word):    
    word_length = len(word)    
    new_word = ""

    #determine how many * are needed
    while word_length > 0:
        new_word += '*'
        word_length -=1

    #find the word in the text and replace with asterisk
    return text.replace(word, new_word)


'''Second Solution'''
def censor(text, word):    
    return ("*"*len(word)).join(text.split(word))

print censor("I know they know you know i know you know", "know")

'''Third Solution'''
 def censor(text, word):
    censored_word = "" 
    for wrd in text: 
        if wrd != word: 
            censored_word += wrd 
        else:
            censored_word += "*" * len(word) 
    return censored_word 


'''Fourth (and best) Solution'''
def censor(text, word):
    return text.replace(word,"*" * len(word))