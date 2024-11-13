import tkinter as tk
from tkinter import messagebox
import random

# Constants
CELL_SIZE = 40
ROWS, COLS = 15, 15
TIME_LIMIT = 60  # Time limit in seconds

# Initialize player position
player_pos = [1, 1]  # Starting position

# Create main window
root = tk.Tk()
root.title("Maze Runner")
root.geometry(f"{COLS * CELL_SIZE + 20}x{ROWS * CELL_SIZE + 120}")
root.config(bg="#f0f0f0")  # Light background color

# Create the canvas for the maze
canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="lightgray", bd=0)
canvas.pack(pady=20)

# Timer display at the top with improved font
timer_label = tk.Label(root, text=f"Time Left: {TIME_LIMIT}", font=("Verdana", 16, "bold"), bg="#f0f0f0", fg="darkgreen")
timer_label.pack()

# Instructions at the bottom with updated font and color
instructions_label = tk.Label(root, text="Use arrow keys to move: ↑ ↓ ← →", font=("Verdana", 12), bg="#f0f0f0", fg="darkblue")
instructions_label.pack(pady=10)

# Maze generation function to guarantee solvability
def generate_maze(rows, cols):
    # Create an empty grid of walls
    maze = [["#" for _ in range(cols)] for _ in range(rows)]
    
    # Start and exit positions
    maze[1][1] = "P"  # Player starts here
    maze[rows - 2][cols - 2] = "E"  # Exit is here

    # Use Depth-First Search (DFS) to create a path
    def dfs(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)  # Shuffle directions for randomness
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 1 <= nx < rows - 1 and 1 <= ny < cols - 1 and maze[nx][ny] == "#":
                maze[nx][ny] = " "  # Make the new cell a path
                maze[x + dx][y + dy] = " "  # Open the wall between cells
                dfs(nx, ny)  # Recursively visit the next cell

    # Start DFS from the player's position (1, 1)
    dfs(1, 1)

    # Add random traps, but don't place them on the exit or player
    for _ in range(10):
        x, y = random.randint(1, rows - 2), random.randint(1, cols - 2)
        if maze[x][y] == " " and (x, y) != (rows - 2, cols - 2) and (x, y) != (1, 1):
            maze[x][y] = "T"

    return maze

maze = generate_maze(ROWS, COLS)

# Draw the maze with creative visual elements
def draw_maze():
    canvas.delete("all")
    for row in range(ROWS):
        for col in range(COLS):
            x1, y1 = col * CELL_SIZE, row * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            if maze[row][col] == "#":  # Wall
                canvas.create_rectangle(x1, y1, x2, y2, fill="darkgray", outline="black", width=2)
            elif maze[row][col] == " ":  # Path
                canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black", width=1)
            elif maze[row][col] == "P":  # Player
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black", width=2)
            elif maze[row][col] == "E":  # Exit
                canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black", width=2)
            elif maze[row][col] == "T":  # Trap
                canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black", width=2)

# Move player within the maze
def move_player(dx, dy):
    global player_pos
    x, y = player_pos
    new_x, new_y = x + dx, y + dy

    # Check for boundaries and wall collisions
    if 0 <= new_x < ROWS and 0 <= new_y < COLS and maze[new_x][new_y] != "#":
        if maze[new_x][new_y] == "E":
            messagebox.showinfo("Maze Runner", "Congratulations! You've reached the exit!", icon="info")
            root.quit()
        elif maze[new_x][new_y] == "T":
            messagebox.showwarning("Maze Runner", "You hit a trap! Game Over.", icon="warning")
            root.quit()
        else:
            # Update maze and player position
            maze[x][y] = " "
            player_pos = [new_x, new_y]
            maze[new_x][new_y] = "P"
            draw_maze()

# Handle key presses for movement
def on_key_press(event):
    key = event.keysym
    if key == "Up":
        move_player(-1, 0)
    elif key == "Down":
        move_player(1, 0)
    elif key == "Left":
        move_player(0, -1)
    elif key == "Right":
        move_player(0, 1)

# Timer function
def update_timer():
    time_left = int(timer_label.cget("text").split(": ")[1])
    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left - 1}")
        root.after(1000, update_timer)
    else:
        messagebox.showinfo("Maze Runner", "Time's up! Game Over.", icon="error")
        root.quit()

# Start game function to initialize timer and draw maze
def start_game():
    # Clear instructions and start button
    instructions_label.pack_forget()

    # Start the timer and the game
    draw_maze()
    update_timer()

# Create a stylish start button with hover, pressed, and gradient effects
def on_hover(event):
    start_button.config(bg="#45a049", fg="white")

def on_leave(event):
    start_button.config(bg="#4CAF50", fg="white")

def on_click(event):
    start_button.config(bg="#388e3c", fg="white")

def on_release(event):
    start_button.config(bg="#45a049", fg="white")

start_button = tk.Button(
    root,
    text="Start Game",
    font=("Verdana", 14, "bold"),
    width=20,
    height=2,
    relief="flat",
    bg="#4CAF50",
    fg="white",
    command=start_game
)
start_button.pack(pady=30)

# Adding more button interactions
start_button.bind("<Enter>", on_hover)
start_button.bind("<Leave>", on_leave)
start_button.bind("<Button-1>", on_click)
start_button.bind("<ButtonRelease-1>", on_release)

# Bind arrow keys for movement
root.bind("<Up>", on_key_press)
root.bind("<Down>", on_key_press)
root.bind("<Left>", on_key_press)
root.bind("<Right>", on_key_press)

# Start the main event loop
root.mainloop()
