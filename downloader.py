import requests
from urllib import request


startNum = 1000
filesToRetrieve = 5
curFile = startNum

while curFile < startNum + filesToRetrieve:

    filename = str(curFile) + '.txt'
    filepath = 'books/' + filename
    url = 'http://www.gutenberg.org/files/' + str(curFile) + '/' + filename
    url2 = 'http://www.gutenberg.org/files/' + str(curFile) + '/' + str(curFile) + '-0.txt'

    r = requests.get(url)
    if r.status_code == 200:
        with open(filepath, 'w') as f:
            f.write(r.text)
        print('Book #' + str(curFile) + ' retrieved.')
    else:
        r = requests.get(url2)
        if r.status_code == 200:
            with open(filepath, 'w') as f:
                f.write(r.text)
            print('Book #' + str(curFile) + ' retrieved (using ' + str(curFile) + '-0.txt).')
        else:
            print('Book #' + str(curFile) + ' failed: ' + str(r.status_code))
    curFile += 1



    #print(r.text)

