from PIL import Image, ImageDraw
import numpy as np
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

im1 = np.array(Image.open("src_0.png").convert("RGB"))  # nie ma deadpoola
im2 = np.array(Image.open("src_1.png").convert("RGB"))  # jest deadpool

mask = np.array(im2)
mask[np.abs(im2-im1) < 1] = 0

box = Image.fromarray(mask).getbbox()

print(box)
hero = mask[box[1]:box[3], box[0]:box[2]]
herosizex, herosizey = (box[3]-box[1], box[2]-box[0])



heroR, heroG, heroB = Image.fromarray(hero).split()
print('herosize:')
print((herosizex, herosizey))
plt.imshow(hero)
mhist = Image.fromarray(hero).histogram(mask=heroR)
mhistA, mhistAbins = np.histogram(hero, bins=255*3)
##########
##########
im = Image.open('img3.png')
print("rozmiar:")
print(im.size)
sizey, sizex = im.size
xjump, yjump = int(herosizex/10), int(herosizey/10)
imA = np.array(im)
value = np.zeros((ceil(sizex/xjump), ceil(sizey/yjump)))
for x in range(0, sizex, xjump):
    for y in range(0, sizey, yjump):
        bmp = imA[x:x+herosizex, y:y+herosizey]
        h, hbins = np.histogram(bmp, bins=255*3)
        r = np.array(h) - np.array(mhistA)
        p = np.dot(r, r)
        value[int(x/xjump), int(y/yjump)] = p

print("Wartosc minimalna bledu: %d", value.min())
posx, posy = np.unravel_index(value.argmin(), value.shape)
print("pozycja:")
print((posx, posy))
draw = ImageDraw.Draw(im)

# Create figure and axes
fig1, ax1 = plt.subplots(1, sharex='col', sharey='row')

# Display the image
ax1.imshow(im)

# Add a Rectangle patch
x1, y1, x2, y2 = (posy*yjump, posx*xjump, posy*yjump+herosizey, posx*xjump+herosizex)
width = x2 - x1
height = y2 - y1
ax1.add_patch(patches.Rectangle((x1, y1), width, height, linewidth=2, edgecolor='green', facecolor='none'))

plt.show()