import enchant
import time

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
    song_removed = False
    for song, song_dict in list(my_dict.items()):
        if song_dict["artist"].lower() == maya_artist.lower():
            my_dict.pop(song)
            song_removed = True
            print(f"Song of {maya_artist}, removed successfully.")
    if not song_removed:
        print("No songs for that artist.")
    return my_dict


def is_israeli(song_details):
    return song_details["genre"].lower() == "israeli"


def israeli_dict(og_dict):
    new_dict = {}
    for song, details in og_dict.items():
        if is_israeli(og_dict[song]):
            minutes = int(details["duration"][0])
            seconds = int(details["duration"][1])
            if minutes < 3 or (minutes == 3 and seconds <= 30):
                new_dict[song] = details

    return new_dict



def sleep_timer(song_dict):
    timer_seconds = int(input("How many minutes do you want ot hear music? ")) * 60
    while True:
        for song, details in song_dict.items():
            print(f"{song} is playing")
            song_duration_seconds = details["duration"][0] * 60 + details["duration"][1]
            for _ in range(song_duration_seconds):
                time.sleep(0.01)
                timer_seconds-=1
                if timer_seconds <= 0:
                    print("Time is up playlist not finished!")
                    return

        print("Playlist Over!")
        break

def shift(list_of_nums, num_of_shifts):
    new_list = []
    real_shift = num_of_shifts%len(list_of_nums)
    for i in range(real_shift, len(list_of_nums)):
        new_list.append(list_of_nums[i])
    for i in range(0, real_shift):
        new_list.append(list_of_nums[i])

    return new_list


def main():
    print_dict(liked_songs)
    my_dict = maya_check(liked_songs)
    my_dict = maya_dont_like_artists(my_dict)
    print_dict(my_dict)
    israeli = israeli_dict(my_dict)
    print(israeli)
    sleep_timer(my_dict)
    print(shift([1,2,3,4,5,6,7,8,9], 10))


main()