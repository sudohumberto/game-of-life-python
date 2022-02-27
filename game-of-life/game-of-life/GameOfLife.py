# Game Of Life Logic
# Humberto Barrantes
# 2022

import numpy as np
import pandas as pd

class GameOfLife:
    
    
    def __init__(self, rows, cols, seed=None, random=False):
        """
        Initializes the matrix and settle a seed if required

        Parameters:
        rows (int): number of rows in the game matrix
        
        cols (int): number of cols in the game matrix

        seed (str): name of the csv file that contains the initial values of the game matriz
        """

        self.rows = rows
        self.cols = cols
        
        self.matrix = np.zeros((rows, cols))

        if random:
            self.matrix = np.random.randint(0, 2, size=(rows, cols))

        if seed != None:
            self.load_seed(seed)

        self.time = 0
        
    def load_seed(self, seed):
        """
        Loads the data inside a csv file and copy it to the center of the game matrix

        Parameters:
        seed (str): name of the csv file the function uses to load the initial values
        """
        df = pd.read_csv(seed, header=None)

        arr = df.to_numpy()
        
        arr_rows = arr.shape[0]
        arr_cols = arr.shape[1]

        from_row = (self.rows - arr_rows) // 2
        from_col = (self.cols - arr_cols) // 2

        to_row = from_row + arr_rows
        to_col = from_col + arr_cols

        self.matrix[from_row:to_row,from_col:to_col] = arr



    def cell_transition(self, row, col):
        """
        Computes the state of the individual/cell in the next iteration based on
        John Conway's game of life rules

        Parameters:
        row (int): row of the individual/cell we are analysing

        col (int): col of the individual/cell we are analysing

        Returns:
        int: 1 if the individual/cell is still alive, 0 if it dies
        """
        neighbours = 0
        for i in range(-1,2):
            for j in range(-1,2):
                
                if i == 0 and j == 0:
                    continue
                else:
                    if row+i > 0 and row+i < self.rows:
                        if col+j > 0 and col+j < self.cols:
                            neighbours += self.matrix[row+i][col+j]
        
        # live cell 
        if self.matrix[row][col]:
            
            # Any live cell with fewer than two live neighbours dies 
            # underpopulation or exposure
            if neighbours < 2:
                return 0
            # Any live cell with more than three live neighbours dies 
            # overpopulation or overcrowding
            elif neighbours > 3:
                return 0
            # Any live cell with two or three live neighbours lives, 
            # unchanged, to the next generation.
            else:
                return 1
        
        # dead cell
        else:
            # Any dead cell with exactly three live neighbours will come to life
            if neighbours == 3:
                return 1
            else:
                return 0
        


    def update(self):
        """
        Iterates over the entire matrix and updates every position
        """
        new_array = np.zeros((self.rows, self.cols))
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                new_array[row][col] = self.cell_transition(row, col)

        ones = new_array.sum()
        self.matrix = new_array