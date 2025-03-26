import cv2
import os
import numpy as np
#import entrenar_EigenFace as entrenador
import entrenar_FisherFace as entrenador
#import entrenar_LBPHFace as entrenador

data_entrenamiento = "../E3_ReconocimientoFacial_OpenCV/F1-Entrenamiento"

alto, largo = 300, 300

def get_folders_name_from(from_location):
    list_dir = os.listdir(from_location)
    # folders = [archivo for archivo in listDir if os.path.splitext(archivo)[1] == ""]
    # the above is equals to ....
    folders = []
    for file in list_dir:
        temp = os.path.splitext(file)
        if temp[1] == "":
            folders.append(temp[0])
    folders.sort()
    folders.remove('.DS_Store') #solo en mac
    return folders

folders = get_folders_name_from(data_entrenamiento)
print('Nombre de las carpetas (clases): ', folders)

labels = []
images = []
label = 0

for folder in folders:
    full_dir = data_entrenamiento + '/' + folder
    print('Leyendo las imágenes')

    for fileName in os.listdir(full_dir):
        print('Faces: ', folder + '/' + fileName)
        labels.append(label)
        img = cv2.imread(full_dir + '/' + fileName, 0) # 0 = escala de grises
        img = cv2.resize(img, (alto, largo), interpolation=cv2.INTER_CUBIC)
        images.append(img)
        #cv2.imshow('img',img)
        #cv2.waitKey(10)
    label = label + 1

print('labels= ',labels)
for clase in range(label):
    print('Imagenes de clase ' + str(clase) + ':',np.count_nonzero(np.array(labels)==clase))

entrenador.train(images, labels)