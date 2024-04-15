# AimTrainer

**Enhanced Aim Trainer** is a Python-based interactive game designed to help users improve their mouse aiming and clicking accuracy. Developed using the Pygame library, it provides a visually appealing interface with dynamically generated targets that expand and contract, requiring precision and quick reactions from players. 

### Features

- **Dynamic Target Generation**: Targets spawn at random locations on the screen at regular intervals, increasing the challenge.
- **Colorful Interface**: Utilizes a dual-color scheme for targets that enhances visual clarity and user engagement.
- **Performance Metrics**: Tracks and displays elapsed time, score (number of hits), misses, and clicking accuracy.
- **End Game Summary**: Provides a final overview of the player's performance once the game ends (upon losing all health points).

![WhatsApp Image 2024-04-15 at 12 27 58_6839d7b4](https://github.com/Amsmoox/AimTrainer/assets/82274806/bb57404f-9dc1-44de-93ad-da9018d60b29)

### Requirements

Before you can run the Enhanced Aim Trainer, make sure you have the following installed:

- **Python**: Version 3.6 or later. You can download it from [python.org](https://www.python.org/).
- **Pygame**: Version 2.0.1 or later. Pygame is a set of Python modules designed for writing video games. You can install it using pip:

  ```bash
  pip install pygame
  ```

### How to Run the Game

Follow these steps to get the game up and running on your system:

1. **Clone the repository** or download the ZIP file and extract it:

   ```bash
   git clone https://github.com/Amsmoox/AimTrainer.git
   cd AimTrainer
   ```

2. **Run the game**:
   
   Open a terminal in the project directory and execute the following command:

   ```bash
   python AimTrainer.py
   ```

   This command will start the game window and you can begin playing immediately.

### Project Structure

- **AimTrainer.py**: The main game script containing all the logic and UI definitions necessary to run the game.
  - `MovingTarget` class: Defines the target's behavior including growth and movement logic.
  - `render_scene` function: Responsible for drawing the current state of the game screen, including all targets.
  - `display_info` function: Displays current game statistics such as score, time elapsed, and misses.
  - `final_screen` function: Shows the end game summary with final stats.
  - `gameplay` function: Contains the main game loop which handles events, updates game state, and refreshes the display.
  
### Support or Contact

Having trouble with the game?
Contact me at : 

[<img align="left" alt="MharrechAyoub | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]


[linkedin]: https://www.linkedin.com/in/ayoubmharrech/

