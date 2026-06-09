file_path="example.txt"
with open(file_path, "r")as file:
    content=file.read()

words=content.split()
words_count=len(words)
print("total words in",file_path,":",word_count)
