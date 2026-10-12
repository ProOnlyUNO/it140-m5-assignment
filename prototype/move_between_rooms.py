"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}

# Start the player in the Great Hall.
current_room = 'Great Hall'

# Continue the game until the player chooses to exit.
while current_room != 'exit':
    print('You are currently in the', current_room)

    command = input('Enter a direction (north, south, east, west) or exit: ').lower()

    if command == 'exit':
        current_room = 'exit'
        print('You have exited the game.')

    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
        print('You moved to the', current_room)

    else:
        print('Invalid command. You cannot move in that direction.')
