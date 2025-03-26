import cv2
import numpy as np

def train(images, labels):
	face_recognizer = cv2.face.FisherFaceRecognizer_create()

	print("Inicia Entrenamiento...")
	face_recognizer.train(images, np.array(labels))
	print("Entrenamiento Finalizado")
	dir = "../E3_ReconocimientoFacial_OpenCV/modelo/"
	face_recognizer.write( dir + 'modeloFisherFace.xml')
	print("Modelo almacenado!!!")
