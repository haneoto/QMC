import os
import codecs
import chardet

def replace_quotes(text):
    count_single_quote = 0
    count_double_quote = 0
    result = ""

    for line in text.split("\n"):
        for char in line:
            if char == "'":
                count_single_quote += 1
                if count_single_quote % 2 == 1:
                    result += "‘"
                else:
                    result += "’"
            elif char == '"':
                count_double_quote += 1
                if count_double_quote % 2 == 1:
                    result += "“"
                else:
                    result += "”"
            else:
                result += char
        result += "\n"

    return result

folder_path = os.getcwd()
file_extensions = ['.txt', '.srt', '.ass', '.ssa', '.vtt', '.lrc']
files_to_convert = [file for file in os.listdir(folder_path) if any(file.endswith(ext) for ext in file_extensions)]

for file_name in files_to_convert:
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'rb') as file:
        raw_data = file.read()
        encoding = chardet.detect(raw_data)['encoding']

    with codecs.open(file_path, 'r', encoding=encoding) as file:
        text = file.read()

    converted_text = replace_quotes(text)

    with codecs.open(file_path, 'w', encoding=encoding) as file:
        file.write(converted_text)

    print(f"Done：{file_name}")
