import csv
import os

dir1 = "C:/Users/USUARIO/Desktop/ST0245-001/proyecto/codigo/csv/sano_csv/"
dir2 = "C:/Users/USUARIO/Desktop/ST0245-001/proyecto/codigo/csv/enfermo_csv/"
list1 = os.listdir(dir1)
list2 = os.listdir(dir2)

def load(dlist, directory):
    csv_list = []
    for i in dlist:
        with open(directory + i, 'r') as csv_file:
            csv_list.append(csv.reader(csv_file))
    return csv_list

healthy = load(list1, dir1)
sick = (list2, dir2)

for i in healthy:
    print(i)