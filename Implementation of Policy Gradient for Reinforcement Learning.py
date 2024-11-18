import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Hyperparameters
learning_rate = 0.01
gamma = 0.99  # Discount factor for rewards
episodes = 1000

# Environment setup (Simple example: 2 actions)
n_states = 4
n_actions = 2

# Define the Policy Network
def build_policy_network(input_dim, output_dim):
    model = Sequential([
        Dense(24, activation='relu', input_dim=input_dim),
        Dense(24, activation='relu'),
        Dense(output_dim, activation='softmax')
    ])
    return model

policy_network = build_policy_network(n_states, n_actions)
optimizer = Adam(learning_rate)

# Storage for training
state_memory = []
action_memory = []
reward_memory = []

# Function to choose an action based on the policy
def choose_action(state):
    state = state[np.newaxis, :]
    probabilities = policy_network(state).numpy().flatten()
    return np.random.choice(n_actions, p=probabilities)

# Function to calculate discounted rewards
def discount_rewards(rewards, gamma):
    discounted = np.zeros_like(rewards, dtype=np.float32)
    cumulative = 0
    for i in reversed(range(len(rewards))):
        cumulative = cumulative * gamma + rewards[i]
        discounted[i] = cumulative
    return discounted

# Training loop
for episode in range(episodes):
    state = np.random.random(n_states)  # Random initial state (replace with environment state)
    episode_rewards = []
    
    for t in range(100):  # Maximum steps per episode
        action = choose_action(state)
        reward = np.random.random()  # Simulated reward (replace with environment reward)
        next_state = np.random.random(n_states)  # Simulated transition (replace with actual environment transition)
        
        # Store experience
        state_memory.append(state)
        action_memory.append(action)
        reward_memory.append(reward)
        
        state = next_state
        episode_rewards.append(reward)
        
        if np.random.random() < 0.1:  # Simulated episode end condition
            break
    
    # Discount and normalize rewards
    discounted_rewards = discount_rewards(episode_rewards, gamma)
    discounted_rewards -= np.mean(discounted_rewards)
    discounted_rewards /= np.std(discounted_rewards)
    
    # Train policy network
    with tf.GradientTape() as tape:
        states = np.array(state_memory)
        actions = np.array(action_memory)
        rewards = np.array(discounted_rewards)
        
        action_probs = policy_network(states)
        indices = np.arange(len(actions))
        chosen_action_probs = tf.math.log(action_probs[indices, actions])
        loss = -tf.reduce_mean(chosen_action_probs * rewards)
    
    grads = tape.gradient(loss, policy_network.trainable_variables)
    optimizer.apply_gradients(zip(grads, policy_network.trainable_variables))
    
    # Clear memory
    state_memory.clear()
    action_memory.clear()
    reward_memory.clear()

    if episode % 100 == 0:
        print(f"Episode {episode}, Total Reward: {sum(episode_rewards):.2f}")

print("Training Complete!")
