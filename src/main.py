import numpy as np

# Define the environment and it's obstacles.
# 0 represents a grid tile that is empty, -1 represents an obstacle, and 1 represents the goal.
gridworld = np.array([
    [0, 0, 0, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, -1, 0],
    [-1, 0, -1, 0, 0],
    [0, 0, 0, 0, 1]
])

# Define the goal state
goal_state = (4, 4)

# Define the different set of actions
actions = ['up', 'down', 'left', 'right']

# Initializing the Q-Table with all zeros.
q_table = np.zeros((5, 5, len(actions)))

# Define the reward for the given action
def get_reward(state, action, next_state):
    # Check for obstacle collision
    if gridworld[next_state[0], next_state[1]] == -1:
        # if next_state is an obstacle, penalize the agent
        r = -10
    # Check if agent has reached goal
    elif next_state == goal_state:
        # if next_state is the goal, reward the agent
        r = 10
    # All other cases, have a small penalty for movement to maximize navigation efficiency.
    else:
        r = -1 
    return r

# Define the Q-Learning algorithm
def q_learning(state, action, reward, next_state):
    # Determine the best future action based on Q-values of the next state
    best_future_qval = np.max(q_table[next_state[0], next_state[1], :])
    # Grab the current Q-value
    curr_qval = q_table[state[0], state[1], actions.index(action)]
    # Calculate temporal distance error
    TD_error = (reward + gamma * best_future_qval - curr_qval)
    # Update the Q-Table
    q_table[state[0], state[1], actions.index(action)] += alpha * TD_error

# Define the hyperparameters
num_episodes = 1000
alpha = 0.1
gamma = 0.99
epsilon = 0.1

# Define a simple form of memory for visuals


for episode in range(num_episodes):
    #Some initial setup and debug for training
    
    
    print('********')
    print('performing episode', episode)
    print('********')
    
    # Set the current state to be a random position.
    state = (np.random.randint(0,5), np.random.randint(0,5))
  
    # If the agent hasn't reached the goal, begin the training process
    while state != goal_state:
        # Determine whether or not to make a random action or an action based on the max q values of the current state inside the Q-Table.
        # This is a simple epsilon-greedy policy, where 10% of the time, a random action is performed so the agent can explore the environment.
        if np.random.rand() < epsilon:
            action = actions[np.random.randint(0, len(actions))]
        else:
            action = actions[np.argmax(q_table[state[0], state[1], :])]

        # Change the value of the next state to current state in case the attempt to get the next_state is invalid (bug handling)
        next_state = state
        # Get the next state based on directional movement
        if action == 'up':
            next_state = (state[0]-1, state[1])
        elif action == 'down':
            next_state = (state[0]+1, state[1])
        elif action == 'left':
            next_state = (state[0], state[1]-1)
        elif action == 'right':
            next_state = (state[0], state[1]+1)
        # Check if the next state is out of bounds, if so then revert the state change and keep the original state.
        if next_state[0] < 0 or next_state[0] > 4 or next_state[1] < 0 or next_state[1] > 4 or gridworld[next_state[0], next_state[1]] == -1:
            next_state = state

        # Calculate reward based on the action chosen from Q-Table
        reward = get_reward(state, action, next_state)
        
        # Update the Q value of of the current state
        q_learning(state, action, reward, next_state)

        # Progress to the next state
        state = next_state

print('finished training, starting testing')
# Testing using the fully updated Q-Table.
num_episodes = 100
successes = 0
total_reward = 0

times_moved_history = {}
mem = []
for episode in range(num_episodes):
    ep_mem = []
    print('********')
    print('performing testing w episode', episode)
    print('********')
    state = (np.random.randint(0, 5), np.random.randint(0, 5))
    ep_mem.append(state)
    orig_state = state
    episode_reward = 0
    times_moved = 0
    while state != goal_state:
        print('state is not equal to goal')
        action = actions[np.argmax(q_table[state[0], state[1], :])]
        
        next_state = state
        if action == 'up':
            next_state = (state[0]-1, state[1])
            print('moving up')
        elif action == 'down':
            print('moving down')
            next_state = (state[0]+1, state[1])
        elif action == 'left':
            print('moving left')
            next_state = (state[0], state[1]-1)
        elif action == 'right':
            print('moving right')
            next_state = (state[0], state[1]+1)
        if next_state[0] < 0 or next_state[0] > 4 or next_state[1] < 0 or next_state[1] > 4 or gridworld[next_state[0], next_state[1]] == -1:
            next_state = state
            print('hitting wall at state:', state, 'with actions:',q_table[state[0], state[1], :])
            print('Q-table:')
            print(q_table)
        ep_mem.append(next_state)
        reward = get_reward(state, action, next_state)
        episode_reward += reward
        
        state = next_state
        print('moved to next state')
        times_moved = times_moved + 1
        
    if state == goal_state:
        print('reached goal - times moved:', times_moved)
        successes += 1
        times_moved_history[str(times_moved)] = orig_state
    else:
        print('failed to reach goal')
    total_reward += episode_reward
    mem.append(ep_mem)

# Print the results
print('Success Rate:', successes/num_episodes)
print('Average Reward:', total_reward/num_episodes)

print('Final Q-Table Used:')
print(q_table)

print('Move Count History (Count : (startpos):')
print(times_moved_history)

print("Episode Memories:")
print(mem)



