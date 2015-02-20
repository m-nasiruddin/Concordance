# -*- encoding: utf-8 -*-
__author__ = 'Mohammad'


def __file_reader__():
    """function for reading files"""
    corpus = open('data/input/SemCor3.0_all_raw_text.txt', 'r')  # reads the corpus
    return [corpus]


def __concordance_creator__(corpus):
    """function for creating concordance"""
    words_dictionary = {}  # dictionary for all unique words
    lines_dictionary = {}  # dictionary for all lines
    for line in corpus:
        striped_line = line.strip()
        lower_striped_line = striped_line.lower()
        words = lower_striped_line.split()
        for word in words:
            striped_word = word.strip()
            if not striped_word in lines_dictionary:
                lines_dictionary[striped_word] = []  # creates a list for each word
            lines_dictionary[striped_word].append(lower_striped_line)  # puts the lines
    return [lines_dictionary, words_dictionary]


def __concordance_writer__(lines_dictionary):
    """function for writing concordance"""
    for key in sorted(lines_dictionary):
        left_index = 0
        target_index = 0
        right_index = 0
        output_files = open('data/output/' + key + '.csv', 'w')
        for line in lines_dictionary[key]:  # loop for calculating the value of left_index, target_index and right_index
            words = line.split()
            left = words.index(key) - 1
            if left > left_index:
                left_index = left
            target = words.index(key)
            if target > target_index:
                target_index = target
            right_words = len(words) - target - 1
            right = target_index + right_words
            if right > right_index:
                right_index = right
        for line in lines_dictionary[key]:  # loop for generating the concordance
            words = line.split()
            current_target_index = words.index(key)

            left_zeros = target_index - current_target_index
            left_word_index = target_index - left_zeros
            right_zeros = (right_index - left_zeros) - (len(words) - 1)
            right_word_index = len(words) - 1

            for left_zero in range(0, left_zeros):
                output_files.write(';')
            for left_word in range(0, left_word_index):
                output_files.write(words[left_word] + ';')
            output_files.write(key + ';')
            for right_zero in range(0, right_zeros):
                output_files.write(';')
            for right_word in range(current_target_index + 1, right_word_index + 1):
                output_files.write(words[right_word] + ';')
            output_files.write('\n')

        output_files.flush()
        output_files.close()


def main():
    """main function"""
    files = __file_reader__()  # calls the __file_reader__() function
    corpus = files[0]
    concordance = __concordance_creator__(corpus)  # calls the __concordance_creator__() function
    lines_dictionary = concordance[0]
    __concordance_writer__(lines_dictionary)  # calls the __concordance_writer__() function
    print('Successfully finished!')


if __name__ == '__main__':
    main()