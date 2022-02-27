# Game Of Life Gif generator
# Humberto Barrantes
# 2022

from PIL import Image, ImageDraw
from array2gif import write_gif
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


    def numpy_to_rgb(self, arr):
        result = np.zeros((arr.shape[0]*10, arr.shape[1]*10, 3))

        for row in range(arr.shape[0]):
            for col in range(arr.shape[1]):

                if arr[row,col] == 1:
                    result[row*10:(row*10)+10,col*10:(col*10)+10] = np.zeros((10, 10, 3))
                else:
                    result[row*10:(row*10)+10,col*10:(col*10)+10] = np.full((10, 10, 3), 255)

        return result