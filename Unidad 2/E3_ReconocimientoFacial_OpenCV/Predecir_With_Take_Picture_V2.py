import cv2  ##opencv
cam = cv2.VideoCapture(0) ##videocamara --- #op. cargar de carpeta las imagenes originales.. :p
contFotos = 0

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

###########
alto, largo = 300, 300
data_entrenamiento = "../E3_ReconocimientoFacial_OpenCV/F3-Prueba"
dir = "../E3_ReconocimientoFacial_OpenCV/modelo/"
modelo = cv2.face.EigenFaceRecognizer_create()
modelo.read(dir + 'modeloEigenFace.xml')
###########

def face_detect_box(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    faces_frames = []
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)

        aux = image.copy()
        face = aux[y:y+h, x:x+w]
        faces_frames.append(face)

        gray_face = face.copy()
        gray_face = cv2.cvtColor(gray_face, cv2.COLOR_BGR2GRAY)
        gray_face = cv2.resize(gray_face, (alto, largo), interpolation=cv2.INTER_CUBIC)
        respuesta = modelo.predict(gray_face)
        print("Respueta: ", respuesta)
        cv2.putText(image, '{}'.format(respuesta), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

        nombres =  ["Daniel", "Aaron", "Eduardo"]
        if respuesta[1] < 13000: #valor configurable ->valores mas cercanos = mayor confianza en la prediccion
            cv2.putText(image, '{}'.format(nombres[respuesta[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(image, 'Desconocido', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return faces, faces_frames


while True:
    result, image = cam.read()
    if result:

        faces_detected, img_faces = face_detect_box(image)

        cv2.imshow("Camara_Principal", image)

        res = cv2.waitKey(1) ## 1  = .. no detenga la ejecucion
        #print(res , "  ", ord("q"))
        if res == ord("q"):
            cam.release()
            cv2.destroyWindow("Camara_Principal")
            break
        elif res == ord(" "): ##space
            if len(img_faces) == 0:
                cv2.imwrite("foto_"+ str(contFotos) + ".png", image)
            else:
                imagen_cara = cv2.resize(img_faces[0], (alto, largo), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite("foto_" + str(contFotos) + ".png", imagen_cara)

            contFotos+=1
    else:
        print("No image detected. Please! try again")
        break


