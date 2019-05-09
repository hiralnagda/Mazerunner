from board import *
from find_neighbours import *
import heapq as hq
import collections


def heuristic_val_euclidean(neighbour, window, px_size):
    x, y = neighbour
    xdiff = (x - (window - px_size)) ** 2
    ydiff = (y - (window - px_size)) ** 2
    return pow(xdiff + ydiff, 0.5)


def heuristic_val_manhattan(neighbour, window, px_size):
    x, y = neighbour
    xdiff = (window - px_size) - x
    ydiff = (window - px_size) - y
    return xdiff + ydiff


def get_path(parents, source, dest, win):
    path = collections.deque()
    node = dest
    path.appendleft(node)

    while node != source:
        if parents.get(node) is None:
            print("No path")
            return False
        node = parents[node]
        path.append(node)
        x, y = node

        # Shortest Path
        if (x,y) != source:
            rec = Rectangle(Point(x, y), Point(x + 10, y + 10))
            rec.setFill("yellow")
            rec.draw(win)
    return path


def astar_manhattan(visited_copy, window, padding, px_size, win):
    visited = visited_copy.copy()
    count = 0
    closedList = set()

    # openList (fval,(x,y))
    openList = list()

    # openList2 only has tuple (x,y) : easy to compare with neighbours
    openList2 = set()
    parents = dict()
    cost_to_node = dict()
    source = (padding, padding)
    dest = (window - px_size, window - px_size)
    openList2.add(source)
    hq.heapify(openList)
    hq.heappush(openList, (heuristic_val_manhattan(source, window, px_size), source))

    # Cost to node is g()
    cost_to_node[source] = 0
    visit_order = 1
    max_fringe_size = -1
    no_of_nodes_expanded = 0

    while len(openList) != 0:
        if len(openList) > max_fringe_size:
            max_fringe_size = len(openList)
        count = count + 1
        fval, curr = hq.heappop(openList)
        openList2.remove(curr)
        closedList.add(curr)
        nbours = return_neighbours(curr, window, padding, px_size)

        if curr == dest:
            path = get_path(parents, source, dest, win)
            return [True, len(path), count, max_fringe_size, visited_copy]

        for neighbour in nbours:
            if visited[neighbour] is False:
                cost = cost_to_node[curr] + px_size

                if neighbour in openList2 and cost < cost_to_node[neighbour]:
                    openList.pop(neighbour)
                    openList2.remove(neighbour)

                if neighbour in closedList and cost < cost_to_node[neighbour]:
                    closedList.remove(neighbour)

                if neighbour not in openList2 and neighbour not in closedList:
                    cost_to_node[neighbour] = cost
                    fval = cost_to_node[neighbour] + heuristic_val_manhattan(neighbour, window, px_size)
                    openList2.add(neighbour)
                    hq.heappush(openList, (fval, neighbour))
                    parents[neighbour] = curr
                    no_of_nodes_expanded += 1
                    x, y = neighbour

                    if (x,y) != source and (x,y) != dest:
                        rec = Rectangle(Point(x, y), Point(x + px_size, y + px_size))
                        rec.setFill("orange")
                        visit_order = visit_order + 1
                        rec.draw(win)
    return [False, None, None, None, None]


def astar_euclidean(visited_copy, window, padding, px_size, win):
    visited = visited_copy.copy()
    count = 0
    closedList = set()

    # openList (fval,(x,y))
    openList = list()

    # openList2 only has tuple (x,y) : easy to compare with neighbours
    openList2 = set()
    parents = dict()
    cost_to_node = dict()
    source = (padding, padding)
    dest = (window - px_size, window - px_size)
    openList2.add(source)
    hq.heapify(openList)
    hq.heappush(openList, (heuristic_val_euclidean(source, window, px_size), source))

    # Cost to node is g()
    cost_to_node[source] = 0
    visit_order = 1
    max_fringe_size = -1
    no_of_nodes_expanded = 0
    while len(openList) != 0:
        if len(openList) > max_fringe_size:
            max_fringe_size = len(openList)
        count = count + 1
        fval, curr = hq.heappop(openList)
        openList2.remove(curr)
        closedList.add(curr)
        nbours = return_neighbours(curr, window, padding, px_size)

        if curr == dest:
            path = get_path(parents, source, dest, win)
            return [True, len(path), count, max_fringe_size, visited_copy]

        for neighbour in nbours:
            if visited_copy[neighbour] is False:

                cost = cost_to_node[curr] + px_size

                if neighbour in openList2 and cost < cost_to_node[neighbour]:
                    openList.pop(neighbour)
                    openList2.remove(neighbour)

                if neighbour in closedList and cost < cost_to_node[neighbour]:
                    closedList.remove(neighbour)

                if neighbour not in openList2 and neighbour not in closedList:
                    cost_to_node[neighbour] = cost
                    fval = cost_to_node[neighbour] + heuristic_val_euclidean(neighbour, window, px_size)
                    openList2.add(neighbour)
                    hq.heappush(openList, (fval, neighbour))
                    parents[neighbour] = curr
                    no_of_nodes_expanded += 1
                    x, y = neighbour

                    if (x, y) != source and (x, y) != dest:
                        rec = Rectangle(Point(x, y), Point(x + px_size, y + px_size))
                        rec.setFill("grey")
                        visit_order = visit_order + 1
                        rec.draw(win)
    return [False, None, None, None, None]


def astar_main_euclidean(visited, window, padding, px_size, win):
    dest_status = astar_euclidean(visited, window, padding, px_size, win)
    time.sleep(2)
    # win.getMouse()
    return dest_status


def astar_main_manhattan(visited, window, padding, px_size, win):
    dest_status = astar_manhattan(visited, window, padding, px_size, win)
    time.sleep(2)
    # win.getMouse()
    return dest_status
