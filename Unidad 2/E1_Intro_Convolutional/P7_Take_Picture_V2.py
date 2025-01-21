import cv2  ##opencv
cam = cv2.VideoCapture(0) ##videocamara --- #op. cargar de carpeta las imagenes originales.. :p
contFotos = 0

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def face_detect_box(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    faces_frames = []
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)

        aux = image.copy()
        faces_frames.append(aux[y:y+h, x:x+w])

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
                imagen_cara = cv2.resize(img_faces[0], (300, 300), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite("foto_" + str(contFotos) + ".png", imagen_cara)

            contFotos+=1
    else:
        print("No image detected. Please! try again")
        break


