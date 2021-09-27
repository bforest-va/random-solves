import re
import sys

formatedJSON = ''
if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    fileName = input('Enter a file name: ')
with open('./Input/' + fileName, 'r', encoding='utf-8') as data:
    for each_line in data:
        if (re.search('{\n', each_line) or re.search('},\n', each_line) or re.search('}\n', each_line) or re.search(']\n', each_line) or '"articles":' in each_line or '"id":' in each_line) and '"body":' not in each_line:
            formatedJSON += each_line
        elif '"title":' in each_line:
            formatedJSON += each_line[:-2] + '\n'
    newFile = open('./Output/' + fileName, 'w', encoding='utf-8')
    newFile.write(formatedJSON)
    newFile.close()
