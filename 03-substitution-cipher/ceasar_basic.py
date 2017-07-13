# coding=utf-8

ALPHABET = u'abcdefghijklmnopqrstuvwxyz'


def encrypt(input, offset=1):
    intab = ALPHABET
    outtab = ALPHABET[offset:] + ALPHABET[:offset]

    intab = [ord(char) for char in intab]
    trantab = dict(zip(intab, outtab))

    return input.translate(trantab)


def decrypt(input, offset=1):
    intab = ALPHABET
    outtab = ALPHABET[offset:] + ALPHABET[:offset]

    outtab = [ord(char) for char in outtab]
    trantab = dict(zip(outtab, intab))

    return input.translate(trantab)


challenge = u'dsvvckwwkxc won rygkbn ksuox liqqno qbkmo ryzzob nox pybcdk wynobxk nkdybx'
response = decrypt(challenge)

print 'Challenge: %s' % challenge
print 'Response:  %s' % response

challenge = encrypt(u'tillsammans med howard aiken byggde grace hopper den forsta moderna datorn', 2)
response = decrypt(challenge, 2)

print 'Challenge: %s' % challenge
print 'Response:  %s' % response
