import json

# load the data with error handling
def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return[]

# helper method to add video in file
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)   

# list of all video
def list_all_videos(videos):
    print("\n")
    print("*" * 70)

    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")

    print("\n")    
    print("*" * 70)

# adding video and time
def add_video(videos):
    name = input("Enter video title: ")
    time = input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1<= index  <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter  the new time: ")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("invalid index selected")    
def delete_video(videos):
     list_all_videos(videos)
     index = int(input("Enter the video index to delete: "))
     if 1 <= index  <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
     else:
        print("Invalid index")    

        
            

def main():
    videos = load_data()
    while True:
        print("\n YOUTUBE MANAGER | choose an option")
        print("1. List all youtube video")
        print("2. Add a youtube video")
        print("3. update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your Choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("invalid choice")

if  __name__ == "__main__":
    main()                
        




