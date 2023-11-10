import datetime
import sys
from PIL import Image
from keras.models import load_model
import numpy as np
from numpy import asarray
from numpy import expand_dims
import pickle
import cv2
import sqlite3
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget
from facial.logic import face_detector
from facial.services.model_singleton import ModelSingleton
# from facial.services.model_singleton import ModelSingleton
# from facial.logic.face_detector import face_detector
# from services.model_singleton import ModelSingleton

import time
from PySide2 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal


import resources_rc


class Worker(QThread):
    finished = pyqtSignal()
    
    def run(self):
        import Get_BD
        
        self.finished.emit()
        
        
        self.labelGif.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.verticalLayout_3.addWidget(self.labelGif)
        movie = QMovie('Pictures/loading2.gif')
        self.labelGif.setMovie(movie)
        movie.start() 
        self.labelGif.setVisible(False)  # Défaut : caché
        
############################################### BTN CLICKED ###################################################
###############################################################################################################
###############################################################################################################

        self.BtnCharger.clicked.connect(self.loadImage)
        self.BtnAjouter.clicked.connect(self.insert)
        self.BtnModif.clicked.connect(self.edit)
        self.validerBtn.clicked.connect(self.editAccount)
        self.BtnSupp.clicked.connect(self.delete)
        self.table.cellClicked.connect(self.handle_cell_clicked)
        self.BtnRecherche.clicked.connect(self.search)
        self.chargerBdBtn.clicked.connect(self.chargerBd)
        self.ligne = self.table.cellClicked.connect(self.on_cell_clicked)
        self.BtnActualiser.clicked.connect(self.reflesh)
        self.videoBtn.clicked.connect(self.getFace)
        
        self.showTableData()
        
        
        
        
        
        
        
        
        
