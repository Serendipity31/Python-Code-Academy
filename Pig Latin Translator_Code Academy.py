#Pig Latin Translator from CodeAcademy

yg = 'ay'
name = raw_input('What is your name?')
greeting = 'Hi, ' + name + '!'
#welcome = greeting + name + '!'
print greeting

original = raw_input('Enter a word, ' + name + ':')

if len(original) > 0 and original.isalpha():
    #print original
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)] + first + pyg
    print "Great, %s! your word in pig latin is: " % (name) + new_word 
else:
    print 'empty'