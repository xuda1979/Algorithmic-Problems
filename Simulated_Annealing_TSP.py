import math
import random
import matplotlib.pyplot as plt

# Define the function to calculate the total distance of the tour
def calculate_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) + distance_matrix[tour[-1]][tour[0]]

# Create a new candidate solution by swapping two cities
def create_new_solution(current_solution):
    i, j = random.sample(range(len(current_solution)), 2)
    new_solution = current_solution.copy()
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Define the function to perform the simulated annealing algorithm
def simulated_annealing(cities, distance_matrix, initial_temperature, cooling_rate, max_iterations, min_temperature=1e-10, seed=42, log=True):
    random.seed(seed)  # Seed the random number generator for reproducibility
    current_solution = random.sample(range(cities), cities)
    best_solution = current_solution.copy()
    current_distance = best_distance = calculate_distance(current_solution, distance_matrix)
    temperature = initial_temperature
    no_improvement_iterations = 0
    max_no_improvement = 1000
    distances = []
    temperatures = []
    acceptance_rates = []
    accepted_moves = 0
    total_moves = 0

    for iteration in range(max_iterations):
        new_solution = create_new_solution(current_solution)
        new_distance = calculate_distance(new_solution, distance_matrix)
        total_moves += 1

        # Accept the new solution if better or with a probability based on temperature
        if new_distance < current_distance or (temperature > min_temperature and random.random() < math.exp(-(new_distance - current_distance) / temperature)):
            current_solution, current_distance = new_solution, new_distance
            accepted_moves += 1
            if new_distance < best_distance:
                best_solution, best_distance = new_solution.copy(), new_distance
                no_improvement_iterations = 0
        else:
            no_improvement_iterations += 1

        distances.append(best_distance)
        temperatures.append(temperature)
        acceptance_rates.append(accepted_moves / total_moves if total_moves > 0 else 0)

        if no_improvement_iterations >= max_no_improvement:
            if log:
                print(f"Terminating early at iteration {iteration} due to no improvement over the last {max_no_improvement} iterations.")
            break

        # Adaptive cooling schedule: adjust the cooling rate based on iteration count and solution improvement
        improvement_factor = 1 - (best_distance / (current_distance + 1e-10))  # Factor based on improvement
        adaptive_cooling_rate = cooling_rate * (1 - iteration / max_iterations) * (1 + improvement_factor)
        temperature = max(temperature * adaptive_cooling_rate, min_temperature)

    if log:
        print("Optimization Report:")
        print(f"Total iterations: {iteration + 1}")
        print(f"Final Temperature: {temperature}")
        print(f"Best Distance: {best_distance}")
        print(f"Acceptance Rate: {accepted_moves / total_moves if total_moves > 0 else 0:.4f}")

    visualize_progress(distances, temperatures, acceptance_rates)
    return best_solution, best_distance

# Plot the progress of the best distance, temperature, and acceptance rate
def visualize_progress(distances, temperatures, acceptance_rates):
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Best Distance', color='b')
    ax1.plot(distances, marker='o', linestyle='-', color='b', label='Best Distance')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Temperature', color='r')
    ax2.plot(temperatures, linestyle='--', color='r', label='Temperature')
    ax2.tick_params(axis='y', labelcolor='r')

    fig.tight_layout()
    plt.title('Simulated Annealing Progress')
    plt.legend(loc='upper right')
    plt.show()

    plt.plot(acceptance_rates, marker='x', linestyle='-', color='g', label='Acceptance Rate')
    plt.xlabel('Iteration')
    plt.ylabel('Acceptance Rate')
    plt.title('Acceptance Rate Progress')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    cities = 5
    distance_matrix = [
        [0, 10, 15, 20, 25],
        [10, 0, 35, 25, 30],
        [15, 35, 0, 30, 5],
        [20, 25, 30, 0, 15],
        [25, 30, 5, 15, 0]
    ]
    initial_temperature = 1000
    cooling_rate = 0.995
    max_iterations = 10000

    best_solution, best_distance = simulated_annealing(cities, distance_matrix, initial_temperature, cooling_rate, max_iterations, log=True)
    print("Best Solution:", best_solution)
    print("Best Distance:", best_distance)