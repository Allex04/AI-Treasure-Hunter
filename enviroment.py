import numpy as np
import matplotlib.pyplot as plt

class TreasureHunter:
    def __init__(self):
        self.grid_size = 8        
        self.n_actions = 4
        self.max_steps = 100
        self.steps = 0
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
    
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
        self.steps = 0
        return self.state

    def is_terminal(self, state):
        return bool(self.grid[state] == 3 or self.grid[state] == 4)

    def is_truncated(self):
        return self.steps >= self.max_steps

    def get_next_state(self, state, action):
        next_state = list(state)
        if action == 0:  # Move up
            next_state[0] = max(0, state[0] - 1)
        elif action == 1:  # Move right
            next_state[1] = min(self.grid_size-1, state[1] + 1)
        elif action == 2:  # Move down
            next_state[0] = min(self.grid_size-1, state[0] + 1)
        elif action == 3:  # Move left
            next_state[1] = max(0, state[1] - 1)
        if self.grid[tuple(next_state)] == 1:
            return tuple(state)
        else:
            return tuple(next_state)
    def step(self, action):
        next_state = self.get_next_state(self.state, action)
        self.steps += 1
        if next_state == self.state:
            reward = -2
        elif self.grid[next_state] == 0:
            reward = -1
        elif self.grid[next_state] == 2:
            reward = -10
        elif self.grid[next_state] == 3:
            reward = 10
        elif self.grid[next_state] == 4:
            reward = 30
        self.state = next_state
        terminal = self.is_terminal(next_state)
        truncated = self.is_truncated()
        return next_state, reward, terminal, truncated


#test    
game = TreasureHunter()

game.state = (2, 1)
print(game.step(1))  # wall

game.state = (4, 3)
print(game.step(1))  # trap

game.state = (0, 5)
print(game.step(1))  # small treasure

game.reset()
game.steps = 99
print(game.step(1))