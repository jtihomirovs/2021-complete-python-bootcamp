import csv
import re

import PyPDF2

# Task 1
# open the file
data = open('find_the_link.csv', encoding='utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

n = 0
link = []
for line in data_lines:
    link.append(line[n])
    print(line[n])
    n += 1

print(''.join(link))

# Task 2
f = open('Find_the_Phone_Number.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(f)

# pattern = r'\d{3}.\d{3}.\d{4}'
#
# for num in range(pdf_reader.numPages):
#     page = pdf_reader.getPage(num)
#     page_text = page.extractText()
#     match = re.search(pattern, page_text)
#
#     if match:
#         print(match.group())

pattern = r'\d{3}'

all_text = ''

for n in range(pdf_reader.numPages):
    page = pdf_reader.getPage(n)
    page_text = page.extractText()

    all_text = all_text + ' ' + page_text

for match in re.finditer(pattern, all_text):
    print(match)

# <re.Match object; span=(41808, 41811), match='505'>
# So its located somewhere there 41790:41898+20
print(all_text[41790:41898 + 20])

# Lets find exact match
pattern_precise = r'\d{3}.\d{3}.\d{4}'
for match in re.finditer(pattern_precise, all_text):
    print(match)
