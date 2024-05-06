# Define the capacities of the jugs
jug1_capacity = 4
jug2_capacity = 3

# Initial state: Both jugs are empty
initial_state = (0, 0)

# Define the production rules
def fill_jug1(state):
    return (jug1_capacity, state[1])

def fill_jug2(state):
    return (state[0], jug2_capacity)

def empty_jug1(state):
    return (0, state[1])

def empty_jug2(state):
    return (state[0], 0)

def pour_jug1_to_jug2(state):
    amount_to_pour = min(state[0], jug2_capacity - state[1])
    return (state[0] - amount_to_pour, state[1] + amount_to_pour)

def pour_jug2_to_jug1(state):
    amount_to_pour = min(jug1_capacity - state[0], state[1])
    return (state[0] + amount_to_pour, state[1] - amount_to_pour)

# Apply the rules to get the next possible states
def get_next_states(state):
    next_states = []
    next_states.append(fill_jug1(state))
    next_states.append(fill_jug2(state))
    next_states.append(empty_jug1(state))
    next_states.append(empty_jug2(state))
    next_states.append(pour_jug1_to_jug2(state))
    next_states.append(pour_jug2_to_jug1(state))
    return next_states

# Breadth-First Search to find a solution
def water_jug_bfs(target_amount):
    queue = [(initial_state, [])]  # (current_state, path)
    visited = set()

    while queue:
        current_state, path = queue.pop(0)
        if current_state[0] == target_amount or current_state[1] == target_amount:
            return path
        
        if current_state in visited:
            continue
        
        visited.add(current_state)

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# Example usage:
target_amount = 2  # Amount of water to measure
solution_path = water_jug_bfs(target_amount)

if solution_path:
    print(f"Steps to measure {target_amount} liters of water:")
    for i, state in enumerate(solution_path):
        print(f"Step {i + 1}: Jug 1 = {state[0]}, Jug 2 = {state[1]}")
else:
    print("No solution found.")
