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
    7: [-3, -1, 1]
}

# Calculate the Manhattan distance heuristic
def calculate_manhattan(current_state):
    return sum(abs(current // 3 - goal // 3) + abs(current % 3 - goal % 3)
               for current, goal in ((current_state.index(i), goal_state.index(i))
                                     for i in range(1, 9)))

# Uniform Cost Search (UCS) function to solve the Eight Puzzle
def solve_puzzle(initial_state):
    open_list = [(0, initial_state, None)]  # (cost, state, parent)
    closed_list = set()
    costs = {initial_state: 0}  # Dictionary to track the cost to reach each state

    while open_list:
        cost, current_state, parent = heapq.heappop(open_list)

        if current_state == goal_state:
            # Reconstruct the path
            path = []
            while parent:
                path.append(current_state)
                current_state, parent = parent
            path.append(current_state)
            path.reverse()
            return path, cost

        if current_state in closed_list:
            continue

        closed_list.add(current_state)

        blank_index = current_state.index(0)
        for move in moves[blank_index]:
            new_state = list(current_state)
            new_state[blank_index], new_state[blank_index + move] = new_state[blank_index + move], 0
            new_state_tuple = tuple(new_state)
            new_cost = cost + 1  # Uniform cost of each move is 1

            if new_state_tuple not in costs or new_cost < costs[new_state_tuple]:
                costs[new_state_tuple] = new_cost
                heapq.heappush(open_list, (new_cost + calculate_manhattan(new_state_tuple), new_state_tuple, (current_state, parent)))

    return None, None  # No solution found

# Test the UCS on a given puzzle
if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 0, 5, 7, 8, 6)  # Example initial state
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
