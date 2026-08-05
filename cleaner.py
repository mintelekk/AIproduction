import re

def clean(text):
     #Remove punctuation and symbols
    
    #Replace punctuation and quotes
    text1 = text.replace('\"', '').replace('\'', '').replace(',', '').replace('?', '').replace('!', '').replace('.', '')
    #Remove leading and trailing whitespace
    text1 = text1.replace('(', '').replace(')', '').replace(':', '').replace(';', '')
    text1 = text1.strip()
    #Remove multiple new lines
    text1 = re.sub(r'\r\n','\n',text1)
    #Remove multiple spaces
    text1 = re.sub(r" +"," ", text1)
    #Remove multiple tabs or single tabs
    text1 = re.sub(r'\t+',' ',text1)
    #Remove extra white space
    text1 = re.sub(r'\n\s*\n+','\n\n', text1)

    return text1