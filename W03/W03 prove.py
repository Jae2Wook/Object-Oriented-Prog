class Bot:

    def __init__(self): # "self" links all the self. member data through functions in the class
        self.x_cord = 10  #member data
        self.y_cord = 10
        self.fuel_amnt = 100

    def move_left(self):
        if self.fuel_amnt < 5: #less than 5 because I can move when I have 5 fuel
            print("Insufficient fuel to perfrom action.")
        else:
            self.x_cord -= 1
            self.fuel_amnt -= 5

    def move_right(self):
        if self.fuel_amnt < 5:
            print("Insufficient fuel to perfrom action.")
        else:
            self.x_cord += 1
            self.fuel_amnt -= 5
        
    def move_up(self):
        if self.fuel_amnt < 5:
            print("Insufficient fuel to perfrom action.")
        else:
            self.y_cord -= 1
            self.fuel_amnt -= 5
        
    def move_down(self):
        if self.fuel_amnt < 5:
            print("Insufficient fuel to perfrom action.")
        else:
            self.y_cord += 1
            self.fuel_amnt -= 5

    def act_fire(self):
        if self.fuel_amnt < 15:
            print("Insufficient fuel to perfrom action.")
        else:
            self.fuel_amnt -= 15
            print("Pew! Pew!")

    def display_status(self):
        print("({}, {}) - Fuel: {}".format(self.x_cord, self.y_cord, self.fuel_amnt))

def main():
    print('Commands: "left", "right", "up", "down", "fire", "status", "quit"')
    robot = Bot()     #robot can use Bot class's functions
    robot.display_status()
    command = ""              #going into the while loop
    while command != "quit":
        command = input("Enter command: ")
        if command == "left":
            robot.move_left()

        elif command == "right":
            robot.move_right()

        elif command == "up":
            robot.move_up()

        elif command == "down":
            robot.move_down()

        elif command == "fire":
            robot.act_fire()

        elif command == "status":
            robot.display_status()

    print("Goodbye")

if __name__ == "__main__":
    main()