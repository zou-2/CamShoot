import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
import cv2


class VideoPlayer(QMainWindow):
    def __init__(self):
        super(VideoPlayer, self).__init__()

        self.setWindowTitle("Video Player")

        # Créer un QLabel pour afficher la vidéo
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        # Créer un QWidget pour contenir le QLabel
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Créer un layout vertical pour le QWidget
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.label)

        # Créer un QTimer pour rafraîchir l'affichage de la vidéo
        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video)
        self.timer.start(30)  # Rafraîchir toutes les 30 ms

        # Démarrer la capture vidéo avec OpenCV
        self.video_capture = cv2.VideoCapture(0)

    def display_video(self):
        # Lire la vidéo avec OpenCV
        ret, frame = self.video_capture.read()
        if ret:
            # Convertir le frame en QImage
            height, width, channels = frame.shape
            bytes_per_line = channels * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_BGR888)

            # Convertir QImage en QPixmap
            pixmap = QPixmap.fromImage(q_image)

            # Mettre le QPixmap dans le QLabel
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def closeEvent(self, event):
        # Arrêter la capture vidéo et libérer les ressources à la fermeture de la fenêtre
        self.timer.stop()
        self.video_capture.release()
        super(VideoPlayer, self).closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoPlayer()
    window.show()
    sys.exit(app.exec_())