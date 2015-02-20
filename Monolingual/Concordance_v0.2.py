__author__ = 'Mohammad'
import re


def __concordance_creator__(corpus):
    """function for creating concordance"""
    words_dictionary = {}  # dictionary for all unique words
    lines_dictionary = {}  # dictionary for all unique lines
    linenumber = 0

    for line in corpus:
        stripline = line.strip()
        lower_stripline = stripline.lower()

        # if not lower_stripline in lines_dictionary:
        # lines_dictionary[lower_stripline] = []
        # lines_dictionary[lower_stripline].append(lower_stripline)

        words = lower_stripline.decode('utf-8').split()
        wordnumber = len(words)  # counts the number of words in each line
        linenumber += 1  # counts the number of lines in the corpus

        for word in words:
            stripword = word.strip()
            lower_stripword = stripword.lower()
            # print(word)

            # if not lower_stripword in words_dictionary:
            #     words_dictionary[lower_stripword] = []
            # words_dictionary[lower_stripword].append(linenumber)

            if not lower_stripword in lines_dictionary:
                lines_dictionary[lower_stripword] = []  # creates a list for each word
            lines_dictionary[lower_stripword].append(linenumber)  # puts the line numbers
            lines_dictionary[lower_stripword].append(wordnumber)  # puts the number of words in a line
            lines_dictionary[lower_stripword].append(lower_stripline)  # puts the lines
    return [lines_dictionary, words_dictionary]


def __file_reader__():
    """function for reading files"""
    corpus = open("data/file.txt", "r")  # reads the corpus
    stopwords = open("data/stopwords.txt", "r")  # reads the stopwords
    punctuations = open("data/punctuations.txt", "r")  # reads the punctuations
    numbers = re.compile(r'^\-?[0-9]+\.?[0-9]*')  # regular expression for numbers
    return [corpus, stopwords, punctuations, numbers]


files = __file_reader__()  # calls the __filereader__() function
corpus = files[0]
stopwords = files[1]
punctuations = files[2]
numbers = files[3]

concordance = __concordance_creator__(corpus)  # calls the __concordancecreator__() function
lines_dictionary = concordance[0]
words_dictionary = concordance[1]
# print("%-15s %5s %s" % ("Word", "Count", "Line Numbers"))
# for key in sorted(wordsdictionary):
# print('%-15s %5d: %s' % (key, len(wordsdictionary[key]), wordsdictionary[key]))

print("%-15s %s %s %s %s" % ("Target", "Count", "[Line,", "Word,", "'Sentence']"))
print("%-15s %s %s %s %s" % ("------", "-----", "------", "-----", "-----------"))
for key in sorted(lines_dictionary):
    print('%-15s %s %s' % (key, len(lines_dictionary[key]), lines_dictionary[key]))
