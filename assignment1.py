"""
Name: Soe Htet Naung
Date started:26 April 2020 (5pm)
GitHub URL:https://github.com/JCUS-CP1404/assignment-01-songs-app-Soe-Htet-Naung
"""
"""
This Program will help the users to make a list of the songs that the users wished to be learn
and keep track of the updated status of the learned songs and unlearned songs in the list.
The users may add more songs to the list and mark the songs as learned when they choose to complete them.
"""


def main():
    """The main function will handle the menu input part and the rest by calling other functions"""
    print("Songs to Learn 1.0 - by Soe Htet Naung")
    songs = initialize_songs()  # get song list
    menu_choice = main_menu()   # output the main menu
    while menu_choice != "q":
        if menu_choice == "l":
            list_songs(songs)   # show the list of songs and get unlearned value
        elif menu_choice == "a":
            songs = add_songs(songs)  # add new song to the song list
        elif menu_choice == "c":
            songs = complete_songs(songs)  # mark newly learned songs
        else:
            print("Invalid Menu choice.")  # error handling for unaccepted menu choices
            pass
        menu_choice = main_menu()
    exit_function(songs)


def main_menu():
    print("Menu:\nL - List songs\nA - Add songs\nC - Complete a song\nQ - Quit")
    return input(">>> ").lower().strip()    # handle the case errors and extra spaces


# Open the csv file, read it to get how many songs are in the file, then return the list of songs
def initialize_songs():
    song_file = open("songs.csv", "r")
    song_count = 0
    song_list = []
    for song in song_file:
        detail = song.strip('\n').split(',')
        song_list.append(detail)
        song_count += 1
    print(song_count, "songs loaded")
    song_file.close()
    return song_list


# this function will format the songs before the song list printed out
# and check which songs are marked as learned and which are not.
def list_songs(songs):
    unlearned = 0
    learned = 0
    for song in songs:
        if song[3] == "u":
            print("{}. * {:42} - {:25} ({})".format(songs.index(song), song[0], song[1], song[2]))
            unlearned += 1
        else:
            print("{}.   {:42} - {:25} ({})".format(songs.index(song), song[0], song[1], song[2]))
            learned += 1
    print("{} songs learned, {} songs still to learn.".format(learned, unlearned))


# this function will add new songs into the csv file by asking users to fill in the required inputs
def add_songs(songs):
    title = input("Title: ")
    while title.strip() == "":  # error handling for blank values
        print("Input cannot be blank")
        title = input("Title: ")
    artist = input("Artist: ")
    while artist.strip() == "":
        print("Input cannot be blank")
        artist = input("Artist: ")
    year = check_number("Year: ")  # used check_number function to handle the input errors
    while year < 0 or year is None:
        print("Number must be >= 0")
        year = check_number("Year: ")
    print("{} ({} from {}) added to song list.".format(title, artist, year))
    songs.append([title, artist, year, "u"])
    return songs


# this function will check if the number is a valid number or other values
# it will also handle the error by showing error message and will ask the user to input a valid number
def check_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print("Invalid input! please enter a valid number")
    return value


# this function will mark the songs that are learned with the help of user input
def complete_songs(songs):
    unlearned = 0
    for song in songs:
        if song[3] == "u":
            unlearned += 1
    if unlearned == 0:
        print("No more songs to learn")
    else:
        print("Enter the number of a song to mark as learned")
        while True:  # error handling to check invalid user inputs by comparing the input with the existing song numbers
            song = check_number(">>> ")
            if song < 0 or song is None:  # error handling for the inputs lower than the numbers in list and other value
                print("Number must be >= 0")
                continue  # go back to the start of the loop
            elif song >= len(songs):    # error handling for the inputs that are greater than numbers in list
                print("Invalid song number")
                continue
            else:
                break   # exist the loop
        if songs[song][3] == "l":  # check if the song is learned
            print("You have already learned {}".format(songs[song][0]))
        else:  # if the song is not learned, marked as learned
            songs[song][3] = "l"
            print("{} by {} learned.".format(songs[song][0], songs[song][1]))
    return songs


# this function will save/rewrite the new song list and
# recount the total song numbers to show as a output before closing the file
def exit_function(songs):
    song_file = open("songs.csv", "w")
    song_counter = 0
    for song in songs:
        song_file.write(','.join(str(category) for category in song))
        song_file.write('\n')
        song_counter += 1
    print(song_counter, "saved to songs.csv\nHave a nice Day :)")
    song_file.close()


if __name__ == '__main__':
    main()
