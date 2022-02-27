# Game Of Life
# Humberto Barrantes
# 2022


# Imports

from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

# Local files

from GameOfLife import *
from GameOfLifeGUI import *
from GameOfLifeGif import *

# Main

#def main():

#    app = QApplication(sys.argv)

#    game_of_life = GameOfLife(50,50, random=True)
    
#    window = GameOfLifeGUI(game_of_life)

#    sys.exit(app.exec_())


#if __name__ == '__main__':
#    main()

# Ceate GIF

#game_of_life = GameOfLife(50,50, "lexicon/gabriel-p138.csv")

#GameOfLifeGif(game_of_life, "gabriel-p138.gif").create(iterations=138)

game_of_life = GameOfLife(50,50, random=True)

GameOfLifeGif(game_of_life, "radom-200.gif").create(iterations=200)