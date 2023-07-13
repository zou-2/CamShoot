
import os
import sys
from ui_Principal import *
import threading

import os
# import sys

# # Obtenez le chemin absolu du dossier parent du fichier en cours d'exécution
# chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# # Ajoutez le chemin absolu du dossier parent au chemin de recherche des modules
# chemin_facial = os.path.join(chemin_parent, "facial")
# sys.path.append(chemin_facial)

# from facial import Get_BD



# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
ModelSingleton.get_instance("./facenet_keras_weights.h5")
# INITIALIZE APP SETTINGS
settings = QSettings()

## MAIN WINDOW CLASS

class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # APPLY JSON STYLESHEET
        # self = QMainWindow class  
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        # SHOW WINDOW
        self.show()

        # EXPAND CENTER MENU WIDGET SIZE
        self.ui.parametreBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.informationBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.aideBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
       
        # CLOSE CENTER MENU WIDGET
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())


        # EXPAND RIGHT MENU WIDGET SIZE
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
       
        # CLOSE RIGHT MENU WIDGET SIZE
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
       
       # CLOSE RIGHT MENU WIDGET SIZE
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
        


########################################################################
## EXECUTE L'APP
########################################################################
if __name__ == "__main__":
    #ui = Ui_MainWindow()
    #def demarrer_interface():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    #thread_1 = threading.Thread(target= demarrer_interface)
    #thread_2 = threading.Thread(target= ui.getFace())
    
    
    #thread_1.start()
    #thread_2.start()
    
    #thread_1.join()
    #thread_2.join()
 
########################################################################
## END===>
########################################################################