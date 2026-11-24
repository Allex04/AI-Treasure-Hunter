import numpy as np
import random

class QLearningAgent:
    def __init__(self, grid_size, n_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.grid_size = grid_size         
        self.n_actions = n_actions
        self.q_table = np.zeros((self.grid_size, self.grid_size, self.n_actions))  # Q-values for each state-action pair
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def choose_action(self, state):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.randint(0, self.n_actions-1)  # Explore
        else:
            max_q = np.max(self.q_table[state])
            best_actions = np.where(self.q_table[state] == max_q)[0]  # Exploit
            return random.choice(best_actions)

    def update_q_value(self, state, action, reward, next_state, terminated):
        if terminated:
            max_future_q = 0
        else:
            max_future_q = np.max(self.q_table[next_state])  # Best Q-value for next state
        current_q = self.q_table[state][action]
        # Q-learning formula
        self.q_table[state][action] = current_q + self.learning_rate * (
            reward + self.discount_factor * max_future_q - current_q
        )



if __name__ == "__main__":
    agent = QLearningAgent(8, 4)

    state = (0, 5)
    action = 1
    reward = 10
    next_state = (0, 6)
    terminated = True

    agent.update_q_value(state, action, reward, next_state, terminated)
    print(agent.q_table[state][action])

    agent.update_q_value(state, action, reward, next_state, terminated)
    print(agent.q_table[state][action])

    agent.q_table[0, 5, 1] = 10

    agent.update_q_value((0, 4), 1, -1, (0, 5), False)
    print(agent.q_table[0, 4, 1])

    agent.update_q_value((0, 4), 1, -1, (0, 5), False)
    print(agent.q_table[0, 4, 1])

    agent = QLearningAgent(8, 4)

    agent.q_table[0, 6] = [20, 50, 30, 10]

    agent.update_q_value((0, 5), 1, 10, (0, 6), True)
    print(agent.q_table[0, 5, 1])