link = input().split("\\")
file = link[-1]
file_name, file_extension = file.split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")