
def vacuum_cleaner():
    rooms = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    location = 'A'

    while 'Dirty' in rooms.values():
        print("Vacuum is in room", location)

        if rooms[location] == 'Dirty':
            print("Room", location, "is Dirty. Cleaning...")
            rooms[location] = 'Clean'
        else:
            print("Room", location, "is already Clean.")

        if location == 'A':
            location = 'B'
        else:
            location = 'A'

    print("All rooms are clean!")
    print(rooms)

vacuum_cleaner()
