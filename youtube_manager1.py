import json


def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, videos in enumerate(videos, start=1):
        print(f"{index}.{videos['name']},Duration:{videos['time']}")
    print("\n")
    print("*" * 50)


def add_video(videos):
    name = input("Enter video name :")
    time = input("Enter video time :")
    videos.append({"name": name, "time": time})
    save_data(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter the video name : ")
        time = input("Enter the video timed name :")
        videos[index - 1] = {"name": name, "time": time}
        save_data(videos)
    else:
        print("Invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted : "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data(videos)
    else:
        print("Invalid video index")


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def main():
    videos = load_data()
    while True:
        print("/n Youtube manager || Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter an option : ")

        print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid option")


if __name__ == "__main__":
    main()
