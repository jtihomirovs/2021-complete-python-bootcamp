import csv

# open the file
data = open('example.csv', encoding='utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

# Print all data
# print(data_lines)

# print row count
print(len(data_lines))

# print 5 lines
for line in data_lines[:5]:
    print(line)

# print 10th row
print(data_lines[10])

# print 10th rows email value
print(data_lines[10][3])

# grab all the emails and append them to a new list
all_emails = []

for line in data_lines[1:15]:
    all_emails.append(line[3])

print(all_emails)

# grab full names - in out data source first names and last names are seperated
full_names = []
for line in data_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])

print(full_names)

# writing
# 'w' - create new file, 'a' - append
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')

# write a single row
csv_writer.writerow(['a', 'b', 'c'])

csv_writer.writerows([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])

# close file
file_to_output.close()
