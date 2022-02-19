# Game Of Life GUI
# Humberto Barrantes
# 2022

from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


class GameOfLifeGUI(QMainWindow):
    
    
    def __init__(self, game, speed=100):
        """
        Initializes the Graphic Interface for the GameOfLife object

        Parameters:
        game (GameOfLife): Game of Life logic object

        speed (int): times between iterations
        """
        
        super().__init__()

        self.game = game
        
        self.count = 0
        
        self.title = "Game of Life"
  
        self.top= 150

        self.left= 150
        
        self.width = game.rows * 10

        self.height = game.cols * 10

        self.speed = speed
  
        self.InitWindow()
    
    
    def InitWindow(self):
        """
        Creates the Main window and the Timer to refresh it
        """
        
        self.setWindowTitle(self.title)

        self.setGeometry(self.top, self.left, self.width, self.height)

        self.show()
        
        # creating a timer object
        timer = QTimer(self)
  
        # adding action to timer
        timer.timeout.connect(self.tick)
  
        # update the timer every second
        timer.start(self.speed)
    
    
    def paintEvent(self, event):
        """
        Takes the game matrix and paint it inside the window using QPainter

        Parameters:
        event (QEvent): raised when the window updates

        """

        painter = QPainter(self)
        painter.setPen(QPen(Qt.black,  1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        
        for row in range(self.game.rows):
            for col in range(self.game.cols):
                if self.game.matrix[row][col]:
                    painter.drawRect(row*10, col*10, 10, 10)
    
    
    def tick(self):
        """
        Timer Event executed every t seconds 
        """

        self.count += 1
        self.game.update()
        self.update()