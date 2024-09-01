# 🎮 Simple Pygame Adventure

This is a simple 2D game developed using Python and Pygame. In this game, the player controls a character that must avoid enemies and collect bonuses to score points. The game continues until the player's health reaches zero.

## 🕹️ Game Features

- **Player Movement**: The player can move in all directions within the game window.
- **Enemies**: The player must avoid enemies that move horizontally across the screen.
- **Bonuses**: Collect bonuses to increase your score.
- **Health**: The player starts with 100 health points. Colliding with enemies reduces health by 50 points. The game ends when health drops to 0.
- **Score**: The score increases by 1 point for each bonus collected.
- **Game Over Screen**: Displays the final score and allows the player to restart the game by pressing Enter.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Pygame library (`pygame`)

### Installing Pygame

To install Pygame, use pip:

```bash
pip install pygame
```

### 🛠️ Running the Game

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Antot-12/Python_game.git
    cd Python_game
    ```

2. **Run the game**:

    ```bash
    python game.py
    ```

### 🎮 How to Play

- **Movement**: 
  - Use the arrow keys to move the player character.
  - **Left Arrow**: Move left.
  - **Right Arrow**: Move right.
  - **Up Arrow**: Move up.
  - **Down Arrow**: Move down.
  
- **Objectives**:
  - Avoid enemies that move across the screen.
  - Collect bonuses to increase your score.
  - Survive as long as possible to achieve a high score.

- **Game Over**:
  - The game ends when the player's health reaches zero.
  - On the Game Over screen, press `Enter` to restart the game.

### 🖼️ Assets

- The game uses images for the player, enemies, bonuses, and background. Ensure that these image files (`1-1.png`, `bonus.png`, `enemy.png`, `background.png`, etc.) are placed in the same directory as the game script.

### 🛠️ Customization

- **Animation Interval**: Change the `ANIMATION_INTERVAL` variable to adjust the speed at which the player's animation frames change.
- **Game Speed**: Modify the values in `FPS.tick(120)` to control the game speed (lower for slower, higher for faster).

### 🐞 Troubleshooting

- **Missing Images**: Ensure all required images are in the same directory as the game script.
- **Pygame Errors**: Make sure Pygame is installed correctly (`pip install pygame`).

---

Enjoy playing the game! 🚀
