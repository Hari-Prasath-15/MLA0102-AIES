
from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        m, c, boat = state
        path = path + [state]

        if state == goal:
            for step in path:
                print("Missionaries:", step[0],
                      "Cannibals:", step[1],
                      "Boat:", "Left" if step[2] == 1 else "Right")
            print("Solution found!")
            return

        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            nm, nc, nb = new_state

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            if (nm > 0 and nm < 3 and nm < nc):
                continue

            rm, rc = 3 - nm, 3 - nc

            if rm > 0 and rm < rc:
                continue

            if new_state not in visited:
                queue.append((new_state, path))

    print("No solution found")

solve()
