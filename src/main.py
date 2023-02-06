from mainmenu import MainMenu
from videoplayer import VideoPlayer
from PyQt5.QtWidgets import QApplication
import sys


app = QApplication(sys.argv)
# mainMenu = MainMenu()
# mainMenu.setWindowTitle("Random Video Player")
# mainMenu.show()
videoPlayer = VideoPlayer()
videoPlayer.show()

sys.exit(app.exec_())