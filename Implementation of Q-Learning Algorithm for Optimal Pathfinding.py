import numpy as np

# Define the environment
states = ["A", "B", "C", "D", "E"]
actions = ["Go_Left", "Go_Right"]
rewards = {
    ("A", "Go_Right"): 0,
    ("B", "Go_Left"): 0,
    ("B", "Go_Right"): 1,
    ("C", "Go_Left"): 1,
    ("C", "Go_Right"): 0,
    ("D", "Go_Left"): 0,
    ("E", "Go_Left"): 1,
}

# Initialize the Q-Table
Q_table = np.zeros((len(states), len(actions)))

# Hyperparameters
learning_rate = 0.1
discount_factor = 0.9
episodes = 1000

# Training the Q-Learning algorithm
for episode in range(episodes):
    state_index = np.random.randint(0, len(states))  # Start at a random state
    for _ in range(10):  # Limiting steps per episode
        action_index = np.random.randint(0, len(actions))  # Choose a random action
        current_state = states[state_index]
        action = actions[action_index]

        # Calculate reward
        next_state = states[(state_index + (1 if action == "Go_Right" else -1)) % len(states)]
        reward = rewards.get((current_state, action), -1)

        # Update Q-Value
        next_state_index = states.index(next_state)
        Q_table[state_index, action_index] = Q_table[state_index, action_index] + learning_rate * (
            reward + discount_factor * np.max(Q_table[next_state_index]) - Q_table[state_index, action_index]
        )

        # Transition to next state
        state_index = next_state_index

# Display the learned Q-Table
print("Learned Q-Table:")
for state, q_values in zip(states, Q_table):
    print(f"{state}: {q_values}")
