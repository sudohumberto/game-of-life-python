# Game Of Life Gif generator
# Humberto Barrantes
# 2022

from array2gif import write_gif
import numpy as np

class GameOfLifeGif:

    def __init__(self, game, gifname):
        self.game = game
        self.gifname = gifname

    def create(self, iterations):

        frames = []

        ids = []

        while iterations > 0:
            frame = self.numpy_to_rgb(self.game.matrix)
            frame_id = id(frame)

            frames.append(frame)

            if frame_id in ids:
                break
            else:
                ids.append(frame_id)

            self.game.update()

            iterations -= 1
        
        write_gif(frames, "beluchenko-p37.gif")


    def numpy_to_rgb(self, arr):
        result = np.zeros((arr.shape[0]*10, arr.shape[1]*10, 3))

        for row in range(arr.shape[0]):
            for col in range(arr.shape[1]):

                if arr[row,col] == 1:
                    result[row*10:(row*10)+10,col*10:(col*10)+10] = np.zeros((10, 10, 3))
                else:
                    result[row*10:(row*10)+10,col*10:(col*10)+10] = np.full((10, 10, 3), 255)

        return result