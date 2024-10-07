import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
"""
)


def list_all_videos():
    cursor.execute("SELECT  * FROM videos ")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    con.commit()


def update_video(video_id, name, time):
    cursor.execute(
        "UPDATE videos SET name = ? ,time = ?  WHERE id = ? ", (name, time, video_id)
    )
    con.commit()


def delete_video(video_id):
    cursor.execute(
        "DELETE FROM videos WHERE id = ?",
        (video_id),
    )
    con.commit()


def main():
    while True:
        print("\n Youtube manager || choose a option")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit")

        choice = input("Enter your choice :")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                name = input("Enter the video name :")
                time = input("Enter video time : ")
                add_video(name, time)
            case "3":
                video_id = input("Enter video id to update: ")
                name = input("Enter the video name : ")
                time = input("Enter the video time : ")
                update_video(video_id, name, time)
            case "4":
                video_id = input("Enter video id to delete: ")
                delete_video(video_id)
            case _:
                print("Invalid choice")
    con.close()


if __name__ == "__main__":
    main()
