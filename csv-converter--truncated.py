import sys

orders = ''
i = 0
fileCount = 0
if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    fileName = raw_input("Enter a file name: ")
with open('./Input/' + fileName + '.csv', 'r') as data:
    for each_line in data:
        orders += each_line.replace('\n', ',')
        i += 1
        if i >= 500:
            path = './Output/' + fileName + str(fileCount) + '.txt'
            newFile = open(path, 'w')
            newFile.write(orders)
            newFile.close()
            i = 0
            orders = ''
            fileCount += 1
    path = './Output/' + fileName + str(fileCount) + '.txt'
    newFile = open(path, 'w')
    newFile.write(orders)
    newFile.close()
