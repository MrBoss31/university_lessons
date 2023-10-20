file_name = "myfile.txt"  # Specify the file name
text_to_write = "Привет, !\nЭто вторая строка.\nИ ещё одна строка."

with open(file_name, "w", encoding="UTF-8") as file:
    file.write(text_to_write)

print(f"Файл {file_name} успешно создан и записан.")
print("featured")