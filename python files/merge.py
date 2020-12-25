#C:\Users\surya\Downloads\final_april_may\files

from os import walk
f = []
directory = "C:/Users/surya/Downloads/final_april_may/files"
final_file = "C:/Users/surya/Downloads/final_april_may/files/finalfile.txt"
final_fp =  open(final_file , "a", encoding='utf-8')
files = []
for (dirpath, dirnames, filenames) in walk(directory):
    files = filenames

for file in files:
    file1 = open(directory+"/"+file, "r", encoding='utf-8')
    file_content = file1.read()
    final_fp.write(file_content)
    file1.close()
    # break
final_fp.close()