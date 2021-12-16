import os
import pprint
from requests import get, post, delete, put
import json
pp = pprint.PrettyPrinter(indent=4,depth=20)

url = "http://127.0.0.1:5000/"
users = url + "users/"
musics = url + "musics/"
playlists = url + "playlist/"


def clear_terminal():
    os.system('clear')


def make_user():
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    return {"username": username, 'email': email, 'password': password}


# "username": "string",
#  "email": "string",
#  "password": "string",


def make_music():
    name = input("Name: ")
    artist = input("Artist: ")
    album = input("Album: ")
    return {'name': name, 'artist': artist, 'album': album}


# "artist": "string",
#   "album": "string",
#   "name": "string",

def make_playlist():
    name = input("Name: ")
    user_id = input("User id: ")
    music_list = [ int(x) for x in input("Music List (separated by white-space): ").split(" ")]
    return {'name': name, 'user_id': user_id, 'musics_list': music_list}

    # "name": "string",
    # "user_id": 0,
    # "musics_list": [
    #     0


def ask_id():
    print("Id:", end=" ")
    answer = input()
    return answer


def user_request(request_type):
    if request_type == 0:
        return get(users).json()
    elif request_type == 1:
        user_id = ask_id()
        return get(users + str(user_id)).json()
    elif request_type == 2:
        payload = make_user()
        return post(users, json=payload)
    elif request_type == 3:
        user_id = ask_id()
        pp.pprint(get(users + str(user_id)).json())
        payload = make_user()
        return put(users + str(user_id), json=payload)
    elif request_type == 4:
        user_id = ask_id()
        return delete(users + str(user_id))
    else:
        return ""

    # menu = "0 - Get All\n1 - Get\n2 - Post\n3 - Put\n4 - Delete"


def music_request(request_type):
    if request_type == 0:
        return get(musics).json()
    elif request_type == 1:
        music_id = ask_id()
        return get(musics + str(music_id)).json()
    elif request_type == 2:
        payload = make_music()
        return post(musics, json=payload)
    elif request_type == 3:
        music_id = ask_id()
        pp.pprint(get(musics + str(music_id)).json())
        payload = make_music()
        return put(musics + str(music_id), json=payload)
    elif request_type == 4:
        music_id = ask_id()
        return delete(musics + str(music_id))

    # menu = "0 - Get All\n1 - Get\n2 - Post\n3 - Put\n4 - Delete"

def playlist_request(request_type):
    if request_type == 0:
        return get(playlists).json()
    elif request_type == 1:
        playlist_id = ask_id()
        return get(playlists + str(playlist_id)).json()
    elif request_type == 2:
        payload = make_playlist()
        return post(playlists, json=payload)
    elif request_type == 3:
        playlist_id = ask_id()
        pp.pprint(get(playlists + str(playlist_id)).json())
        payload = make_playlist()
        return put(playlists + str(playlist_id), json=payload)
    elif request_type == 4:
        playlist_id = ask_id()
        return delete(playlists + str(playlist_id))
    elif request_type == 5:
        music_id = ask_id()
        music_url = f"{playlists}music/{music_id}"
        return get(music_url).json()
    elif request_type == 6:
        user_id = ask_id()
        user_url = f"{playlists}user/{user_id}"
        return get(user_url).json()



def menu_model():
    menu = "0 - User\n1 - Music\n2 - PlayList"
    print(menu)


def menu_request(choice=None):
    menu = "0 - Get All\n1 - Get\n2 - Post\n3 - Put\n4 - Delete"
    if choice == 2:
        print(menu + "\n5 - GetAll by Music\n6 - GetAll By User")
    else:
        print(menu)


def request(choice, request_type):
    if choice == 0:
        return user_request(request_type)
    elif choice == 1:
        return music_request(request_type)
    elif choice == 2:
        return playlist_request(request_type)


def main():
    while True:
        clear_terminal()
        menu_model()
        choice = int(input())
        menu_request(choice)
        request_type = int(input())
        stuff = request(choice, request_type)
        clear_terminal()
        json_formatted_str = json.dumps(stuff, indent=4)
        print(json_formatted_str)
        # pp.pprint(stuff)
        input()


if __name__ == '__main__':
    main()
