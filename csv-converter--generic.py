import sys

if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    fileName = raw_input("Enter a file name: ")
reformated = ''
with open('./Input/' + fileName + '.csv', 'r') as data:
    for each_line in data:
        reformated += each_line.replace('\n', ',').replace('\r', '')
    path = './Output/' + fileName +'.txt'
    newFile = open(path, 'w')
    newFile.write(reformated)
    newFile.close()
