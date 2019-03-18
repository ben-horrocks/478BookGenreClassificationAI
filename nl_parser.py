import nltk

stopwords = set(nltk.corpus.stopwords.words('english'))
most_common_english_words = [w for w in nltk.word_tokenize(open('most_common.txt', 'r').read()) if not w in stopwords]

file = 'parsed_books/parsedexample.txt'
f = open(file, 'r').read()

# nltk Tokenization
words_with_punctuation = nltk.word_tokenize(f)
words = list(word.lower() for word in words_with_punctuation if word.isalpha())
sentences = nltk.sent_tokenize(f)

# Word Count
total_word_count = len(words)

# Average Words Per Sentence
average_words_per_sentence = total_word_count / len(sentences)

# Average Word Length
total_char_count = 0
for word in words:
    total_char_count += len(word)
average_word_length = total_char_count / len(words)

# Common Words
words_without_stopwords = [w for w in words if not w in stopwords]
frequency_distribution = nltk.FreqDist(words_without_stopwords)
most_common_words_distribution = dict(frequency_distribution.most_common(1000))
most_common_words_in_book = {}
for word in most_common_english_words:
    word = word.lower()
    if word in most_common_words_distribution:
        most_common_words_in_book[word] = round(most_common_words_distribution[word] / float(total_word_count), 8)
    else:
        most_common_words_in_book[word] = 0

# Create .arff file
output_arff = '''@RELATION genres

@ATTRIBUTE word_count numeric
@ATTRIBUTE words_per_sentence numeric
@ATTRIBUTE average_length_of_word numeric'''

for common_word in most_common_english_words:
    output_arff += ('\n@ATTRIBUTE {} numeric'.format(common_word))

output_arff += '''
@ATTRIBUTE genre { fiction, non-fiction }

@DATA
'''

output_arff += '{},{},{}'.format(
    total_word_count,
    average_words_per_sentence,
    average_word_length)

for word, word_freq_percent in sorted(most_common_words_in_book.iteritems()):
    output_arff += ',{}'.format(word_freq_percent)

output_arff += ',fiction\n'
output_filename = 'example.arff'

fp = open(output_filename, "w")
fp.write(output_arff)
