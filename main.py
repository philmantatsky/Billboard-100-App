import random
random.seed(5) #Do not delete this line!!
artist_songs = { "Shaboozey":["A Bar Song (Tipsy)"] ,  "SabrinaCarpenter":["Taste","Please Please Please","Espresso"]  , "PostMalone": ["I Had Some Help","Pour Me A Drink", "Guy For That"] ,"BillieEilish" : ["Birds Of A Feather","Wildflower"] }

#Milestone 1 - Task 1: Ask the user for a command 
command = input("Enter command: ")

#Milestone 1 - Task 2: Split the command 
space_index = command.index(" ")
first_word = command[:space_index]
second_word = command[space_index + 1:]
print(f"First word of the command is: {first_word}")
print(f"Second word of the command is: {second_word}\n")
#Milestone 1 - Task 3: Top hit?
if first_word == "RandomSong" or second_word == "AllHits" or second_word not in artist_songs.keys() or (first_word != "Songs" and first_word != "RandomSong"):
    top_hit = ""
else:
    top_hit = input("Tophit ? (yes/no):")
#Submit for grading right here!
#Continue milestones 2 ,3 and 4  below!
if top_hit == "yes":
    print(f" My Song Choice: \n{artist_songs[second_word][0]}")
elif top_hit == "no":
    print(f" My Song Choice: \n{artist_songs[second_word]}")
if first_word == "RandomSong" and second_word in artist_songs.keys():
    rand = random.randint(0, len(artist_songs[second_word]) - 1)
    print("My Song Choice: ")
    print(artist_songs[second_word][rand])
if second_word == "AllHits":
    print("My Song Choice: ")
    print(list(artist_songs.values()))
if first_word == "Songs":
    if second_word != "AllHits" and (second_word not in artist_songs.keys()):
        print(f'Incorrect second command {second_word}, should be "AllHits" or the Artist\'s Name instead.')
if first_word == "RandomSong":
    if second_word not in artist_songs.keys():
        print(f"Incorrect second command {second_word}, should be the Artist's Name instead.")
if top_hit != "yes" and top_hit != "no" and top_hit != "":
    print(' Incorrect choice, should be "yes" or "no".')
if first_word != "Songs" and first_word != "RandomSong":
    print(f'Incorrect first command {first_word}, should be "Songs" or "RandomSong" instead.')