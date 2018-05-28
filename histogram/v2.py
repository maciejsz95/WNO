from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import feature

def img_plot(x, y, obraz, z):
    if(z==0):
        ax[x, y].imshow(obraz)
        ax[x, y].axis("off")
    else:
        ax[x, y].imshow(obraz, cmap=plt.cm.gray)
        ax[x, y].axis("off")

def hist_plot(x, y, kolor, ilosc, pixele, z):
    if(z==0):
        ax[x, y].plot(kolor, ilosc / pixele)
    else:
        ax[x, y].plot(kolor, ilosc / pixele, 'k')

# rysowanie wykresow
fig, ax = plt.subplots(2, 3)

# otworzenie obrazu
obraz = Image.open("il.jpg")
obraz_dane = np.array(obraz)

ax[0, 0].set_title("Oryginalny obraz")
img_plot(0, 0, obraz, 0)

# przypisanie odpowiednich wartosci RGB
czerwony, czerw_ilosc = np.unique(obraz_dane[:, :, 0], return_counts=True)
zielony, ziel_ilosc = np.unique(obraz_dane[:, :, 1], return_counts=True)
niebieski, nieb_ilosc = np.unique(obraz_dane[:, :, 2], return_counts=True)

# obliczenie liczby pikseli, do znormalizowania histogramu
width, high = obraz.size
ilosc_pixeli = width * high

ax[1, 0].set_title("Histogram RGB")
hist_plot(1, 0, czerwony, czerw_ilosc, ilosc_pixeli, 0)
hist_plot(1, 0, zielony, ziel_ilosc, ilosc_pixeli, 0)
hist_plot(1, 0, niebieski, nieb_ilosc, ilosc_pixeli, 0)

# Model YUV
szary_czerwony = np.array(obraz)[:, :, 0] * 0.299
szary_zielony = np.array(obraz)[:, :, 1] * 0.587
szary_niebieski = np.array(obraz)[:, :, 2] * 0.114
skala_szarosci = szary_czerwony + szary_zielony + szary_niebieski

szary, szar_ilosc = np.unique(skala_szarosci, return_counts=True)

ax[1, 1].set_title("Histogram odcieni szarosci")
hist_plot(1, 1, szary, szar_ilosc, ilosc_pixeli, 1)

szary_obraz = Image.fromarray(skala_szarosci)

ax[0, 1].set_title("Obraz czarno-biały")
img_plot(0, 1, szary_obraz, 0)

# Canny
canny = feature.canny(skala_szarosci, sigma=10)

ax[0, 2].set_title("Canny")
img_plot(0, 2, canny, 1)

# Krzyż Robertsa
in_im_x_y = np.delete(np.delete(skala_szarosci, 1, axis=0), 1, axis=1)
in_im_x1_y1 = np.delete(np.delete(skala_szarosci, -1, axis=0), -1, axis=1)

in_im_x1_y = np.delete(np.delete(skala_szarosci, 1, axis=0), -1, axis=1)
in_im_x_y1 = np.delete(np.delete(skala_szarosci, -1, axis=0), 1, axis=1)

tmp1 = in_im_x_y - in_im_x1_y1
tmp2 = in_im_x1_y - in_im_x_y1
krzyz = np.abs(tmp1) + np.abs(tmp2)

ax[1, 2].set_title("Krzyż Robertsa")
img_plot(1, 2, krzyz, 1)


plt.show()
