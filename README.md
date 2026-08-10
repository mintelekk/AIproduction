Retrieval Augmented Generation LLM that is built from scratch without the aid of Auto Complete or Copilot.

Set Up: Activate .venv/Scripts/Activate
Set virtual environment to .venv/Scripts/python.exe  
Add documents/ folder with .docx, .txt or .pdf file textbooks. Then, users can execute data preprocess the files and ask questions.

Step 1: Run Main.py to preprocess the books in documents/ folder
Use the command "python -m pytest tests/test_preprocessing_main.py -v -s" to see the stored SQLite database. Prints out 
Documents:  file name and number of pages.
chunks per document: document # and number of 100 word chunks in database. 

Step 2: Run retriever.py