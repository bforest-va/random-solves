import sys

def fileLen(fileName):
    with open('./Input/' + fileName  + '.csv') as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

def jsonStart():
    return "["

def jsonBody(header, chunk):
    return "\n\t{\n\t\t\"" + header + "\": [\n" + chunk[:-2] + "\n\t\t]\n\t},"

def jsonEnd():
    return "\n]"

chunk = ''
json = ''


if len(sys.argv) > 1:
    fileName = sys.argv[1]
    if len(sys.argv) > 2:
        size = sys.argv[2]
else:
    fileName = raw_input("Enter a file name: ")
    size = raw_input("Enter a max array size: ")
fileSize = fileLen(fileName)
print('The csv file has ' + str(fileSize) + ' lines in it.')

with open('./Input/' + fileName + '.csv', 'r') as data:
    for i, each_line in enumerate(data):
        if i == 0:
            header = each_line.replace('\n', '').replace('\r', '')
        else:
            # extra escaped quote to retain 1 set after postman runner strips the other
            chunk += "\t\t\t\"\\\"" + each_line.replace('\n', '').replace('\r', '') + "\\\"\",\n"
            if i % int(size) == 0:
                json += jsonBody(header, chunk)
                chunk = ''
    # will add empty set or error if mod exactly fits
    json += jsonBody(header, chunk)[:-1]
    path = './Output/' + fileName + '.json'
    newFile = open(path, 'w')
    newFile.write(jsonStart() + json + jsonEnd())
    newFile.close()
print('You can find the json file in the Output folder.')
