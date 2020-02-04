# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# 
# Examples
# pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
# pigIt('Hello world !');     // elloHay orldway !

import re

def pig_it(text):
    words = text.split()
    result = []
    for word in words:
        if re.match("^[a-zA-Z_]*$", word):
            result.append(word[1:] + word[0] + 'ay')
        else:
            result.append(word)
    return " ".join(result)
