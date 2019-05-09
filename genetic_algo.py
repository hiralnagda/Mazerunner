# from depth_first_search import *
from breadth_first_search import *

maze_prob = 0.1
maze_population = []
maze_pop_count = 100
counter = 0
padding = 5
px_size = 25
size = 20
mid = (size * size)/2
end = size * size
window = (px_size * size) + padding

# Generates maze population for the application of G.A
while True:
    # Select the maze
    visited_main, window, padding, px_size = build_maze(maze_prob)
    # Apply DFS to get parameters for the fitness function
    maze_population.append(breadth_first_search(visited_main, window, padding, px_size))
    # If the destination is reachable
    if maze_population[-1][0] is True:
        counter = counter + 1
    else:
        # If the destination is not reachable, pop the last added item
        maze_population.pop()
    if counter == maze_pop_count:
        break

# Run the algo 50 times
for i in range(50):
    # print(maze_population)
    maze_population = sorted(maze_population, key=lambda l:l[1], reverse=True) # Sorting by shortest path

    # Select the 2 fittest mazes and perform a crossover
    mother = maze_population[0]
    father = maze_population[1]
    child = OrderedDict()

    # Select first half of mother
    counter = 0
    for key, val in mother[-1].items():
        counter = counter + 1
        child[key] = val
        if counter == mid:
            break

    # Select second half of father
    counter = 0
    for key, val in father[-1].items():
        counter = counter + 1
        if mid < counter < end + 1:
            child[key] = val
        if counter >= end + 1:
            break

    result = breadth_first_search(child, window, padding, px_size)

    if result[0] is True:
        # print('if entered')
        # If a path exists, add it to the population and remove the weakest element
        maze_population.pop()
        maze_population.append(result)
    else:
        # print('else entered')
        # If the maze does not exist, remove the max element and try again
        maze_population.pop(0)
