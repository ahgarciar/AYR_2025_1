import os
import cv2

alto, largo = 300, 300

data_entrenamiento = "../E3_ReconocimientoFacial_OpenCV/F3-Prueba"
dir = "../E3_ReconocimientoFacial_OpenCV/modelo/"

modelo = cv2.face.EigenFaceRecognizer_create()
modelo.read(dir + 'modeloEigenFace.xml')

def predict(file):
    img = cv2.imread(file, 0) #escala de grises
    img = cv2.resize(img, (alto, largo), interpolation=cv2.INTER_CUBIC)

    #cv2.imshow('img', img)
    #cv2.waitKey(10)

    respuesta =  modelo.predict(img)  # etiqueta devuelta y confianza en la prediccion
    print("Respuesta: ", respuesta)

    match respuesta[0]:
        case 0:
            return 'C1-Daniel'
        case 1:
            return 'C2-Aaron'
        case 2:
            return 'C3-Eduardo'
        case _:
            return '----'


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


def probar_reconocedor():
    base_location = "../E2_ConvolutionalNeuronalNetwork/F3-Prueba/" #'./F3-Prueba/'

    folders = get_folders_name_from(base_location)

    correct = 0
    count_predictions = 0
    for folder in folders:
        files = [archivo for archivo in os.listdir(base_location + '/' + folder) if archivo.endswith(".jpg") or archivo.endswith(".jpeg") or archivo.endswith(".png")]
        for file in files:
            composed_location = base_location + folder + '/' + file
            prediction =  predict(composed_location)
            print('Folder Name: ', folder, ' Prediction: ',  prediction, " Resulto: ", prediction in folder)
            count_predictions += 1
            if prediction in folder:
                correct +=1

    print("Efficiency: ", (correct/count_predictions*100))

probar_reconocedor()