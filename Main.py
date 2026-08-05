import parser
import cleaner
import tokenizer
import chunker
import embedding
from pathlib import Path
def main():
    #Tokenize test
    #print(tokenize("Hello, how are you doing today? Can't help you right now."))
    #print(parser.parse('SpaceX cover.docx').text)
    title = 'documents/learntocode.txt'
    title2 = 'documents/SpaceX cover.docx'
    '''
    #Loop through input folder
    documents_folder = Path("documents")

    for file in documents_folder.iterdir():
        if file.is_file():
    '''
    Document1 = parser.parse(title)
    cleaned = cleaner.clean(Document1.text)
    tokenized = tokenizer.tokenize(cleaned)
    chunked = chunker.chunk(tokenized)
    #print(chunked)

    embeddings = embedding.generateEmbedding(chunked)
    print(embeddings[0].shape)
    print(len(embeddings))
if __name__ == "__main__":
    main()