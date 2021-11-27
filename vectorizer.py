import re
import numpy as np
import string

dictionary = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'h',
    'ґ': 'g',
    'д': 'd',
    'е': 'e',
    'є': 'ie',
    'ж': 'zh',
    'з': 'z',
    'и': 'y',
    'і': 'i',
    'ї': 'i',
    'й': 'i',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'kh',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shch',
    'ю': 'iu',
    'я': 'ia',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'H',
    'Ґ': 'G',
    'Д': 'D',
    'Е': 'E',
    'Є': 'Ye',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'Y',
    'І': 'I',
    'Й': 'Y',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'Kh',
    'Ц': 'Ts',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Shch',
    'Ю': 'Yu',
    'Я': 'Ya',
    'ь': '',
}


def get_text(filename):
    """Extracts the text from received file and returns it"""
    with open(filename, encoding='utf-8') as file:
        return file.read()


def get_sentences(text):
    """Splits the received text into sentences and returns list of sentences stripped of punctuation and multiple spaces"""
    text = text.replace('\n', '')
    sentences = re.split(r'[.|!|?|…]', text)
    sentences = [s.strip(' ') for s in sentences]
    sentences = [s for s in sentences if len(s) > 0]
    sentences = [''.join([char for char in sentence if char.isalpha() or char.isspace()]) for sentence in sentences]
    sentences = [re.sub('\s+', ' ', sentence) for sentence in sentences]
    return sentences


def get_word_sum(word):
    """Get the word and returns the sum of the serial numbers of their constituent letters of the Latin alphabet"""

    trans_letters = [''.join(dictionary[char]) for char in word]        # get transliterated equivalents of letter
    trans_word = ''.join(trans_letters)                                 # get transliterated words

    word_sum = 0
    latin_alphabet = list(string.ascii_letters)

    for char in trans_word:
        trans_char_number = latin_alphabet.index(char) + 1
        word_sum += trans_char_number
    return word_sum


def vectorizer(filename):
    """Returns a numeric matrix that consists of the sum of the ordinal numbers of the constituent letters
     of the words in the Latin alphabet from the received text"""

    text = get_text(filename).replace('\n', ' ')
    sentences = get_sentences(text)

    # define dimensionality of the matrix
    row_max = max([len(sentence.split(' ')) for sentence in sentences])
    matrix = np.zeros([len(sentences), row_max])

    # divide sentences into words and write the resulting sums into a matrix
    for i, sentence in enumerate(sentences):
        words = sentence.split(' ')
        for j, word in enumerate(words):
            matrix[i, j] = get_word_sum(word)

    # visual display of the matrix
    for row in matrix:
        for val in row:
            print(val, end='  ')
        print('\n')


if __name__ == '__main__':
    vectorizer('text.txt')




