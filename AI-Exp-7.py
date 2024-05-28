import random

# Function to generate a random solution
def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []
    for i in range(len(tsp)):
        random_city = cities[random.randint(0, len(cities) - 1)]
        solution.append(random_city)
        cities.remove(random_city)
    return solution

# Function to calculate the total length of a given route
def routeLength(tsp, solution):
    route_length = 0
    for i in range(len(solution)):
        route_length += tsp[solution[i - 1]][solution[i]]
    return route_length

# Function to generate neighbours of a solution
def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbours.append(neighbour)
    return neighbours

# Function to find the best neighbour
def getBestNeighbour(tsp, neighbours):
    best_route_length = routeLength(tsp, neighbours[0])
    best_neighbour = neighbours[0]
    for neighbour in neighbours:
        current_route_length = routeLength(tsp, neighbour)
        if current_route_length < best_route_length:
            best_route_length = current_route_length
            best_neighbour = neighbour
    return best_neighbour, best_route_length

# Hill Climbing Algorithm
def hillClimbing(tsp):
    current_solution = randomSolution(tsp)
    current_route_length = routeLength(tsp, current_solution)
    while True:
        neighbours = getNeighbours(current_solution)
        best_neighbour, best_neighbour_route_length = getBestNeighbour(tsp, neighbours)
        if best_neighbour_route_length >= current_route_length:
            break
        current_solution = best_neighbour
        current_route_length = best_neighbour_route_length
    return current_solution, current_route_length

# Main function
def main():
    tsp = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]
    solution, length = hillClimbing(tsp)
    print(f"Optimal route: {solution}")
    print(f"Route length: {length}")

if __name__ == "__main__":
    main()
