import cv2
import numpy as np

def train(images, labels):
	face_recognizer = cv2.face.LBPHFaceRecognizer_create()

	print("Inicia Entrenamiento...")
	face_recognizer.train(images, np.array(labels))
	print("Entrenamiento Finalizado")
	dir = "../E3_ReconocimientoFacial_OpenCV/modelo/"
	face_recognizer.write( dir + 'modeloLBPHFace.xml')
	print("Modelo almacenado!!!")
