
from ui_Principal import *

class Connexion():
            # connexion à la base de données
    con = sqlite3.connect('CamShoot.db')
    cur = con.cursor()
       
    def __init__(self, parent):
        self.parent = parent
        self.identifiant = self.parent.input_id_pers.text()
        self.nom = self.parent.input_nom.text()
        self.prenom = self.parent.input_prenom.text()
        self.photo = self.parent.input_photo.text()
        self.telephone = self.parent.input_telephone.text()
        self.mail = self.parent.input_mail.text()
        self.adresse = self.parent.input_adresse.text()
    def sel(self):
        cur.execute("insert into Personnes (id_Pers,photo,nom,prenom,mail,telephone,adresse)values (?,?,?,?,?,?,?)", (identifiant, photo, nom, prenom, mail, telephone, adresse))
        con.commit()
        RqtRes = cur.fetchall()
        con.close()
    
        self.parent.input_id_pers.setText("")
        self.parent.input_nom.setText("")
        self.parent.input_prenom.setText("")
        self.parent.input_photo.setText("")
        self.parent.input_telephone.setText("")
        self.parent.input_mail.setText("")
        self.parent.input_adresse.setText("")
    