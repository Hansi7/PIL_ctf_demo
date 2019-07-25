f = open('256x256.txt', 'r')
str = f.read()
f.close()

import base64

ok = base64.b64decode(str)
ok_str = ok.decode()

from PIL import Image

image = Image.new('RGB', size=(256, 256))
for row in range(256):
    for col in range(256):
        index_n = row * 256 + col
        if (ok_str[index_n] == '1'):
            image.putpixel((row, col), (0, 0, 0, 1))
        else:
            image.putpixel((row, col), (222, 222, 222, 1))

image.save('ascii_art_output.jpg')
