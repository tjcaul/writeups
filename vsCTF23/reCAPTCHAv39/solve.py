from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def count(img, val):
    x = 0
    for row in img:
        for pixel in row:
            if pixel == val:
                x = x + 1
    return x

def check_around(img, x, y):
    val = img[x][y]
    num = -1
    for xi in range(max(x-1, 0), min(x+2, 200)):
        for yi in range(max(y-1, 0), min(y+2, 200)):
            if img[xi][yi] == val:
                num = num + 1
    return num

def smooth(img, threshold, val):
    new_img = [row[:] for row in img]
    for x in range(0, 200):
        for y in range(0, 200):
            around = check_around(img, x, y)
            if around < threshold and img[x][y] == val:
                new_img[x][y] = 0
            else:
                new_img[x][y] = img[x][y]
    return new_img

def pick(img, val):
    new_img = [row[:] for row in img]
    for x in range(0, 200):
        for y in range(0, 200):
            if img[x][y] == val:
                new_img[x][y] = 255
            else:
                new_img[x][y] = 0
    return new_img

def get_red(img_raw):
    img = []
    for row_raw in img_raw:
        row = []
        for pixel in row_raw:
            row.append(pixel[0])
        img.append(row)
    return img

while True:
    try:
        os.unlink('Unknown.png')
    except:
        pass
    while not os.path.exists('Unknown.png'):
        pass
    img = np.asarray(Image.open('Unknown.png'))
    img2 = get_red(img)
    img3 = pick(img2, 240)
    img4 = smooth(img3, 2, 255)
    #img5 = [[img3[x][y] and img4[x][y] for x in range(0, 200)] for y in range(0, 200)]
    #plt.imshow(img4, cmap='gray')
    #plt.show()
    area = count(img4, 0) / 40000 * 100
    print(area, flush=True)
