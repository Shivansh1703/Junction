import os
import platform
import time

def clear_screen():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

class Game:
    def __init__(self):
        self.map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "P", " ", "#", " ", " ", " ", "#", "T", "#"],
            ["#", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
            ["#", " ", "#", "#", " ", "#", "#", " ", "#", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ]
        self.player_pos = [1, 1]

    def print_map(self):
        for row in self.map:
            print("".join(row))

    def move(self, direction):
        x, y = self.player_pos
        if direction == "up":
            if self.map[y-1][x] != "#":
                self.map[y][x] = " "
                self.map[y-1][x] = "P"
                self.player_pos = [x, y-1]
        elif direction == "down":
            if self.map[y+1][x] != "#":
                self.map[y][x] = " "
                self.map[y+1][x] = "P"
                self.player_pos = [x, y+1]
        elif direction == "left":
            if self.map[y][x-1] != "#":
                self.map[y][x] = " "
                self.map[y][x-1] = "P"
                self.player_pos = [x-1, y]
        elif direction == "right":
            if self.map[y][x+1] != "#":
                self.map[y][x] = " "
                self.map[y][x+1] = "P"
                self.player_pos = [x+1, y]

    def check_win(self):
        x, y = self.player_pos
        return self.map[y][x+1] == "T"

def main():
    game = Game()
    print("Welcome to Code Adventure!")
    time.sleep(1)
    print("Reach the treasure (T) by navigating the maze with commands.")
    print("Available commands: move_up(), move_down(), move_left(), move_right()")
    time.sleep(2)

    def move_up():
        game.move("up")

    def move_down():
        game.move("down")

    def move_left():
        game.move("left")

    def move_right():
        game.move("right")

    while not game.check_win():
        clear_screen()
        game.print_map()
        try:
            command = input("Enter your command: ")
            eval(command)  # Execute the entered command
        except Exception as e:
            print("Invalid command! Use move_up(), move_down(), move_left(), or move_right().")
            time.sleep(1)

    print("Congratulations! You've found the treasure!")

if __name__ == "__main__":
    main()
