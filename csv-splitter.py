import sys

def fileLen(fileName):
    with open('./Input/' + fileName  + '.csv') as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

half = ''

if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    fileName = raw_input("Enter a file name: ")
fileSize = fileLen(fileName)
print('The file has ' + str(fileSize) + ' lines in it.')
path = './Output/' + fileName + '_0' + '.csv'

with open('./Input/' + fileName + '.csv', 'r') as data:
    for i, each_line in enumerate(data):
        if i == 0:
            header = each_line
        half += each_line
        if i == fileSize // 2:
            newFile = open(path, 'w')
            newFile.write(half)
            newFile.close()
            half = header
            path = './Output/' + fileName + '_1' + '.csv'
    newFile = open(path, 'w')
    newFile.write(half)
    newFile.close()
