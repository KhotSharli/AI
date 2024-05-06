# Define the goal state of the puzzle
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 represents the blank space

# Define movements (left, right, up, down)
moves = {
    0: [1, 3],
    1: [-1, 1, 3],
    2: [-1, 3],
    3: [-3, 1, 3],
    4: [-3, -1, 1, 3],
    5: [-3, -1, 3],
    6: [-3, 1],
    7: [-3, -1, 1]
}

# Perform depth-limited DFS
def depth_limited_dfs(current_state, depth_limit, path=[]):
    if depth_limit == 0:
        return None  # Reached depth limit without finding the goal

    if current_state == goal_state:
        path.append(current_state)
        return path  # Goal state found

    blank_index = current_state.index(0)
    for move in moves[blank_index]:
        new_state = list(current_state)
        new_state[blank_index], new_state[blank_index + move] = new_state[blank_index + move], 0
        result = depth_limited_dfs(tuple(new_state), depth_limit - 1, path + [current_state])
        if result:
            return result

    return None  # Goal not found within depth limit

# Iterative Deepening Depth-First Search (IDDFS)
def iddfs(initial_state):
    depth_limit = 0
    while True:
        result = depth_limited_dfs(initial_state, depth_limit)
        if result:
            return result
        depth_limit += 1

# Test the IDDFS on a given puzzle
if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 0, 5, 7, 8, 6)  # Example initial state
    solution_path = iddfs(initial_state)
    
    if solution_path:
        print("Solution found:")
        for i, state in enumerate(solution_path):
            print("Move", i)
            print(state[0], state[1], state[2])
            print(state[3], state[4], state[5])
            print(state[6], state[7], state[8])
            print()
    else:
        print("No solution found within the search depth limit.")
