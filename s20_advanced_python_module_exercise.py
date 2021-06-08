import os
import re

file_path = 'C:\\Python\\Examples\\unzip_me_for_instructions\\extracted_content'


def search_phone(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    content = f.read()

    if re.search(pattern, content):
        return re.search(pattern, content)
    else:
        return ''


results = []
for folder, sub_folders, files in os.walk(os.getcwd() + "\\unzip_me_for_instructions\\extracted_content"):
    for f in files:
        full_path = folder + '\\' + f
        results.append(search_phone(full_path))

for r in results:
    if r != '':
        print(r.group())