def chargerBd(self):
        # Afficher le GIF
        self.labelGif.setVisible(True)
        
        self.worker = Worker()
        self.worker.finished.connect(self.onFinished)
        self.worker.start()

    def onFinished(self):
        self.labelGif.setVisible(False)
    
    ###################################################################################################################
    ############################################### FACE RECOGNITION ########################################################
    
    def record(self,identity,D_H):
        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        identity = str(identity)
        cur.execute("select id_Pers from Personnes where prenom = (?)", (identity,))
        con.commit()
        RqtResult = cur.fetchall()
        cur.execute("insert into Passages (dateHeure,ID_Pers)values (?,?)", (D_H, RqtResult[0][0]),)
        con.commit()   
        #RqtResult = cur.fetchall()
        con.close()
                
    def getFace(self):
        # HaarCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        HaarCascade = cv2.CascadeClassifier(cv2.samples.findFile(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'))
        #MyFaceNet = load_model("facenet_keras.h5")


        myfile = open("data.pkl", "rb")
        database = pickle.load(myfile)
        myfile.close()

        cap = cv2.VideoCapture(0)

        detected_identities = []
        # À l'extérieur de la boucle principale, initialisez un compteur pour créer des noms de fichiers uniques
        unknown_counter = 1

    
        while True:
            _, gbr1 = cap.read()

            wajah = HaarCascade.detectMultiScale(gbr1, 1.1, 4)

            if len(wajah) > 0:
                x1, y1, width, height = wajah[0]
            else:
                continue

            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height

            gbr = cv2.cvtColor(gbr1, cv2.COLOR_BGR2RGB)
            gbr = Image.fromarray(gbr)
            gbr_array = asarray(gbr)

            face = gbr_array[y1:y2, x1:x2]

            face = Image.fromarray(face)
            face = face.resize((160, 160))
            face = asarray(face)

            face = face.astype('float32')
            mean, std = face.mean(), face.std()
            face = (face - mean) / std

            signature = face_detector.face_detector(face)

            min_dist = 100
            identity = ' '
            date_heure = datetime.datetime.now()
            date_heure_texte = date_heure.strftime("%Y-%m-%d %H:%M:%S")

            for key, value in database.items():
                dist = np.linalg.norm(value - signature)
                if dist < min_dist:
                    min_dist = dist
                    color = (0, 255, 0)
                    identity = f"{key}"
                    

                    if identity not in detected_identities:
                        detected_identities.append(identity)

                    if identity != "non_reconnu":
                        color = (0, 255, 0)
                    else:
                        color = (0, 0, 255)

            cv2.putText(gbr1, identity, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (color), 2, cv2.LINE_AA)
            cv2.rectangle(gbr1, (x1, y1), (x2, y2), (color), 2)

            cv2.imshow('res', gbr1)

            # Vérifier si la liste detected_identities contient uniquement l'identité "non_reconnu" et prendre une photo
            if len(detected_identities) == 1 and detected_identities[0] == "non_reconnu":
                shoot_face_unknown = gbr1[y1:y2, x1:x2]
                chemin_dossier = "Photo/"
                img_item = f"{chemin_dossier}unknown_unknown_{time.time()}_face_{unknown_counter}.png"
                # img_item = "sary_test.png"
                cv2.imwrite(img_item, shoot_face_unknown)

                # Incrémenter le compteur pour le prochain fichier
                unknown_counter += 1
                
                self.record(identity,date_heure_texte)
                # Pour activer le bouton
                self.label_12.setText("Une personne vient de passer")
                self.notificationBtn.setEnabled(True)
                
            else:
                    
                self.record(identity,date_heure_texte)
                self.label_12.setText("Une personne vient de passer")
                self.notificationBtn.setEnabled(True)
            
            detected_identities = []

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()
    
    ###################################################################################################################
    ############################################### SHOW TABLE ########################################################    
    def showTableData(self):
        # Connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("select * from Personnes where id_Pers != 0")
        con.commit()
        RqtResult = cur.fetchall()
        
        self.table.clearContents()
        self.table.setRowCount(0)
        
        # Définissez la hauteur de ligne fixe (par exemple, 100 pixels)
        row_height = 100
        
        for row_number, row_data in enumerate(RqtResult):
            print(row_number)
            
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number == 1:  # Colonne contenant les données binaires de l'image
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(column_data)
                    label = QtWidgets.QLabel()
                    label.setPixmap(pixmap)
                    # Redimensionnez l'image pour qu'elle s'affiche à sa taille normale
                    label.setScaledContents(True)
                    # Encapsulez le QLabel dans un QWidget
                    widget = QtWidgets.QWidget()
                    layout = QtWidgets.QHBoxLayout()
                    layout.addWidget(label)
                    widget.setLayout(layout)
                    self.table.setCellWidget(row_number, column_number, widget)
                else:
                    self.table.setItem(row_number, column_number, QTableWidgetItem(item))
                    # Définissez la hauteur de la ligne
                    self.table.setRowHeight(row_number, row_height)
        con.close()

        # Ajustez automatiquement la hauteur des lignes pour afficher les images en entier
        # for row_number in range(self.table.rowCount()):
        #     self.table.resizeRowToContents(row_number)
    
    #######################################################################################################
    ############################################### SEARCH ################################################
    def search(self):
        #print("test:",self.input_Recherche.text())
        id = self.input_Recherche.text()
       
        for row_number in range(self.table.rowCount()):
            found = False
            for column_number in range(self.table.columnCount()):
                item = self.table.item(row_number, column_number)
                if item and id in item.text():
                    found = True
                    break
            if found:
                self.table.showRow(row_number)
            else:
                self.table.hideRow(row_number)
                
        if self.table.rowCount() == 0:
            QMessageBox.information(self, "Information", "Aucune ligne trouvée avec la recherche : {}".format(id))

    ###################################################################################################################
    ############################################### handle_cell_clicked ########################################################
    
    def  handle_cell_clicked(self,row, column):
        identifiant = self.table.item(row,0).text()
        # photo = self.table.item(row,1).text()
        nom = self.table.item(row,2).text()
        prenom = self.table.item(row,3).text()
        mail = self.table.item(row,4).text()
        telephone = self.table.item(row,5).text()
        adresse =self.table.item(row,6).text()
        ohatra = self.table.item(row,6).text()
        
        #desplacement données
        self.input_id_pers.setText(identifiant)
        self.input_nom.setText(nom)
        self.input_prenom.setText(prenom)
        # self.input_photo.setText(photo)
        self.input_mail.setText(mail)
        self.input_telephone.setText(telephone)
        self.input_adresse.setText(adresse)
        self.input_adresse.setText(ohatra)
    
    #fonction recuperant ligne table    
    def on_cell_clicked(self, row):
        return row
    #fonction actualisant la table    
    def reflesh(self):
        self.showTableData()
