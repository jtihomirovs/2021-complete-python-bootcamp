import shutil
import zipfile

f = open('fileone.txt', 'w+')
f.write('One file')
f.close()

f = open('filetwo.txt', 'w+')
f.write('Two file')
f.close()

# This approach work just with entire file

comp_file = zipfile.ZipFile('compfile.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('compfile.zip', 'r')
zip_obj.extractall('extracted_content')

# This approach work with entire folder
dir_to_zip = 'C:\\Python\\Examples\\extracted_content'

output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)

shutil.unpack_archive('example.zip', 'final_unzip', 'zip')
