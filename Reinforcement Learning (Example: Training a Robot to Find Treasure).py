import numpy as np

# Defining the environment as a grid (4x4)
# 0: Empty space, 1: Treasure, -1: Danger
grid = np.array([
    [0, 0, 0, 1],  # 1 = Treasure
    [0, -1, 0, 0],  # -1 = Danger
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])

# Robot's initial position
robot_position = [0, 0]

# Simulated moves (Right, Down, Right, Right)
moves = ['right', 'down', 'right', 'right']
reward = 0

# Simulating the robot's actions
for move in moves:
    if move == 'right':
        robot_position[1] += 1
    elif move == 'down':
        robot_position[0] += 1

    # Get the reward at the new position
    current_cell = grid[robot_position[0], robot_position[1]]
    if current_cell == 1:
        reward += 10  # Treasure
        print(f"Treasure found at {robot_position}!")
        break
    elif current_cell == -1:
        reward -= 5  # Danger
        print(f"Danger at {robot_position}! Losing points.")
    else:
        print(f"Safe move to {robot_position}.")

print("Total reward:", reward)
