# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file = open(filename, "r")
    return file.read()

def count_words():
    text = read_file_content("./story.txt")
    dis_allowed = ['\n','.','?', ',',]
    for char in dis_allowed:
        text = text.lower().replace(char, "")
    text = list(text.split(" "))
    text = [x for x in text if x]
    from collections import Counter
    counts = Counter(text)
    return counts
