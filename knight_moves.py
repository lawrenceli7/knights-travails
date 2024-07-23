from collections import deque

def knightMoves(start, end):
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def isOnBoard(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    queue = deque([(start, [start])])
    visited = set()
    visited.add(tuple(start))

    while queue:
        (current, path) = queue.popleft()

        if current == end:
            return path
        for move in moves:
            nextPos = (current[0] + move[0], current[1] + move[1])

            if isOnBoard(nextPos[0], nextPos[1]) and nextPos not in visited:
                visited.add(nextPos)
                queue.append((nextPos, path + [nextPos]))


print(knightMoves([0, 0], [1, 2]))
print(knightMoves([0, 0], [3, 3]))
print(knightMoves([3, 3], [0, 0]))
print(knightMoves([0, 0], [7, 7]))