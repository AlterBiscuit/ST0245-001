import numpy as np

SQUARE_AREA = 3

img_input ="./brown-sick-cow-standing-field-260nw-1157826748.csv"
img_data = np.genfromtxt(img_input, delimiter=',')

img_height = len(img_data)
img_width = len(img_data[0])

compressed_data = np.genfromtxt(img_input, delimiter=',')

for i in range(int(img_height / SQUARE_AREA)):
    for j in range(int(img_width / SQUARE_AREA)):
        i_from, i_to = i*SQUARE_AREA, (i*SQUARE_AREA)+SQUARE_AREA
        j_from, j_to = j*SQUARE_AREA, (j*SQUARE_AREA)+SQUARE_AREA
        square_data = img_data[i_from:i_to, j_from:j_to]

        square = np.reshape(square_data, (SQUARE_AREA, SQUARE_AREA))

        nearestNeighbour = square[0, 0]

        if SQUARE_AREA > 1:
          nearestNeighbour = square[1, 1]
      
        square.fill(nearestNeighbour)

        compressed_data[i_from:i_to, j_from:j_to] = square

with open("comprimida.csv", "w") as file:
    for row in compressed_data:
        row_length = len(row)
        for counter, cell in enumerate(row):
          if counter == row_length - 1:
            file.write(f'{int(cell)}\n')
          else:
            file.write(f'{int(cell)},')