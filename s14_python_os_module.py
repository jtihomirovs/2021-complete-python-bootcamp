import os

# f = open('practice.txt', 'w+')
# f.write('This is a test string')
# f.close()
print(os.getcwd())
print(os.listdir())
print(os.listdir('C:\Python'))
# shutil.move('practice.txt', 'C:\\Users\\Juris\\Desktop\\test')
# shutil.move('C:\\Users\\Juris\\Desktop\\test\\practice.txt', os.getcwd())

# send2trash.send2trash('practice.txt')

file_path = 'C:\\Users\\Juris\\Desktop\\Python_folder'
for folder, sub_folders, files in os.walk(file_path):
    print(f'Currently looking at {folder}')
    print('\n')
    print('The subfolders are: ')
    for sub_folder in sub_folders:
        print(f'\t Subfolder: {sub_folder}')

    print('\n')
    print('The files are: ')
    for f in files:
        print(f'\t File: {f}')
    print('\n')
