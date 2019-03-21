from downloader import downloadBookRange
from parser import parse_file
from nl_parser_functioned import nltk_parser
import io

number_to_read_in = 500

print("")
print(str(number_to_read_in)+" books requested from web")
print("")

books = downloadBookRange(filesToRetrieve=number_to_read_in)
print("")
print(str(len(books))+" books correctly read from web")
print("")
parsed_books = []

for book in books:
    parsed_book = parse_file(book[1])
    if len(parsed_book) > 0:
        print("#"+str(book[0])+" headers parsed")
        parsed_books.append((book[0],parsed_book))
    else:
        print("#"+str(book[0])+" failed headers parsed")

print("")
print(str(len(parsed_books))+" books correctly parsed headers")
print("")

for parsed_book in parsed_books:
    new_file = 'parsed_books/'+str(parsed_book[0])+'.txt'
    out = io.open(new_file, 'w+', encoding="utf-8")
    for ln in parsed_book[1]:
        out.write(ln + '\n')
    out.close()

#print(parsed_books[3][1])

number_parsed = nltk_parser(parsed_books)

print("")
print(str(number_parsed)+" books added to data set")
print("")
# send through Ben G's parser to get csv

quit()
