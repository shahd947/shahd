import random

def fitness_function(individual):

    return sum(individual)


def generate_individual(length):
    return [random.randint(0, 1) for _ in range(length)]


def generate_population(size, individual_length):
    return [generate_individual(individual_length) for _ in range(size)]


def select_parents(population, fitness_scores):

    idx1, idx2 = random.sample(range(len(population)), 2)
    if fitness_scores[idx1] > fitness_scores[idx2]:
        return population[idx1]
    return population[idx2]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip bit
    return individual


def genetic_algorithm(population_size, individual_length, generations, mutation_rate):

    population = generate_population(population_size, individual_length)
    
    for generation in range(generations):
  
        fitness_scores = [fitness_function(ind) for ind in population]
        
      
        print(f"Generation {generation}: Best fitness = {max(fitness_scores)}")
      
        new_population = []
        for _ in range(population_size // 2):
            parent1 = select_parents(population, fitness_scores)
            parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
        
      
        population = new_population
    

    fitness_scores = [fitness_function(ind) for ind in population]
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    print(f"Best individual: {best_individual} with fitness: {max(fitness_scores)}")


population_size = 20
individual_length = 10
generations = 50
mutation_rate = 0.1

genetic_algorithm(population_size, individual_length, generations, mutation_rate)
