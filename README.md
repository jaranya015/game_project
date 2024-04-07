# Space Runner Game
Space Runner is an exhilarating space-themed runner game developed with the Kivy framework. Navigate your ship through a perilous space environment, dodging obstacles and making split-second decisions to survive as long as possible. The game's graphics are rendered using Kivy's canvas, ensuring smooth and engaging gameplay. Ready for the challenge? Dive into the Space Runner experience now!

# Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Gameplay](#gameplay)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
  
## Installation
Before you begin, ensure that you have Python and Kivy installed on your system. Follow these steps to get Space Runner up and running:

1. **Clone the repository:**
  ```bash
git clone https://github.com/jaranya015/game_project.git

3. Navigate to the game directory:
cd game_project

4. Install the required packages:
pip install kivy
pip install -r requirements.txt

# Features

Smooth and intuitive controls designed for desktop environments.
Dynamic obstacles and game environment generated in real-time.
Responsive ship controls allowing for quick dodging and maneuvering.
Score tracking to monitor your progress and set new records.

# Gameplay
Start the Game: Run main.py to launch the game.
Control the Ship: Use the A and D keys or touch controls to move the ship left and right.
Avoid Obstacles: Dodge the tiles and survive as long as you can. Collision with any tile will result in a game over.

# Code Structure
The game's codebase is divided into several key files, each serving a specific purpose:

main.py: The heart of the game, handling application logic, game rendering, and user input.
user_actions.py: Defines functions for processing keyboard and touch events.
transforms.py: Contains functions for transforming game graphics based on the perspective point, enhancing the visual experience.
menu.kv and compsuapp.kv: Kivy language files defining the game's user interface components.
Contributing
We welcome contributions to Space Runner! Whether you have suggestions for improvements, new features, or have found a bug, feel free to create an issue or submit a pull request on GitHub.

To add this to your GitHub repository:
1. Go to your repository on GitHub.
2. Click on "Add file" > "Create new file".
3. Name the file `README.md`.
4. Paste the Markdown content into the file.
5. Scroll down, add a commit message, and choose "Commit new file".

This will create a nicely formatted README on the front page of your GitHub repository
