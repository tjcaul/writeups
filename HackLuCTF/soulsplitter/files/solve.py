import zlib
import sys
import base64
import pprint
from PIL import Image
import cv2
from pyzbar.pyzbar import decode
import subprocess

BLOCK_FULL  = chr(9608)
BLOCK_UPPER = chr(9600)
BLOCK_LOWER = chr(9604)
BLOCK_EMPTY = chr(160)

def render(code):
    code = [not x for x in code]
    code = [code[31 * i + 1 : 31 * i + 30] for i in range(1, 31)]
    for i in range(0, len(code) - 1, 2):
        for j in range(len(code[i])):
            if i + 1 == len(code):
                if code[i][j]:
                    print(BLOCK_UPPER, end='')
                else:
                    print(' ', end='')
            else:
                if code[i][j] and code[i+1][j]:
                    print(BLOCK_FULL, end='')
                elif code[i][j]:
                    print(BLOCK_UPPER, end='')
                elif code[i+1][j]:
                    print(BLOCK_LOWER, end='')
                else:
                    print(' ', end='')
        print()
    print()

app = subprocess.Popen(['/usr/bin/nc', 'flu.xxx','10120'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

template = Image.open('template.bmp')
template = list(template.getdata())

print(app.stdout.readline())
print(app.stdout.readline())

while True:
    header = app.stdout.readline()
    try:
        numshards = int(header[11:13])
    except:
        print(header)
        print(app.stdout.readline())
        exit(0)


    code = [[False] * 29 for i in range(29)]

    for i in range(numshards):
        line = app.stdout.readline()
        data = base64.b64decode(line)
        data = zlib.decompress(data)
        data = str(data, encoding='utf-8')
        data = data.split('\n')

        for row, line in enumerate(data):
            for col, char in enumerate(line):
                if char == BLOCK_FULL or char == BLOCK_UPPER:
                    code[row * 2][col] = not code[row * 2][col] 
                if (char == BLOCK_FULL or char == BLOCK_LOWER) and row + 1 != len(data):
                    code[row * 2 + 1][col] = not code[row * 2 + 1][col] 

    flat = [True] * 31
    for row in code:
        flat += [True] + [not x for x in row] + [True]
    flat += [True] * 31

    flat = [flat[i] and template[i] for i in range(len(flat))]

    render(flat)

    img = Image.new("1", (31, 31), "white")
    img.putdata(flat)
    img.save('img.png')

    qrcode_img = 'img.png'
    img = cv2.imread(qrcode_img)
    decoded_data = decode(img)
    if len(decoded_data) != 0:
        decoded = decoded_data[0].data.decode()
        app.stdin.write(decoded + '\n')
        app.stdin.flush()
        print(decoded)
    else:
        print('Error scanning.')
        exit(1)

    print(app.stdout.readline())
