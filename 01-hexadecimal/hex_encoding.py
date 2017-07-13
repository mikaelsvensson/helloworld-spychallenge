def encode(decimal_number):
    return hex(decimal_number)


def decode(hex_string):
    return int(hex_string, 16)


challenge = 'FF'
response = decode(challenge)

print 'Hexadecimal %s is %d in decimal.' % (challenge, response)

challenge = encode(254)
response = decode(challenge)

print 'Hexadecimal %s is %d in decimal.' % (challenge, response)
