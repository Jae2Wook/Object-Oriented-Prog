from collections import deque

cars = deque()
cars.append("Ford")
cars.append("Mazda")
cars.append("Dodge")

for car in cars:
    print(car)


class Song:

    def __init(self):
        self.title = ""
        self.artist = ""

    def prompt(self):
        self.title = input("Enter the title: ")
        self.artist = input("Enter the artist: ")

    def display(self):
        print("Playing song:")
        print("{} by {}".format(self.title, self.artist))

def main():
    s_list = deque()
    #songs = Song()
    opt = 0
    while opt != 4 :
        songs = Song()
        print(s_list)
        print("Options:")
        print("1. Add a new song to the end of the playlist")
        print("2. Insert a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        opt = int(input("Enter selection: "))
        print()

        if (opt == 1):
            #songs = Song()
            songs.prompt()
            s_list.append(songs)  #not songs.prompt() it is songs which holds self.title and self.artist
            print()
        elif (opt == 2):
            #songs = Song()
            songs.prompt()
            s_list.appendleft(songs)
            print()
        elif (opt == 3):
            if len(s_list) == 0:
                print("The playlist is currently empty.")
                print()
            else:
                songs = s_list.popleft()
                songs.display()
                print()

    print("Goodbye")

if __name__ == "__main__":
    main()