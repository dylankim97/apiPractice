import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "Zico", "view": 1000, "likes": 99},
        {"name": "Swings", "view": 999, "likes": 30},
        {"name": "Esens", "view": 9923, "likes": 99099}]


def main():
    exitProgram = False

    while exitProgram is not True:
        answer = input("get a video?(getbyid). post a video?(post). delete a video?(del) Exit the program?(exit)")

        if answer == "exit":
            exitProgram = True
            break

        perform(answer)


def perform(answer):

    if answer == "post":
        #name = input("name of the vid?")
        #view = input("how many views?")
        #likes = input("how many likes?")
        #id = input("what is the id?")
        #requests.put(BASE + f"video/{id}", {"name": name, "view": view, "likes": likes})
        for i in range(len(data)):
            requests.put(BASE + "video/" + str(i), data[i])


    elif answer == "getbyid":
        video_id = input("What is the id of the video?")
        response = requests.get(BASE + "video/" + str(video_id))
        print(response.json())

    elif answer == "del":
        video_id = input("What is the id of the video?")
        response = requests.delete(BASE + "video/" + str(video_id))


if __name__ == "__main__":
    main()