# Game Of Life Gif generator
# Humberto Barrantes
# 2022

from PIL import Image, ImageDraw
import numpy as np

class GameOfLifeGif:


    def __init__(self, game, gifname, cellsize=20):
        self.game = game
        self.gifname = gifname

        self.height = game.rows * cellsize
        self.width = game.cols * cellsize
        self.cellsize = cellsize

        self.frames = []


    def create(self, iterations):
        """
        Execute the game and calls create_frame on each iteration

        Parameters:
        iterations (int) : number of iterations (frames) to create the gif
        """
        while iterations > 0:
            
            self.create_frame(self.game.matrix)

            self.game.update()

            iterations -= 1
        
        image = self.frames[0]

        image.save(
            self.gifname, 
            save_all=True, 
            append_images=self.frames[1:],
            loop=0
       )


    def create_frame(self, arr):
        """
        Create a PIL Image object based on the current game matrix state

        Parameters:
        arr (numpy.array) : current Game of Life game matrix state
        """
        image = Image.new("RGB", (self.height, self.width), "white")
        draw = ImageDraw.Draw(image)
    
        cs = self.cellsize

        for row in range(arr.shape[0]):
            for col in range(arr.shape[1]):
                if arr[row,col] == 1:
                    draw.rectangle(
                        (col*cs, row*cs, col*cs+cs, row*cs+cs), 
                        fill="black"
                    )

        self.frames.append(image)