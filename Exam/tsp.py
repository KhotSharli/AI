import random
import numpy as np

cities = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (3, 1),
    'D': (4, 3),
    'E': (2, 1)
}

def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Create a distance matrix for all pairs of cities
dist_matrix = np.zeros((len(cities), len(cities)))
city_names = list(cities.keys())

for i, city1 in enumerate(city_names):
    for j, city2 in enumerate(city_names):
        dist_matrix[i][j] = calculate_distance(cities[city1], cities[city2])

POPULATION_SIZE = 100
NUM_GENERATIONS = 500
MUTATION_RATE = 0.01

def create_individual():
    return random.sample(city_names, len(city_names))

population = [create_individual() for _ in range(POPULATION_SIZE)]

def calculate_fitness(individual):
    total_distance = 0
    for i in range(len(cities) - 1):
        total_distance += dist_matrix[city_names.index(individual[i])][city_names.index(individual[i+1])]
    total_distance += dist_matrix[city_names.index(individual[-1])][city_names.index(individual[0])]
    return 1 / total_distance  # We want to maximize fitness

def selection(population, fitness_scores):
    return random.choices(population, weights=fitness_scores, k=2)

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[start:end] + [item for item in parent2 if item not in parent1[start:end]]
    return child

def mutation(individual):
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

for generation in range(NUM_GENERATIONS):
    # Calculate fitness scores for each individual in the population
    fitness_scores = [calculate_fitness(individual) for individual in population]

    # Create a new population through selection, crossover, and mutation
    new_population = []
    for _ in range(POPULATION_SIZE // 2):
        parent1, parent2 = selection(population, fitness_scores)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        new_population.extend([mutation(child1), mutation(child2)])

    # Replace the old population with the new population
    population = new_population

# Find the best individual (route) in the final population
best_individual = max(population, key=calculate_fitness)
best_distance = sum(dist_matrix[city_names.index(best_individual[i])][city_names.index(best_individual[i + 1])] for i in range(len(best_individual) - 1))
best_distance += dist_matrix[city_names.index(best_individual[-1])][city_names.index(best_individual[0])]

print("Best Route:", best_individual)
print("Best Distance:", best_distance)
