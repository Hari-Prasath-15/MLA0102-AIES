
import heapq

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    moves = [-3, 3, -1, 1]

    for move in moves:
        new_pos = zero + move

        if 0 <= new_pos < 9:
            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )
            neighbors.append(tuple(new_state))

    return neighbors

def solve(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        if state == goal:
            for step in path:
                print(step[:3])
                print(step[3:6])
                print(step[6:])
                print()
            print("Solved in", len(path) - 1, "moves")
            return

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + heuristic(neighbor),
                     g + 1, neighbor, path)
                )

    print("No solution found")

start = tuple(map(int, input(
    "Enter 9 numbers (use 0 for blank): "
).split()))

if len(start) == 9 and set(start) == set(range(9)):
    solve(start)
else:
    print("Invalid input! Enter numbers 0 to 8 exactly once.")
