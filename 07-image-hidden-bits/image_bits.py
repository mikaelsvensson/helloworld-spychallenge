# coding=utf-8

from PIL import Image


def encrypt(image_file_path, message, output_path, channel, is_vertical=False):
    im = Image.open(image_file_path).convert('RGB')
    pix = im.load()

    (width, height) = im.size

    bytes = bytearray(message + '\0')
    print 'Storing %d bits requires %d pixels. Specified image contains %dx%d=%d pixels.' % (
        len(message) * 8,
        len(bytes) * 8,
        width,
        height,
        width * height)
    for i, byte in enumerate(bytes):
        for bit_index in range(0, 8):
            bit = (0x1) & (byte >> bit_index)
            # print 'Bit %d of byte %d is %d' % (bit_index, byte, bit)

            pixel_index = i * 8 + bit_index
            pixel_x = pixel_index / height if is_vertical else pixel_index % width
            pixel_y = pixel_index % height if is_vertical else pixel_index / width
            # print pix[pixel_x, pixel_y]
            (r, g, b) = pix[pixel_x, pixel_y]
            new_color = (
                r if channel != 'red' else (r & 0xFE) + bit,
                g if channel != 'green' else (g & 0xFE) + bit,
                b if channel != 'blue' else (b & 0xFE) + bit)
            pix[pixel_x, pixel_y] = new_color

            # print 'Setting green of pixel %d to %d instead of %d' % (
            #     pixel_index + 1, new_channel_value, old_channel_value)
            # print
    im.save(output_path)


def decrypt(image_file_path, channel, is_vertical=False):
    im = Image.open(image_file_path).convert('RGB')
    pix = im.load()

    (width, height) = im.size

    bytes = []

    for byte_index in range(0, width * height):
        byte = 0
        for bit_index in range(0, 8):
            pixel_index = byte_index * 8 + bit_index
            pixel_x = pixel_index / height if is_vertical else pixel_index % width
            pixel_y = pixel_index % height if is_vertical else pixel_index / width
            (r, g, b) = pix[pixel_x, pixel_y]
            byte = \
                byte | ((r & 0x1) << bit_index) if channel == 'red' else \
                    byte | ((g & 0x1) << bit_index) if channel == 'green' else \
                        byte | ((b & 0x1) << bit_index)
        if byte == 0:
            break;
        else:
            bytes.append(byte)
    # print 'Read %d bytes.' % len(bytes)
    return "".join(map(chr, bytes))


# Source: https://en.wikipedia.org/wiki/Steganography
message = (
    'Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. '
    'The word steganography combines the Greek words steganos , meaning "covered, concealed, or protected", and graphein meaning "writing".'
    'The first recorded use of the term was in 1499 by Johannes Trithemius in his Steganographia, a treatise on cryptography and '
    'steganography, disguised as a book on magic. Generally, the hidden messages appear to be (or be part of) something else: images, '
    'articles, shopping lists, or some other cover text. For example, the hidden message may be in invisible ink between the visible '
    'lines of a private letter. Some implementations of steganography that lack a shared secret are forms of security through obscurity, '
    'whereas key-dependent steganographic schemes adhere to Kerckhoffs\'s principle.')

encrypt('sample-image.png',
        message,
        'encrypted-image.png',
        'blue',
        False)

decrypted_message = decrypt('encrypted-image.png', 'blue', False)

print 'Message to encode into image:'
print message
print
print 'Message decoded from image:'
print decrypted_message
