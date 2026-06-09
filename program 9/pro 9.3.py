file_path="output.txt"

with open(file_path, "a")as file:
    file.write("\n this is a additional line:")
print("content appended to",file_path)
