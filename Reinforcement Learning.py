import numpy as np

# Environment setup
states = ['A', 'B', 'C', 'D']
actions = ['left', 'right']
reward_matrix = {
    ('A', 'right'): 1, ('B', 'right'): 2, ('C', 'right'): 3, ('D', 'right'): 10,
    ('A', 'left'): 0, ('B', 'left'): 0, ('C', 'left'): 0, ('D', 'left'): 0
}
q_table = {state: {action: 0 for action in actions} for state in states}
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor

# Q-Learning algorithm
for episode in range(100):
    state = np.random.choice(states)
    for step in range(10):  # Limiting steps per episode
        action = np.random.choice(actions)
        next_state = states[(states.index(state) + (1 if action == 'right' else -1)) % len(states)]
        reward = reward_matrix.get((state, action), 0)
        q_table[state][action] += alpha * (
            reward + gamma * max(q_table[next_state].values()) - q_table[state][action]
        )
        state = next_state

# Display Q-Table
print("Q-Table:")
for state, actions in q_table.items():
    print(state, actions)
