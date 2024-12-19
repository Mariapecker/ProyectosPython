import pandas as pd
import numpy as np
import os
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import os
from utils import cargar_y_preprocesar_imagen

# Configurar la API de Kaggle
api = KaggleApi()
api.authenticate()

# Descargar el conjunto de datos
if os.path.exists('kaggle-cat-vs-dog-dataset.zip') is False:
    api.dataset_download_files('karakaggle/kaggle-cat-vs-dog-dataset')
# kaggle datasets download -d karakaggle/kaggle-cat-vs-dog-dataset
# Descomprimir el archivo descargado
if os.path.exists('dogs_vs_cats\\kagglecatsanddogs_3367a\\PetImages') is False:
    with zipfile.ZipFile('kaggle-cat-vs-dog-dataset.zip', 'r') as file:
        file.extractall('dogs_vs_cats')

def cargar_y_preprocesar_imagen(ruta_imagen, tamano=(64, 64)):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen).convert('RGB')
    imagen = imagen.resize(tamano)
    imagen = np.array(imagen)
    imagen = imagen / 255.0 # Normalización
    return imagen

#Rutas a las carpetas de gatos y perros
ruta_gatos = 'D:\\ProyectosPython\\dogs_vs_cats\\kagglecatsanddogs_3367a\\PetImages\\Cat'
ruta_perros = 'D:\\ProyectosPython\\dogs_vs_cats\\kagglecatsanddogs_3367a\\PetImages\\Dog'
# Cargar y preprocesar imágenes
imagenes = []
etiquetas = []
# Cargar gatos
for archivo in os.listdir(ruta_gatos):
    ruta_completa = os.path.join(ruta_gatos, archivo)
# Lista de extensiones permitidas
    extensiones_permitidas = ['.jpg', '.jpeg', '.png', '.bmp']
    _, extension = os.path.splitext(archivo)

# Comprobar que la extensión es una de las permitidas
if (extension.lower() in extensiones_permitidas):
    try:
        img = cargar_y_preprocesar_imagen(ruta_completa)
        imagenes.append(img)
        etiquetas.append(0) # 0 para gatos
    except:
        print(f"No se pudo cargar la imagen {archivo}")
else:
    continue

# Cargar perros
for archivo in os.listdir(ruta_perros):
    ruta_completa = os.path.join(ruta_perros, archivo)
    # Lista de extensiones permitidas
    extensiones_permitidas = ['.jpg', '.jpeg', '.png', '.bmp']
    _, extension = os.path.splitext(archivo)
# otra opción podría ser ruta_imagen[-4:].lower() para obtener la extensión pero mejor así.
# Comprobar que la extensión es una de las permitidas
if (extension.lower() in extensiones_permitidas):
    try:
        img = cargar_y_preprocesar_imagen(ruta_completa)
        imagenes.append(img)
        etiquetas.append(1) # 1 para perros
    except:
        print(f"No se pudo cargar la imagen {archivo}")
else:
    continue

# Convertir listas a arrays de Numpy
imagenes = np.array(imagenes)
etiquetas = np.array(etiquetas)
X_train, X_test, y_train, y_test = train_test_split(imagenes, etiquetas,
test_size=0.2, random_state=42)
# Construcción del modelo
modelo = Sequential([
Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
MaxPooling2D(2, 2),
Conv2D(64, (3, 3), activation='relu'),
MaxPooling2D(2, 2),
Flatten(),
Dense(128, activation='relu'),
Dense(1, activation='sigmoid')
])
# Compilación del modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo
modelo.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
# Evaluar el modelo
evaluacion = modelo.evaluate(X_test, y_test)
print(f"Test Accuracy: {evaluacion[1] * 100}%")
modelo.save('modelo_cats_vs_dogs.keras') # Guarda el modelo en un archivo .keras

def predecir_imagen(ruta_imagen):
    modelo = load_model('modelo_cats_vs_dogs.keras')
    imagen = cargar_y_preprocesar_imagen(ruta_imagen)
    imagen = np.expand_dims(imagen, axis=0)
    prediccion = modelo.predict(imagen)
    if prediccion[0][0] > 0.5:
        print("Es un perro")
    else:
        print("Es un gato")

from keras.models import load_model
from utils import cargar_y_preprocesar_imagen, predecir_imagen
modelo = load_model('modelo_cats_vs_dogs.keras')
predecir_imagen(modelo, 'dogs_vs_cats/predict/puppy01.jpg')
predecir_imagen(modelo, 'dogs_vs_cats/predict/unknown.png')
predecir_imagen(modelo, 'dogs_vs_cats/predict/unknown1.png')
predecir_imagen(modelo, 'dogs_vs_cats/predict/gato1.jpg')
predecir_imagen(modelo, 'dogs_vs_cats/predict/gato2.jpg')