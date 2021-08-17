import os

def load(dir, img):
    reader = open(dir + img, 'r')
    list1 = []
    for i in reader.readlines():
        list1.append(i.split(","))
    return list1

directory = "C:/Users/USUARIO/Desktop/ST0245-001/proyecto/codigo/csv/sano_csv"
img_list = os.listdir(directory)
for i in img_list:
    imglst = load(directory, i)
 