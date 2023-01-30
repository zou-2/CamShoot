
import os
import sys
from ui_Principal import *

# IMPORT Custom widgets
from Custom_Widgets.Widgets import *

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
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
