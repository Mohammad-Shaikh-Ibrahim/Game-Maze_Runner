import tkinter as tk
from tkinter import messagebox
import random
import time

# Constants
ROWS = 15
COLS = 15
TRAP_COUNT = 5
TIMER_LIMIT = 60  # Time in seconds
LEVELS = 3  # Number of difficulty levels

# Initialize the maze and player position
maze = [[" " for _ in range(COLS)] for _ in range(ROWS)]
player_pos = [1, 1]
exit_pos = [ROWS - 2, COLS - 2]

# Create the Tkinter window
root = tk.Tk()
root.title("Maze Runner Game")

# Create a canvas to draw the maze
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Timer variables
timer = TIMER_LIMIT
time_remaining = tk.Label(root, text=f"Time: {timer}s", font=("Arial", 14))
time_remaining.pack()

# Instructions Label
instructions = tk.Label(root, text="Use arrow keys to move. Reach the exit before time runs out!", font=("Arial", 10))
instructions.pack()

# Player Score
score = 0
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 14))
score_label.pack()

# Maze generation using depth-first search
def generate_maze(level=1):
    global maze, player_pos, exit_pos, TRAP_COUNT
    maze = [["#" for _ in range(COLS)] for _ in range(ROWS)]

    # Modify trap count and maze size based on level
    TRAP_COUNT = 5 * level
    player_pos = [1, 1]
    exit_pos = [ROWS - 2, COLS - 2]

    # Create a simple path from (1,1) to the exit (ROWS-2, COLS-2)
    def carve_path(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < ROWS - 1 and 1 <= ny < COLS - 1 and maze[nx][ny] == "#":
                maze[nx][ny] = " "
                carve_path(nx, ny)

    # Carve the path from the start (1,1)
    maze[1][1] = " "
    carve_path(1, 1)
    
    # Place the exit
    maze[ROWS - 2][COLS - 2] = "E"
    
    # Add traps randomly
    traps_placed = 0
    while traps_placed < TRAP_COUNT:
        trap_x = random.randint(1, ROWS - 2)
        trap_y = random.randint(1, COLS - 2)
        if maze[trap_x][trap_y] == " ":
            maze[trap_x][trap_y] = "T"
            traps_placed += 1

# Function to draw the maze on the canvas
def draw_maze():
    canvas.delete("all")
    for i in range(ROWS):
        for j in range(COLS):
            x0 = j * 40
            y0 = i * 40
            x1 = x0 + 40
            y1 = y0 + 40
            if maze[i][j] == "#":
                canvas.create_rectangle(x0, y0, x1, y1, fill="black")
            elif maze[i][j] == " ":
                canvas.create_rectangle(x0, y0, x1, y1, fill="white")
            elif maze[i][j] == "T":
                canvas.create_rectangle(x0, y0, x1, y1, fill="red")
            elif maze[i][j] == "E":
                canvas.create_rectangle(x0, y0, x1, y1, fill="green")
            elif maze[i][j] == "P":
                canvas.create_rectangle(x0, y0, x1, y1, fill="yellow")

    # Draw player
    player_x, player_y = player_pos
    px0 = player_y * 40
    py0 = player_x * 40
    px1 = px0 + 40
    py1 = py0 + 40
    canvas.create_rectangle(px0, py0, px1, py1, fill="blue")

# Function to move the player
def move_player(dx, dy):
    global player_pos, maze, timer, score
    x, y = player_pos
    new_x, new_y = x + dx, y + dy
    
    # Check for boundaries and wall collisions
    if 0 <= new_x < ROWS and 0 <= new_y < COLS and maze[new_x][new_y] != "#":
        if maze[new_x][new_y] == "E":
            score += 100  # Add score for reaching the exit
            score_label.config(text=f"Score: {score}")
            messagebox.showinfo("Maze Runner", "Congratulations! You've reached the exit!", icon="info")
            level_up()  # Proceed to the next level
        elif maze[new_x][new_y] == "T":
            score -= 10  # Deduct points for hitting a trap
            score_label.config(text=f"Score: {score}")
            messagebox.showwarning("Maze Runner", "You hit a trap! Game Over.", icon="warning")
            level_up()  # Proceed to the next level
        else:
            # Update maze and player position
            maze[x][y] = " "
            player_pos = [new_x, new_y]
            maze[new_x][new_y] = "P"
            draw_maze()

# Level up function to proceed to the next level
def level_up():
    global timer, score
    time.sleep(1)
    if timer > 0:
        level = (score // 100) + 1  # Increase difficulty based on score
        generate_maze(level)
        draw_maze()
        countdown()  # Restart timer for next level

# Functions to move the player using arrow keys
def move_up(event):
    move_player(-1, 0)

def move_down(event):
    move_player(1, 0)

def move_left(event):
    move_player(0, -1)

def move_right(event):
    move_player(0, 1)

# Bind the arrow keys to player movement
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Timer function to count down
def countdown():
    global timer
    if timer > 0:
        timer -= 1
        time_remaining.config(text=f"Time: {timer}s")
        root.after(1000, countdown)
    else:
        messagebox.showwarning("Maze Runner", "Time's up! Game Over.", icon="warning")
        root.quit()

# Start the game and timer
generate_maze()
draw_maze()
countdown()

# Start the game
root.mainloop()
