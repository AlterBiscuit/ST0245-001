from numpy import genfromtxt
from matplotlib import pyplot
from matplotlib.image import imsave
import cv2
import os

original = genfromtxt('./brown-sick-cow-standing-field-260nw-1157826748.csv', delimiter=',')
imsave('original.png', original, cmap='gray')

compressed = genfromtxt('./comprimida.csv', delimiter=',')
imsave('compressed.png', compressed, cmap='gray')

fig = pyplot.figure(figsize=(8, 8))

rows = 1
columns = 2

original_img = cv2.imread('original.png')
original_size = os.path.getsize('original.png') / 1000

compressed_img = cv2.imread('compressed.png')
compressed_size = os.path.getsize('compressed.png')/ 1000

fig.add_subplot(rows, columns, 1)
pyplot.imshow(original_img)
pyplot.axis('off')
pyplot.title("Imagen Original ({:.2f} kb)".format(original_size))

fig.add_subplot(rows, columns, 2)
pyplot.imshow(compressed_img)
pyplot.axis('off')
pyplot.title("Imagen Comprimida ({:.2f} kb)".format(compressed_size))

pyplot.show()
