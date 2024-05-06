import heapq

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
    7: [-3, -1, 1],
    8: [-3, -1]
}

# Calculate the Manhattan distance heuristic
def calculate_manhattan(current_state):
    return sum(abs(current // 3 - goal // 3) + abs(current % 3 - goal % 3)
               for current, goal in ((current_state.index(i), goal_state.index(i))
                                     for i in range(1, 9)))

# A* search function to solve the Eight Puzzle
def solve_puzzle(initial_state):
    open_list = [(calculate_manhattan(initial_state), initial_state, 0, None)]  # (f= estimated cost (f) to reach the goal state , state, g= cost so far (g), parent)
    closed_list = set()

    while open_list:
        _, current_state, g, parent = heapq.heappop(open_list) #Removes and returns the smallest item

        if current_state == goal_state:
            # Reconstruct the path
            path = []
            while parent:
                path.append(current_state)
                current_state, parent = parent
            path.append(current_state)
            path.reverse()
            return path, g

        if current_state in closed_list:
            continue

        closed_list.add(current_state)

        blank_index = current_state.index(0)
        for move in moves[blank_index]:
            new_state = list(current_state)
            new_state[blank_index], new_state[blank_index + move] = new_state[blank_index + move], 0
            new_state_tuple = tuple(new_state)
            if new_state_tuple not in closed_list:
                heapq.heappush(open_list, (g + 1 + calculate_manhattan(new_state_tuple), new_state_tuple, g + 1, (current_state, parent)))

    return None, None  # No solution found

# Test the A* search on a given puzzle
if __name__ == "__main__":
    initial_state = (1,2,3,4,5,0,8,6,7)  # Example initial state
    path, num_moves = solve_puzzle(initial_state)
    
    if path:
        print("Solution found in", num_moves, "moves:")
        for i, state in enumerate(path):
            print("Move", i + 1)
            print(state[0], state[1], state[2])
            print(state[3], state[4], state[5])
            print(state[6], state[7], state[8])
            print()
    else:
        print("No solution found for the given puzzle.")
