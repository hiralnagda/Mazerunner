from Astar import astar_main_manhattan, astar_main_euclidean
from depth_first_search import dfs_main
from breadth_first_search import bfs_main
from board import *

main_win = GraphWin('Mazerunner', 500, 500)
msg = Text(Point(250, 50), "AI Mazerunner Project")
msg.setSize(20)
msg.draw(main_win)

button_ = ["DFS", "BFS", "A* (EU)", "A* (MH)"]
_button = ["green", "blue", "grey", "orange"]

for i in range(4):
    rect = Rectangle(Point(160, 125 + 50*i), Point(340, 175 + 50*i))
    rect.setFill(_button[i])
    rect.draw(main_win)
    msg = Text(Point(250, 150 + 50*i), button_[i])
    msg.draw(main_win)

mouse_click = main_win.getMouse()

if (160 <= mouse_click.x < 340) and (125 <= mouse_click.y < 325):
    main_win.close()
    dfs_data = dict()
    bfs_data = dict()
    astar_data = dict()

    maze_prob = 0.25
    size = 50
    visited_main, window, padding, px_size, win = build_maze(maze_prob, size)

    if 125 <= mouse_click.y < 175:
        print("Depth First Search")
        dfs_visited = visited_main.copy()
        if dfs_main(dfs_visited, window, padding, px_size, win)[0] is True:
            print("Path Exists.")
        else:
            print("No path found.")

    elif 175 <= mouse_click.y < 225:
        print("Breadth First Search")
        bfs_visited = visited_main.copy()
        if bfs_main(bfs_visited, window, padding, px_size, win)[0] is True:
            print("Path Exists.")
        else:
            print("No path found.")

    elif 225 <= mouse_click.y < 275:
        print("A* Heuristic using Euclidean Distance")
        astar_eu_visited = visited_main.copy()
        if astar_main_euclidean(astar_eu_visited, window, padding, px_size, win)[0] is True:
            print("Path Exists.")
        else:
            print("No path found.")

    else:
        print("A* Heuristic using Manhattan Distance")
        astar_mh_visited = visited_main.copy()
        if astar_main_manhattan(astar_mh_visited, window, padding, px_size, win)[0] is True:
            print("Path Exists.")
        else:
            print("No path found.")

else:
    main_win.close()
    main_win = GraphWin('Mazerunner', 300, 100)
    msg = Text(Point(150, 50), "Wrong Selection Aborting!!")
    msg.draw(main_win)
    time.sleep(1)
    main_win.close()
