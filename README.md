## Maze Runner Game

# Overview

Maze Runner is an interactive Python-based game where the player navigates through a maze to reach the exit. The maze is generated dynamically, ensuring each game session is unique. The player uses arrow keys to move, and they must avoid traps while trying to reach the exit before time runs out.

# The game features:

A randomly generated maze with walls, paths, traps, and an exit.

A countdown timer, which adds pressure to reach the exit.

A modern and interactive GUI built with Tkinter, featuring smooth button transitions and hover effects.

A player that moves through the maze, avoiding traps, and aiming to reach the exit.

# Features
Dynamic Maze Generation: The maze is generated randomly every time the game starts, making each game session different.

Traps: Random traps are placed in the maze. If the player hits a trap, the game ends.

Exit: The player must find and reach the exit point in the maze.

Timer: The game has a countdown timer, and the player must complete the maze before the time runs out.

Interactive UI: The game has a modern, user-friendly interface with visually appealing buttons and responsive design.

# Game Rules
Objective: Move the player through the maze using the arrow keys to find the exit before time runs out.

Controls: Use the arrow keys (Up, Down, Left, Right) to move the player through the maze.

Traps: If the player hits a trap (marked as "T"), the game ends immediately.

Exit: The goal is to reach the exit (marked as "E") before the timer runs out.

Timer: The player has 60 seconds to reach the exit. If the timer runs out, the game ends.

# Installation
To play the Maze Runner Game, ensure you have Python installed (preferably version 3.6 or later). You will also need the Tkinter library, which is used for the GUI.

# Steps:
Clone the repository or download the game script file (maze_runner_with_buttons.py).

Open a terminal or command prompt.

Navigate to the directory where the file is saved.

Run the game using the following command:

bash

Copy code

python maze_runner_with_buttons.py

# How to Play

Start the Game: Click the Start Game button.

Navigate: Use the arrow keys to move the player.

Avoid Traps: Watch out for the traps; they will end the game if you step on them.

Find the Exit: Locate and reach the exit before the timer runs out.

Win or Lose: If you reach the exit, you win! If you hit a trap or time runs out, you lose.

# Game UI Features
Start Button: A stylish green button that begins the game when clicked. The button features a modern design with hover and press effects.

Timer: A countdown timer is displayed at the top of the screen, showing the remaining time to reach the exit.

Instructions: Instructions are displayed below the timer, guiding the player on how to move using the arrow keys.

Maze Canvas: The maze is displayed on a canvas, with walls, paths, the player, the exit, and traps clearly marked with different colors.

Game Feedback: Upon winning or losing the game, a message will pop up to inform the player of their status.

# Code Structure

Main Window: The Tkinter window that contains all GUI elements, including the maze, buttons, timer, and instructions.

Maze Generation: The maze is generated dynamically using a Depth-First Search (DFS) algorithm, ensuring there’s always a solvable path from the start to the exit.

Player Movement: The player’s position is updated on the canvas as they move using the arrow keys.

Game Logic: Includes functions for moving the player, checking for traps or the exit, updating the timer, and displaying game over/win messages.

# Contributing

If you have suggestions or improvements, feel free to fork the repository and submit a pull request. All contributions are welcome!

# License

This project is open source and available under the MIT License.
