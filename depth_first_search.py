from board import *
from find_neighbours import *


def get_path(parent, src, dest, path, win):
    while parent[dest] != src:
        x, y = parent[dest]
        rec = Rectangle(Point(x, y), Point(x + 10, y + 10))
        rec.setFill("yellow")
        rec.draw(win)
        path.append(parent[dest])
        dest = parent[dest]
    path.reverse()
    return path


def print_path(parent, src, dest, win):
    print(get_path(parent, src, dest, [], win))


def get_tot_steps(parent, src, dest, win):
    tot_steps = len(get_path(parent, src, dest, [], win))
    return tot_steps + 1


def depth_first_search(visited_copy, window, padding, px_size, win):
    visited = visited_copy.copy()
    iteration = 0
    visit_order = 1
    max_fringe_size = 0
    parent = dict()
    dest_reachable = False
    stack = list()
    source = (padding, padding)
    dest = (window - px_size, window - px_size)
    stack.append(source)
    # win = GraphWin('Mazerunner', window + padding, window + padding)

    while len(stack) != 0:
        iteration = iteration + 1
        temp = stack[-1]
        stack.pop()

        if visited[temp] is False and temp != source and temp != dest:
            visit_order = visit_order + 1
            visited[temp] = True
            rec = Rectangle(Point(temp[0], temp[1]), Point(temp[0] + px_size, temp[1] + px_size))
            rec.setFill("green")
            rec.draw(win)

        if temp == dest:
            dest_reachable = True
            break

        nbours = return_neighbours(temp, window, padding, px_size)
        for element in nbours:
            if visited[element] is False:
                stack.append(element)
                parent[element] = temp

        if len(stack) > max_fringe_size:
            max_fringe_size = len(stack)

    if dest_reachable:
        # print('The destination is reachable.')
        return [True, get_tot_steps(parent, source, dest, win), visit_order, max_fringe_size, visited_copy]
    else:
        # print('The destination is not reachable.')
        return [False, None, None, None, None]

    # print('Number of nodes expanded: ', visit_order)
    #
    # print('Total steps from source to destination: ', get_tot_steps(parent, source, dest))
    #
    # print('Max fringe size: ', max_fringe_size)
    # print_path(parent, source, dest)


def dfs_main(visited, window, padding, px_size, win):
    dest_status = depth_first_search(visited, window, padding, px_size, win)
    time.sleep(2)
    return dest_status
