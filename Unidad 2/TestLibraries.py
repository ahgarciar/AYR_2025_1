##librerias que se requieren:
# tensorflow
# keras
# scikit-learn
# numpy
# pandas

import tensorflow as tf
print(tf.__version__)

import keras as k
print(k.__version__)

import sklearn as sk
print(sk.__version__)

import numpy as n
a = [1, 2, 3] ##lista en python normal ....
a = n.array(a)  #convierte la lista de python a una matriz de numpy
print(a)

import pandas as pd
s = pd.Series([1,3,5, n.nan,6, 8])  #instancias de datos...
print(s)


# SPEECH RECOGNITION OFFLINE CON -> VOSK

