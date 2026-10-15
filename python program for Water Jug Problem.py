
from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        jug1, jug2 = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        print(jug1, jug2)

        if jug1 == target or jug2 == target:
            print("Target reached!")
            return

        states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, capacity2 - jug2),
             jug2 + min(jug1, capacity2 - jug2)),
            (jug1 + min(jug2, capacity1 - jug1),
             jug2 - min(jug2, capacity1 - jug1))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Target cannot be reached")

capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

if target < 0 or target > max(capacity1, capacity2):
    print("Invalid target!")
else:
    water_jug(capacity1, capacity2, target)
