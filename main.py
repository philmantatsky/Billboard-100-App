    import random
    random.seed(5)  # Set a fixed seed for reproducibility in random selection

    # Dictionary of artists with their songs
    artist_songs = {
        "Shaboozey": ["A Bar Song (Tipsy)"],
        "SabrinaCarpenter": ["Taste", "Please Please Please", "Espresso"],
        "PostMalone": ["I Had Some Help", "Pour Me A Drink", "Guy For That"],
        "BillieEilish": ["Birds Of A Feather", "Wildflower"]
    }

    # Milestone 1 - Task 1: Ask the user for a command
    command = input("Enter command: ")

    # Milestone 1 - Task 2: Split the command into two parts
    space_index = command.index(" ")  # Find the first space in the command
    first_word = command[:space_index]  # Get the command type (first word)
    second_word = command[space_index + 1:]  # Get the argument (second word)
    print(f"First word of the command is: {first_word}")
    print(f"Second word of the command is: {second_word}\n")

    # Milestone 1 - Task 3: Determine if a top hit should be selected
    if first_word == "RandomSong" or second_word == "AllHits" or second_word not in artist_songs.keys() or (first_word != "Songs" and first_word != "RandomSong"):
        top_hit = ""  # If command is invalid or no top hit required, leave empty
    else:
        top_hit = input("Tophit ? (yes/no):")  # Ask if a top hit is desired

    # Evaluate user's input and generate a response
    if top_hit == "yes":  # If top hit selected
        print(f" My Song Choice: \n{artist_songs[second_word][0]}")  # First song for selected artist
    elif top_hit == "no":  # If top hit not selected
        print(f" My Song Choice: \n{artist_songs[second_word]}")  # List all songs for selected artist

    # Choose a random song if 'RandomSong' command with valid artist
    if first_word == "RandomSong" and second_word in artist_songs.keys():
        rand = random.randint(0, len(artist_songs[second_word]) - 1)  # Select random song index
        print("My Song Choice: ")
        print(artist_songs[second_word][rand])  # Display random song choice

    # Display all songs if 'AllHits' command
    if second_word == "AllHits":
        print("My Song Choice: ")
        print(list(artist_songs.values()))  # Display all songs for all artists

    # Handle incorrect command inputs with feedback messages
    if first_word == "Songs":
        if second_word != "AllHits" and (second_word not in artist_songs.keys()):
            print(f'Incorrect second command {second_word}, should be "AllHits" or the Artist\'s Name instead.')

    if first_word == "RandomSong":
        if second_word not in artist_songs.keys():
            print(f"Incorrect second command {second_word}, should be the Artist's Name instead.")

    # Handle incorrect top_hit response (not "yes" or "no")
    if top_hit != "yes" and top_hit != "no" and top_hit != "":
        print(' Incorrect choice, should be "yes" or "no".')

    # Handle incorrect first command
    if first_word != "Songs" and first_word != "RandomSong":
        print(f'Incorrect first command {first_word}, should be "Songs" or "RandomSong" instead.')
