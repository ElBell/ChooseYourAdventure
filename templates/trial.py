# -*- coding: utf-8 -*-
"""
Text Adventure Game
An adventure in making adventure games.

To test your current solution, run the `test_my_solution.py` file.

Refer to the instructions on Canavs for more information.

"I have neither given nor received help on this assignment."
author: YOUR NAME HERE
"""
__version__ = 2


# 2) print_introduction: Print a friendly welcome message for your game
def print_introduction():
    print("== The Spooky Adventure ==")
    print("    = By Dr. Bart =")
    print("")
    print("After getting lost in the woods near your house, you stumble into a clearing.")


# 3) get_initial_state: Create the starting player state dictionary
def get_initial_state():
    return {"game status": "playing",
            "location": "Yard",
            "Unused": None,
            "Unused 2": None,
            "has key": False}


# 4) print_current_state: Print some text describing the current game world
def print_current_state(player):
    print("*" * 40)
    print("You are in", player['location'])
    if player['location'] == 'Yard':
        print("There is a house ahead of you, and the forest behind you.")
    elif player['location'] == 'Forest':
        print("You are likely to be eaten by a Grue.")
        if not player['has key']:
            print("But... is that a key on the ground?")
    elif player['location'] == 'Living Room':
        print("You see stairs, and what appears to be a dining room.")
    elif player['location'] == "Dining Room":
        print("There appears to be old, rotting food on the table.")
    elif player['location'] == "Upstairs":
        print("There is a locked door.")
    if player['has key']:
        print("You have a key.")


# 5) get_options: Return a list of commands available to the player right now
def get_options(player):
    if player['location'] == 'Yard':
        return ['Leave yard', 'Enter house']
    elif player['location'] == 'Forest':
        if player['has key']:
            return ['Enter yard']
        else:
            return ['Enter yard', 'Get key']
    elif player['location'] == "Living Room":
        return ['Dining room', 'Leave house', 'Go upstairs']
    elif player['location'] == "Dining Room":
        return ['Eat food', 'Living room']
    elif player['location'] == "Upstairs":
        if player['has key']:
            return ['Go downstairs', 'Enter locked room']
        else:
            return ['Go downstairs']


# 6) print_options: Print out the list of commands available
def print_options(options):
    print("Choose a command:")
    for option in options:
        print("\t", option)


# 7) get_user_input: Repeatedly prompt the user to choose a valid command
def get_user_input(options):
    command = ""
    options = [o.lower() for o in options]
    while command.lower() not in options and command != "quit":
        command = input("Type your command:")
    return command


# 8) process_command: Change the player state dictionary based on the command
def process_command(command, player):
    if command in ("Enter yard", "Leave house"):
        player['location'] = "Yard"
    elif command in ("Leave yard",):
        player['location'] = "Forest"
    elif command in ("Get key",):
        player['has key'] = True
    elif command in ("Enter house", "Living room", "Go downstairs"):
        player['location'] = "Living Room"
    elif command in ("Eat food",):
        player['game status'] = 'lost'
    elif command in ("Dining room",):
        player['location'] = "Dining Room"
    elif command in ("Go upstairs",):
        player['location'] = 'Upstairs'
    elif command in ("Enter locked room",):
        player['game status'] = 'won'
    elif command == "quit":
        player['game status'] = 'quit'


# 9) print_game_ending: Print a victory, lose, or quit message at the end
def print_game_ending(player):
    if player['game status'] == 'won':
        print("Wait, this is your room.")
        print("Hey! You live here! This is your house!")
        print("You should probably take better care of it.")
    elif player['game status'] == 'lost':
        print("The food is gross and squishy in your hands, but you eat it anyway.")
        print("You start feeling sick, and pass out.")
        print("As your vision fades, you have one last thought:")
        print('"You really should not have eaten that food."')
    else:
        print("You quit the game. But what will ever come of you..?")


# Command Paths to give to the unit tester
WIN_PATH = ["Leave yard", "Get key", "Enter yard", "Enter house",
            "Go upstairs", "Bedroom", "Enter locked room"]
LOSE_PATH = ["Enter house", "Dining room", "Eat food"]


# 1) Main function that runs your game, read it over and understand
# how the player state flows between functions.
def main():
    # Print an introduction to the game
    print_introduction()
    # Make initial state
    the_player = get_initial_state()
    # Check victory or defeat
    while the_player['game status'] == 'playing':
        # Give current state
        print_current_state(the_player)
        # Get options
        available_options = get_options(the_player)
        # Give next options
        print_options(available_options)
        # Get Valid User Input
        chosen_command = get_user_input(available_options)
        # Process Comands and change state
        process_command(chosen_command, the_player)
    # Give user message
    print_game_ending(the_player)


# Executes the main function
if __name__ == "__main__":
    '''
    You might comment out the main function and call each function
    one at a time below to try them out yourself '''
    main()
    # e.g., comment out main() and uncomment the line(s) below
    # print_introduction()
    # print(get_initial_state())
    # ...
