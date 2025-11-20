liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    },
    "Achshav Karov": {
        "artist": "Idan Raichel",
        "duration": (2, 26),
        "genre": "Israeli"
    },
    "Uf Gozal": {
            "artist": "Arik Einstein",
            "duration": (2, 56),
            "genre": "Israeli"
    },
    "Papi": {
            "artist": "Odeya",
            "duration": (2, 36),
            "genre": "Pop"
        },
}


def print_dict(my_dict):
    for item in my_dict:
        print(item)


def maya_check(my_dict):
    maya_song = input("Hi Maya what do you want to check? ")
    if maya_song in my_dict:
        maya_wants = input("Yeah that songs is in the playlist do you want to remove it? ")
        if maya_wants.lower() == "yes":
            liked_songs.pop(maya_song)
    else:
        print("No, the song doesn't exist in playlist")
    return my_dict

def maya_dont_like_artists(my_dict):
    maya_artist = input("Hi Maya what artist do you want to remove? ")
    for song, song_dict in list(my_dict.items()):
        if song_dict["artist"].lower() == maya_artist.lower():
            my_dict.pop(song)
            print(f"Songs of {maya_artist}, removed successfully")

    return my_dict

def main():
    print_dict(liked_songs)
    my_dict = maya_check(liked_songs)
    my_dict = maya_dont_like_artists(my_dict)
    print_dict(my_dict)


main()
