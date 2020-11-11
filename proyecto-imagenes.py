# hacemos uso de la libreria tesseract para poder hacerder al texto dentro de la imagen
#! pip install tesseract-ocr
#! pip install pytesseract

# importamos las dependencias que se van a utilizar
# Importamos Pytesseract
#! sudo apt install tesseract-ocr

import shutil
import os
import random
import pytesseract
import sys
try:
    from PIL import Image

except ImportError:
    import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# hacemos uso de la dependencia que nos pernite acceder a cualquier archivo dentro de nuestro equipo
#from google.colab import files


#uploaded = files.upload()
# BytesIO(uploaded['letras.jpg'])

im = Image.open(sys.argv[1])

# Utilizamos el método "image_to_string"
# Le pasamos como argumento la imagen abierta con opencv
texto = pytesseract.image_to_string(im)

# Mostramos el resultado
print(texto)
