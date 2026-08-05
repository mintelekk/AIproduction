import math
#Order tokens into lists of 100 length.
def chunk(tokens):
    chunks = []
    for i in range(0, len(tokens), 100):
        chunki = []
        for i2 in range(i, min(i+ 100,len(tokens))):
            chunki.append(tokens[i2])
        #Chunks end with index label.
        chunks.append(chunki + [math.floor((i+1)/100)])
    return chunks