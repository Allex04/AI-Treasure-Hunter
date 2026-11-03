import numpy as np
import matplotlib.pyplot as plt

class TreasureHunter:
    def __init__(self):
        self.grid_size = 8         
        self.n_actions = 4 
        self.Q_table = np.zeros((grid_size, grid_size, n_actions))
        self.grid = np.zeros((8,8), dtype=int)
    
        self.grid[2,2] = 1
        self.grid[2,3] = 1
        self.grid[2,4] = 1
        self.grid [4,4] = 2
        self.grid [0,6] = 3
        self.grid [7,7] = 4
        self.start_state = (0,0)
        self.state = self.start_state

    def reset(self):
        self.state = self.start_state
        return self.state

    
