import sys

def fileLen(fileName):
    with open('./Input/' + fileName  + '.csv') as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

chunk = ''
fileCount = 0

if len(sys.argv) > 1:
    fileName = sys.argv[1]
    if len(sys.argv) > 2:
        size = sys.argv[2]
else:
    fileName = raw_input("Enter a file name: ")
    size = raw_input("Enter a max file size: ")
fileSize = fileLen(fileName)
print('The file has ' + str(fileSize) + ' lines in it.')

with open('./Input/' + fileName + '.csv', 'r') as data:
    for i, each_line in enumerate(data):
        chunk += each_line
        if i == 0:
            header = each_line
        else:
            if i % int(size) == 0:
                path = './Output/' + fileName + str(fileCount) + '.csv'
                newFile = open(path, 'w')
                newFile.write(chunk)
                newFile.close()
                chunk = header
                fileCount += 1
    path = './Output/' + fileName + str(fileCount) + '.csv'
    newFile = open(path, 'w')
    newFile.write(chunk)
    newFile.close()
print('You can find the ' + str(fileCount + 1) + ' files in the Output folder.')
