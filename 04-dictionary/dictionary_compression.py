# coding=utf-8
import codecs
import csv
import re


# Rules:
#  - The dictionary's first 100,000 words are used.
#  - All input is converted to lower case.
#  - All input is encoded in UTF-8.
#  - Numbers in the input is bad.
#  - Punctuation can be ignored.
#  - Uncommon words (words not in the dictionary) are left unchanged.


def get_common_words(corpus_file):
    common_words = []
    with open(corpus_file) as csvfile:
        reader = csv.DictReader(csvfile,
                                delimiter='\t',
                                quoting=csv.QUOTE_NONE,
                                fieldnames=['word', 'classification', 'baseform', 'status', 'freq_abs', 'freq_rel'])
        for i, row in enumerate(reader):
            common_words.append(unicode(row['word'], 'utf-8').lower())
    return common_words


def encrypt(input, common_words):
    encrypted_text = ''

    input_words = re.split('[\s.:,;\'\"]+', input)
    for input_word in input_words:
        if input_word.strip() == '':
            continue
        if input_word.isdigit():
            print 'Skipping %s because it is already numeric' % input_word
        else:
            try:
                index = common_words.index(input_word)
                encrypted_text += str(index + 1)
            except Exception as e:
                print '!!! Could not find %s amongst the common words' % input_word
                encrypted_text += input_word

        encrypted_text += ' '

    return encrypted_text


def decrypt(input, common_words):
    decrypted_text = ''

    input_words = re.split('\s+', input)
    for input_word in input_words:
        if input_word.isdigit():
            decrypted_text += common_words[int(input_word) - 1]
        else:
            decrypted_text += input_word
        decrypted_text += ' '

    return decrypted_text


common_words = get_common_words('dictionary.txt')

source = codecs.open('sample-data.txt', 'r', encoding='utf8').read().lower();

for message in source.split('\n'):
    print 'Input text:     %s' % message

    encrypted_text = encrypt(message, common_words)
    print 'Encrypted text: %s' % encrypted_text

    decrypted_text = decrypt(encrypted_text, common_words)
    print 'Decrypted text: %s' % decrypted_text

    print
