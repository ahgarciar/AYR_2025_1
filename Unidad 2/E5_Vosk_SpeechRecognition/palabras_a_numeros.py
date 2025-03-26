
##consideramos que solo aparece un numero
#cadena = "tengo dos manzanas"
cadena = "tengo treinta y dos manzanas"
#cadena = "tengo una calificacion de ocho"

from word2number_es import w2n
num_en_digitos = w2n.word_to_num(cadena)
print(num_en_digitos)  #

from num2words import num2words
#num2words(42)
#num2words(42, to='ordinal')
num_en_letra = num2words(num_en_digitos, lang='es')
print(num_en_letra)

cadena = cadena.replace()
