"""C-1.25 Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let s try, Mike.", this function would return
"Lets try Mike"."""

def punctuation_remover(object = str):
    removed = ''.join([i for i in object if not 38 < ord(i) < 48 ])
    return removed

x = punctuation_remover("Let's try, Mike.")
print(x)
