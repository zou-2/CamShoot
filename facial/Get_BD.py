import os
import sys

# Obtenez le chemin absolu du dossier parent du fichier en cours d'exécution
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ajoutez le chemin absolu du dossier parent au chemin de recherche des modules
chemin_facial = os.path.join(chemin_parent, "facial")
sys.path.append(chemin_facial)
print("chemin ="+chemin_facial)
# Importez le fichier du dossier logic
from logic.face_detector import face_detector

# Importez le fichier du dossier logic
from services.model_singleton import ModelSingleton

import sqlite3
from os import listdir
from PIL import Image as Img
from numpy import asarray
from numpy import expand_dims
from keras.models import load_model
import pickle
import cv2

ModelSingleton.get_instance("./facenet_keras_weights.h5")
#charger classifier et facenet_keras


HaarCascade = cv2.CascadeClassifier(cv2.samples.findFile(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'))
#MyFaceNet = load_model("facenet_keras.h5")

#MyFaceNet = FaceNet()


folder = 'photos/' #chemin dossier photos
database = {}

# connexion à la base de données
con = sqlite3.connect('E:/BUR/New folder (2)/Sublime/CamShoot.db')
cur = con.cursor()
cur.execute("select * from Personnes")
RqtResult = cur.fetchall()
#con.commit()
con.close()

#for filename in listdir(folder):
for row in RqtResult:

    #path = folder + filename

    path = row[1]
    
    gbr1 = cv2.imread(path)

    visage = HaarCascade.detectMultiScale(gbr1, 1.1, 4)

    if len(visage) > 0:
        x1, y1, width, height = visage[0]
    else:
        x1, y1, width, height = 1, 1, 10, 10

    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height

    gbr = cv2.cvtColor(gbr1, cv2.COLOR_BGR2RGB)
    gbr = Img.fromarray(gbr)  # conversion file OpenCV en PIL
    gbr_array = asarray(gbr)  #convert en tab

    face = gbr_array[y1:y2, x1:x2]  #prendre face fotsiny

    face = Img.fromarray(face)  # retour en img
    face = face.resize((160, 160))
    face = asarray(face)

    #normaliser entree
    face = face.astype('float32')
    mean, std = face.mean(), face.std() #moyenne et ecart type
    face = (face - mean) / std

    # envoie des entree a facenet
    #face = expand_dims(face, axis=0)
    #signature = MyFaceNet.predict(face)
    signature = face_detector(face)
    #signature = MyFaceNet.embeddings(face)
    #database[filename]= signature
    # print('1 = '+row[1] +', 2 = ' + row[3])
    database[row[3]] = signature

#print(database)
myfile = open("data.pkl", "wb")
pickle.dump(database, myfile)
myfile.close()

myfile = open("data.pkl", "rb")
database = pickle.load(myfile)
myfile.close()