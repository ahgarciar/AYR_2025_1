
#from keras.preprocessing.image import load_img, img_to_array  #deprecated en tf 2.9 #alternative 0
#from tensorflow.keras.utils import load_img  #alternative 1
from keras.utils import load_img, img_to_array #alternative 2

largo, alto = 300, 300
#file = 'FIT_logo_vertical.png'
file = 'ImagenGatoEuropeo.png'
#file = "./Logo_5Aniversario.png"

img = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )

print(img.size)
print(img.mode)

#opcion 1
img.show()
