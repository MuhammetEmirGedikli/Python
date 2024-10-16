import random
import numpy as np
from deap import base, creator, tools

num_vehicles = 3
num_customers = 12
capacity = 8

customer_locations = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_customers)]
customer_demands = [random.randint(1, 10) for _ in range(num_customers)]

def assess_solution(individual):
    routes = [[] for _ in range(num_vehicles)]
    route_capacity = [0] * num_vehicles

    for a, gene in enumerate(individual):
        if gene < num_vehicles:
            routes[gene].append(a)
            route_capacity[gene] += customer_demands[a]

    total_distance = 0.0
    for i in range(num_vehicles):
        if len(routes[i]) > 0:
            route = [0] + routes[i] + [0]
            for j in range(len(route) - 1):
                start = customer_locations[route[j]]
                end = customer_locations[route[j + 1]]
                distance = np.linalg.norm(np.array(end) - np.array(start))
                total_distance += distance

    if total_distance == 0.0:
        total_distance = 999999

    return total_distance,

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("genes", random.sample, range(num_customers), num_customers)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.genes)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", assess_solution)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3)
toolbox.register("select", tools.selTournament, tournsize=1)

def main():
    num_people = 10
    num_generations = 5

    population = toolbox.population(n=num_people)

    fitness_values = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitness_values):
        ind.fitness.values = fit

    for gen in range(num_generations):
        offspring = toolbox.select(population, len(population))

        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < 0.5:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < 0.2:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_individuals = [ind for ind in offspring if not ind.fitness.valid]
        fitness_values = map(toolbox.evaluate, invalid_individuals)
        for ind, fit in zip(invalid_individuals, fitness_values):
            ind.fitness.values = fit

        population[:] = offspring

        fitness = [ind.fitness.values[0] for ind in population]

        print(f"Generation {gen + 1}: Min {min(fitness)}, Max {max(fitness)}, Avg {np.mean(fitness)}")

    return population

if __name__ == "__main__":
    final_population = main()

    best_individual = tools.selBest(final_population, 1)[0]
    best_route = sorted(list(set(best_individual)))
    print("Optimal Route:", best_route)
    print("Total Distance:", best_individual.fitness.values[0])

    input("Press Enter to exit:")
