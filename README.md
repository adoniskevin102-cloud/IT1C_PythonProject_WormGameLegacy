# 🐍 Classic Worm Game - Python

![Worm Logo](./images/WORM%20LOGO.png)

> A nostalgic take on the classic Snake game, built from scratch using Python

**Course:** IT1C | **Project Type:** Final Project | **Status:** ✅ Complete

---

## 📌 What is This Project?

This is a **fully-functional Classic Snake Game** (also called Worm Game) - a fun, retro arcade-style game built entirely in Python! 

![Game Background](./images/WORM%20BG%20I%20USE%20TO%20CANVA.png)

You control a worm/snake that:
- 🍎 **Eats food** to grow longer
- 📈 **Scores points** for each food eaten
- 🏃 **Gets faster** as you progress
- ⚠️ **Avoids walls and itself** to stay alive

It's the perfect blend of nostalgia and modern programming, making it both entertaining AND educational!

---

## 🚀 Installation & Quick Start

### Prerequisites
- **Python 3.x** installed on your computer
  - Check if installed: `python --version` in terminal
  - [Download Python](https://www.python.org/downloads/) if needed

### Step-by-Step Installation

1. **Clone or Download the Repository**
   ```bash
   # Using Git:
   git clone https://github.com/your-username/IT1C_PythonProject_WormGameLegacy.git
   cd IT1C_PythonProject_WormGameLegacy
   
   # Or: Just download the ZIP file and extract it
   ```

2. **Install Dependencies** (For Sound on Mac & Linux)
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** Windows users don't need to install anything! Sound works out of the box.

3. **Run the Game**
   ```bash
   python source/main.py
   ```

4. **That's it!** The game window will open - enjoy! 🎮

### Platform-Specific Details

#### 🪟 Windows
- Just run the game - full sound support works automatically!
- No additional installation required

#### 🍎 macOS
- Install pygame for sound support:
  ```bash
  pip install pygame
  ```
- If pygame won't install:
  ```bash
  pip install pygame --pre
  ```
- Then run: `python source/main.py`

#### 🐧 Linux
- Install pygame for sound support:
  ```bash
  pip install pygame
  ```
- May require additional audio libraries depending on your distro
- Game will still run without pygame, but without sound effects

### Sound Support

| Platform | Sound Support | Setup Required |
|----------|---|---|
| **Windows** | ✅ Yes | No - Works out of the box |
| **macOS** | ✅ Yes | `pip install pygame` |
| **Linux** | ✅ Yes | `pip install pygame` |

**Note:** If pygame can't be installed or audio fails, the game will still work perfectly - sounds will just be skipped silently.

---

## 🎮 How to Play

### Game Objective
Your goal is simple but challenging:
- 🍎 **Eat as much red food as possible** to grow your worm
- 📊 **Maximize your score** and try to beat your personal best
- 🎯 **Survive as long as you can** without hitting walls or yourself

### Game Controls

| Key | Action |
|-----|--------|
| `W` or `↑` | Move Up |
| `S` or `↓` | Move Down |
| `A` or `←` | Move Left |
| `D` or `→` | Move Right |
| `R` | Restart the game (after Game Over) |
| `E` | Exit and close the game |

### Game Over Conditions
- ❌ **Hit the boundary/wall** - You've crashed into the edge of the game area
- ❌ **Hit your own body** - Your head collided with your tail
- 🔔 You'll hear a warning beep and see the Game Over screen

### Scoring System
- Each food eaten = **+10 points**
- Your **high score is tracked** and persists throughout the session
- Game difficulty increases as your score increases (worm moves faster)

---

## ✨ Game Features

| Feature | Description |
|---------|-------------|
| ✅ **Easy to Learn** | Simple controls that anyone can understand |
| ✅ **Smooth Controls** | Responsive keyboard input for precise movement |
| ✅ **Dual Control Options** | Use WASD keys OR arrow keys - choose what feels best |
| ✅ **Score Tracking** | Keep track of current score and highest score |
| ✅ **Progressive Difficulty** | Game automatically gets faster as you eat more |
| ✅ **Sound Effects** | Audio feedback for eating food and game over events |
| ✅ **Visual Polish** | Colorful graphics with background image support |
| ✅ **Instant Restart** | Jump back in with the R key - no need to restart |
| ✅ **Graceful Exit** | Clean shutdown with the E key |

---

## 🛠️ Technologies & Libraries

| Technology | Purpose | Why We Used It |
|-----------|---------|----------------|
| **Python 3.x** | Core language | Simple, readable, perfect for learning |
| **Turtle Module** | Graphics & animation | Built-in, great for 2D graphics without external dependencies |
| **Time Module** | Game speed control | Manages frame timing and game delays |
| **Random Module** | Random generation | Spawns food at random locations |
| **Pygame** | Cross-platform sound | Audio feedback that works on Windows, Mac, and Linux |

---

## 📂 Project Structure

```
IT1C_PythonProject_WormGameLegacy/
│
├── 📄 README.md                          ← You are here! (Project documentation)
│
├── 📄 INSTALL.md                         (Detailed installation instructions)
│
├── 📄 requirements.txt                   (Python dependencies)
│
├── 📁 source/
│   └── 🐍 main.py                        (Main game - THIS IS WHAT YOU RUN)
│
├── 📁 documentation/
│   ├── 📊 flowchart.png                 (Visual program flow diagram)
│   ├── 📋 program logic explanation.docx (Detailed technical explanation)
│   └── 📝 pseudocode.md                 (Algorithm written in plain English)
│
└── 📁 images/
    ├── 🖼️  WORM BG I USE TO CANVA.png   (Game background image)
    └── 🎨 WORM LOGO.png                 (Project logo/icon)
```

---

## 🎓 Game Mechanics (Technical Details)

### How Movement Works
1. The worm is made up of segments (head + body parts)
2. When you press a key, the head moves in that direction
3. Body segments follow the head like a train (each follows the one in front)
4. The game updates every 0.1 seconds (or faster as difficulty increases)

### How Collision Detection Works
1. **Wall Collision:** Game checks if head position is beyond the 290-pixel boundary
2. **Self-Collision:** Game checks if head is touching any body segment

### How Growth Works
1. You eat food when head gets close enough to it
2. A new body segment is created and added to the worm
3. The segment follows the segment in front of it
4. Game speed increases slightly to make it more challenging

### Game State System
- **Play State:** Normal gameplay
- **Game Over State:** Waiting for restart (R) or exit (E) commands

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'turtle'"
This shouldn't happen - Turtle is built into Python. Try:
- Reinstalling Python (making sure to check "Add Python to PATH")
- Using a different Python IDE like PyCharm or VS Code

### Game Won't Start / Black Screen
- Make sure the game window is in focus
- Try pressing a key to wake it up
- Restart the program

### Sound Not Working
- **Windows:** Should work automatically. Try reinstalling the game.
- **Mac/Linux:** Make sure pygame is installed: `pip install pygame`
- Even if sound fails, the game will still run normally - this won't affect gameplay!

### Game is Too Fast / Too Slow
- This is by design - difficulty increases as you score points
- There's no difficulty setting, but you can edit the code if desired
- Check the `delay` variable in the Python file to adjust speed

### Background Image Not Loading
- The game will automatically use a green background if the image file is missing
- This is intentional and won't break the game
- To use a custom background, place `worm_bg.png` in the same folder

### Game Crashes on Close
- This is rare but can happen with Turtle graphics
- Just close the window normally - it should force quit

---

## 💡 Programming Concepts Demonstrated

This project is a great learning resource for Python beginners! It demonstrates:

- **Variables & Data Types** - Storing game state, coordinates, scores
- **Functions** - Movement controls, collision detection, state management
- **Loops** - Main game loop that runs continuously
- **Conditional Statements** - If/else for game logic and collision checking
- **Lists/Data Structures** - Storing snake body segments
- **Event Handling** - Keyboard input processing
- **File Handling** - Loading background image
- **Libraries & Modules** - Using Python's built-in and system libraries

---

## 👨‍💻 Development Team

This project was created by the **IT1C section** as a collaborative final project:

- **John Kevin D. Adonis**
- **Alfred Banda**
- **[Charles E. Almario](https://github.com/jupiter4546/IT1C_Portfolio_Almario)**
- **Ely Jay G. Almazan**
- **Jun Staywart Conde**
- **John Roi Ken German**
- **Cianrei Bares**

---

## 📝 Notes & Tips

### For New Players
- Start slow and get used to the controls
- Remember you can turn in any direction EXCEPT backwards
- The game gets harder the better you do!

### For Programmers/Students
- The code is well-commented and easy to understand
- Each section is clearly labeled (VARIABLE AREA, SCREEN AREA, etc.)
- Try modifying the colors, speed, or graphics!

### For Developers
- Feel free to fork and modify this project
- Add new features like obstacles, power-ups, or difficulty levels
- Share your improvements!

---

## 📚 Additional Resources

- Check the `documentation/` folder for flowcharts and pseudocode
- Python Turtle Documentation: [docs.python.org/turtle](https://docs.python.org/3/library/turtle.html)
- Learn more about game loops: [Google "Game Loop Programming"](https://www.google.com)

---

## ⭐ Have Fun!

Thanks for playing! This was made with care by the IT1C team. Enjoy the nostalgia and challenge yourself to beat your high score! 

**May the worm be with you!** 🐍✨

---

*Last Updated: June 2026 | Made with ❤️ in Python* 
