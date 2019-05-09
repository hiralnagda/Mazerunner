def return_neighbours(position, window, padding, px_size):
    neighbours = []
    x, y = position
    dx = [0, 0, -1 * px_size, px_size]
    dy = [px_size, -1 * px_size, 0, 0]

    for i in range(0, 4, 1):
        row = x + dx[i]
        col = y + dy[i]

        if row < padding or col < padding:
            continue

        if row > window - px_size or col > window - px_size:
            continue

        neighbours.append((row, col))

    return neighbours