########################################################### INSERT #########################################################
############################################################################################################################
############################################################################################################################
    def insert(self):
        identifiant = self.input_id_pers.text()
        nom = self.input_nom.text()
        prenom = self.input_prenom.text()
        # photo = self.input_photo.text()
        telephone = self.input_telephone.text()
        mail = self.input_mail.text()
        adresse = self.input_adresse.text()
        
        # Ouverture du fichier image et conversion en données binaires
        with open(self.input_photo.text(), 'rb') as image_file:
                image_binary = image_file.read()
        

        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("insert into Personnes (id_Pers,photo,nom,prenom,mail,telephone,adresse)values (?,?,?,?,?,?,?)", (identifiant, image_binary, nom, prenom, mail, telephone, adresse))
        con.commit()   
        #RqtResult = cur.fetchall()
        con.close()
        self.label_12.setText("Ajout d'une personne")
        self.input_id_pers.setText("")
        self.input_nom.setText("")
        self.input_prenom.setText("")
        self.input_photo.setText("")
        self.input_telephone.setText("")
        self.input_mail.setText("")
        self.input_adresse.setText("")
        self.showTableData()
        
    ############################################################ EDIT ##########################################################
    ############################################################################################################################
    ############################################################################################################################
    def editAccount(self):
        userName = self.editUserName.text()
        password = self.currentMdp.text()
        newPassword = self.newMdp.text()
        confirmNewPassword = self.confirmNewMdp.text()
        
        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("select * from Login")
        
        RqtResult = cur.fetchall()
        
        oldPassword = RqtResult[0][2]
        
        print(f" current:{password}, oldpass: {oldPassword}, newpass: {newPassword}, confirmpass: {confirmNewPassword}")
        # print(RqtResult[0][2])
        # print(newPassword)
        
        if userName == "":
            userName = "Admin"
        
        if ((str(password) == str(oldPassword)) and (str(newPassword) == str(confirmNewPassword))):
        
            cur.execute("update Login set userName=?,password=?where Identifiant=?",
            (userName, newPassword, 1))
            self.label_12.setText("Compte mise à jours")
            self.editUserName.setText("")
            self.currentMdp.setText("")
            self.newMdp.setText("")
            self.confirmNewMdp.setText("")
            
        con.commit()
        con.close()
        
        self.showTableData()
        
        
    def edit(self):
        identifiant = self.input_id_pers.text()
        # photo = self.input_photo.text()
        nom = self.input_nom.text()
        prenom = self.input_prenom.text()
        telephone = self.input_telephone.text()
        mail = self.input_mail.text()
        adresse = self.input_adresse.text()
        
        # Ouverture du fichier image et conversion en données binaires
        with open(self.input_photo.text(), 'rb') as image_file:
                image_binary = image_file.read()
        
        print(identifiant)
        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("update Personnes set id_Pers=?,photo=?,nom=?,prenom=?,mail=?,telephone=?,adresse=? where id_Pers=?",
            (identifiant, image_binary, nom, prenom, mail, telephone, adresse,identifiant))
        con.commit()
        con.close()
        
        self.label_12.setText("Modification d'une personne")
        self.input_id_pers.setText("")
        self.input_nom.setText("")
        self.input_prenom.setText("")
        self.input_photo.setText("")
        self.input_telephone.setText("")
        self.input_mail.setText("")
        self.input_adresse.setText("")
        self.showTableData()
    def delete(self):
        
        identifiant = self.input_id_pers.text()
        # connexion à la base de données
        con = sqlite3.connect('CamShoot.db')
        cur = con.cursor()
        cur.execute("delete from Personnes where id_Pers = ?",(identifiant,))
        con.commit()   
        con.close()
        
        self.label_12.setText("Suppression d'une personne")    
        self.input_id_pers.setText("")
        self.input_nom.setText("")
        self.input_prenom.setText("")
        self.input_photo.setText("")
        self.input_telephone.setText("")
        self.input_mail.setText("")
        self.input_adresse.setText("")
        self.showTableData()
    
####################################################################################################################

################################################LOAD IMAGE##########################################################
    def loadImage(self):   
        FileName = QFileDialog.getOpenFileName(None, 'open file','E:\Photo_nathan\Albert.jpg')
        self.input_photo.setText(FileName[0])        
