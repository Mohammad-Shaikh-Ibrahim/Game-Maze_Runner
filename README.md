# Maze Runner Game


# Overview

The Maze Runner Game is a Python-based game where you control a player navigating through a maze. The objective is to reach the exit before time runs out, while avoiding traps along the way. As you progress, the game becomes more challenging with more traps and a larger maze. The game features multiple levels, scoring, and a countdown timer.

# Features:

Multiple Levels: The game has multiple levels that get progressively harder. Each level increases the number of traps and the complexity of the maze.

Timer: You must reach the exit before time runs out. The timer counts down from 60 seconds for each level.

Scoring System: The player earns points by reaching the exit and loses points by hitting traps. The score affects the level of difficulty.

Traps: Traps are placed randomly throughout the maze, and if the player hits one, the game ends.

Exit: The player wins by reaching the exit (marked by a green square). After reaching the exit, the player moves on to the next level.

# Requirements:

Python 3.x (Ensure Python 3 is installed on your machine)

Tkinter (Used for the GUI and game rendering)

# How to Play:

Start the Game: Run the Python script to begin playing.

Movement: Use the arrow keys (↑, ↓, ←, →) to move the player through the maze.

Avoid Traps: Be careful not to hit the traps (red squares). If you do, you lose points and the game ends.

Reach the Exit: To win the game, reach the exit (green square) before time runs out. Each time you reach the exit, you advance to a more difficult level.

Scoring: Each exit you reach adds 100 points, and hitting a trap deducts 10 points from your score.

# How to Run:

Ensure you have Python 3.x installed on your computer.

## Install Tkinter (if it’s not installed by default): pip install tk

Save the Python script as maze_runner_game.py.

## Run the script using Python: python maze_runner_game.py

Use the arrow keys to navigate the maze and avoid traps.

# Game Controls:

Up Arrow: Move Up

Down Arrow: Move Down

Left Arrow: Move Left

Right Arrow: Move Right

# Game Logic:

Levels: The game consists of multiple levels. Each level increases the number of traps and the complexity of the maze.

Timer: You have a limited amount of time (60 seconds) to reach the exit in each level. If time runs out, the game ends.

Traps: Traps are randomly placed in the maze. If the player hits a trap, the game ends, and they lose points.

Exit: To proceed to the next level, the player must reach the exit. The game automatically generates a new maze for each level.

Score: The score increases by 100 points each time the player reaches the exit. If the player hits a trap, 10 points are deducted.

# Example Output:
Level 1: 60 seconds, 5 traps.
Level 2: 50 seconds, 10 traps.
Level 3: 40 seconds, 15 traps.
As the levels increase, the maze gets more difficult, and the player must navigate through more traps to reach the exit.

# Future Enhancements:
Power-ups: Add power-ups like extra time or trap detection.

Enemies: Add moving obstacles or enemies that chase the player.

## Leaderboards: Keep track of high scores and allow the player to compete for the best score.

# License:

This project is open-source and available under the MIT License.
