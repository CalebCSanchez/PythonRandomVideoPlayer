from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from videoplayer import VideoPlayer

class MainMenu(QWidget):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)

        button = QPushButton()
        button.setFixedHeight(24)

        button.clicked.connect(self.player)
        mainMenuLayout = QVBoxLayout()
        mainMenuLayout.addWidget(button)
        self.setLayout(mainMenuLayout)


        
        
    def player(self):
        player = VideoPlayer()
        player.setWindowTitle("RandomVideoPlayer")
        player.resize(600, 400)
        player.show()