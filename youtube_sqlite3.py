import sqlite3

con = sqlite3.connect("youtube.db")

cur = con.cursor()

cur.execute('''

CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL

            ) 
''')
def list_all_video():
    cur.execute("SELECT * from videos")
    for row in cur.fetchall():
        print(row)   
def add_video(name,time):
    cur.execute("INSERT INTO videos(name,time) VALUES (?, ?)",(name,time))
    con.commit()
def update_list(index,new_name,new_time):
    cur.execute("Update videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,index))
    con.commit()
def delete_video(index):
    cur.execute
    ("DELETE FROM videos where id = ?",(index))
    con.commit()

def main():
    while True:
        print("\n YOUTUBE MANAGER | A APP WITH DB")
        print("1: List all the youtube video")
        print("2: Add a Youtube video")
        print("3: Update a youtube video")
        print("4: Delete a youtube video")
        print("5: Exit from the app")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_all_video()
        elif choice == 2:
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)
        elif choice == 3:
            index = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_list(index, name, time)
        elif choice == 4:
            index = input("Enter video ID to delete: ")
            delete_video(index)
        elif choice == 5:
            break    
        else:
            print("Invalid choice")                
    
    con.close()

if __name__ == "__main__":
    main()


