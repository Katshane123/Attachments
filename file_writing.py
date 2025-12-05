# Python writing files (.txt , .Json , .csv)

txt_data = "I love pizza actually"

file_path = "output.txt"

with open(file= file_path, mode= "w") as file:
    file.write(txt_data)

    print(F"txt file '{file_path}' has been created")