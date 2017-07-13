import base64


def encode(string):
    return base64.b64encode(string)


def decode(string):
    return base64.b64decode(string)


challenge = 'SGVsbG8='
response = decode(challenge)

print 'Base64 encode string %s is %s when decoded.' % (challenge, response)

challenge = encode('Spy Challenge')
response = decode(challenge)

print 'Base64 encode string %s is %s when decoded.' % (challenge, response)
