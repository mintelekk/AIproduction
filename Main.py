import parser
import cleaner
import tokenizer
import chunker

def main():
    #Tokenize test
    #print(tokenize("Hello, how are you doing today? Can't help you right now."))
    #print(parser.parse('SpaceX cover.docx').text)
    title = 'documents/learntocode.txt'
    title2 = 'documents/SpaceX cover.docx'
    Document1 = parser.parse(title)
    cleaned = cleaner.clean(Document1.text)
    tokenized = tokenizer.tokenize(cleaned)
    chunked = chunker.chunk(tokenized)
    print(chunked)
    
if __name__ == "__main__":
    main()