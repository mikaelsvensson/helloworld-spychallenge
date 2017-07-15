# coding=utf-8
import codecs
import re
import xml.etree.ElementTree as ET


def sanitize_text(txt):
    return re.sub('\s+', ' ', re.sub(u'[^a-zåäö]', ' ', txt.lower())).strip()


def load_chapters(book_file):
    tree = ET.parse(book_file)
    namespaces = {
        'html': 'http://www.w3.org/1999/xhtml'
    }

    root = tree.getroot()

    chapters = []
    current_chapter = None
    for el in root.findall(".//html:div[@class='generated-style']/*", namespaces):
        if el.tag[-2:-1] == 'h':
            if el.tag.endswith('h1') and el.attrib.has_key('id') and el.attrib['id'].startswith('toc-anchor'):
                current_chapter = []
                chapters.append(current_chapter)
        else:
            all_texts = " ".join(el.itertext())
            if all_texts:
                current_chapter.append(sanitize_text(unicode(all_texts)).split())
    return chapters


def find_word(input_word, chapters):
    for chapter_index, chapter in enumerate(chapters):
        for line_index, line in enumerate(chapter):
            try:
                pos = line.index(input_word)
                return '%d:%d:%d' % (chapter_index + 1, line_index + 1, pos + 1)
            except:
                pass
    return None


translations_words = {}


def translate_word(input_word, chapters):
    if not translations_words.has_key(input_word):
        translation = find_word(input_word, chapters)
        if translation is None:
            print '!!!The word %s does not exist in the book' % input_word
            translation = input_word
        translations_words[input_word] = translation
    return translations_words[input_word]


def encrypt(message, chapters):
    translated_words = []
    input = sanitize_text(message)
    input_words = re.split('\s+', input)
    for input_word in input_words:
        translated_words.append(translate_word(input_word, chapters))

    return " ".join(translated_words)


def decrypt(message, chapters):
    translated_words = []
    input_keys = re.split('\s+', message)
    for input_key in input_keys:
        (chapter_number, paragraph_number, word_number) = re.split(':', input_key)
        word = chapters[int(chapter_number) - 1][int(paragraph_number) - 1][int(word_number) - 1]
        translated_words.append(word)
    return " ".join(translated_words)


chapters = load_chapters('selma-lagerlof-nils-holgerssons-underbara-resa-genom-sverige.xml')

source = codecs.open('input.txt', 'r', encoding='utf8').read().lower()
for message in source.split('\n'):
    print 'Input text:     %s' % message

    encrypted_text = encrypt(message, chapters)
    print 'Encrypted text: %s' % encrypted_text

    decrypted_text = decrypt(encrypted_text, chapters)
    print 'Decrypted text: %s' % decrypted_text

    print
