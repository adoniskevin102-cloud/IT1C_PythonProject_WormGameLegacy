# PROGRAM LOGIC EXPLANATION

## Project Title: Classic Worm Game - Python Style

### 1. PROJECT OVERVIEW
This project is a digital recreation of the classic "Snake" or "Worm" game, developed using the Python programming language. The main objective of this project is to demonstrate the application of fundamental programming concepts such as variables, loops, conditional statements, functions, and data structures. The game utilizes the `turtle` module for its graphical interface, allowing for object creation, movement, and rendering.

The core goal of the game is simple: the player controls a worm that moves continuously across the screen. The player must guide the worm to consume food items that appear in random locations. Each time the worm eats food, it grows longer, the score increases, and the game becomes slightly faster and more challenging. The game ends when the worm collides with the boundary of the window or with its own body.

### 2. TECHNOLOGIES AND LIBRARIES USED
The program relies on built-in Python modules to handle different aspects of the game mechanics:

- **Python 3.x**: Serves as the primary programming language used to write the logic, structure, and functions of the game.
- **Turtle Module**: This is the main graphics library used. It is responsible for creating all visible objects such as the worm’s head and body, the food item, and the text display. It also handles moving these objects and updating the screen.
- **Time Module**: Used specifically to control the speed of the game. It creates a delay between movements, ensuring the game runs at a playable speed. As the score increases, this delay is reduced to increase difficulty.
- **Random Module**: This library generates random integer values. It is used to determine the new coordinates where the food item will appear every time it is consumed, ensuring it never appears in the same spot twice in a row.
- **Winsound Module**: Used to provide audio feedback. It generates beep sounds during specific events such as when the worm eats food or when a collision occurs, enhancing the user experience.

### 3. DETAILED PROGRAM LOGIC AND WORKFLOW

#### A. INITIALIZATION AND SETUP
When the program is executed, the first step is to import all required modules. After importing, the system initializes global variables that will be used throughout the game:
- `score`: Tracks the player's current points, starting at 0.
- `high_score`: Records the highest score achieved during the session.
- `delay`: Controls the speed of movement, starting at 0.1 seconds.
- `game_running`: A boolean value that keeps the main loop active.
- `game_state`: Determines whether the game is active ("play") or finished ("game_over").

Next, the game window is created with a fixed resolution of 600x600 pixels. The program attempts to load a custom background image file named `worm_bg.png`. If the file is missing or not found in the directory, the system handles the error gracefully and automatically changes the background color to `lightgreen` so the game can still run without interruption.

Following the screen setup, the program creates the game objects:
1.  **Snake Head**: Created as a circle shape, colored dark green, and placed at the center coordinate `(0, 0)`.
2.  **Food Object**: A smaller circle, colored red, placed initially at coordinate `(0, 100)`.
3.  **Score Pen**: A turtle object used solely to write text on the screen for scores and messages.
4.  **Body List**: An empty list defined to store new segments every time the worm eats food.

#### B. MOVEMENT LOGIC AND CONTROLS
Movement is, controlled by the player using the **W, A, S, D** keys or the **Arrow Keys**. The logic includes a restriction: the worm cannot reverse direction instantly. For example, if the worm is moving UP, pressing the DOWN key will have no effect. This prevents the worm from colliding with itself immediately after turning.

The movement system works in two distinct parts:
1.  **Moving the Body Segments**: The program reads the list of body segments starting from the last one. Each segment moves to the exact coordinate position of the segment in front of it. This creates a chain effect where the body perfectly follows the path of the head.
2.  **Moving the Head**: Once the body is repositioned, the head moves forward by 20 units based on its current direction.

#### C. FOOD CONSUMPTION, SCORING, AND GROWTH
Collision detection is done by calculating the distance between the coordinates of the snake’s head and the food object. If the distance is less than 20 pixels, the system registers a collision.

When food is consumed, the following sequence happens:
1.  **Audio Feedback**: A high-pitched beep sound plays.
2.  **Reposition Food**: New random X and Y coordinates are generated within the game boundary, and the food object teleports there.
3.  **Grow Worm**: A new segment object is created, styled slightly lighter in green color, and added to the end of the body list.
4.  **Update Score**: The score increases by 10 points. If the new score is higher than the current `high_score`, the high score is updated.
5.  **Increase Difficulty**: The `delay` variable is reduced slightly (`delay -= 0.001`), causing the loop to run faster and making the game harder as the player progresses.
6.  **Refresh Display**: The scoreboard is cleared and rewritten to show the updated values.

#### D. COLLISION DETECTION AND GAME OVER LOGIC
The game includes two main collision checks that trigger the "Game Over" state:

1.  **Wall Collision**: The playable area is set between coordinates -290 and +290 on both the X and Y axes. If the head’s coordinate goes beyond these limits, it is considered a crash.
2.  **Self-Collision**: The system loops through every segment stored in the body list. If the distance between the head and any body segment becomes less than 20 pixels, it is registered as a crash.

When a collision is detected:
- The `game_state` changes from `"play"` to `"game_over"`.
- A low-pitched warning sound plays.
- The screen displays the text **"GAME OVER GG!!"** in large red font, along with instructions:
    - Press **[ R ]** to Try Again: This resets the head position, clears the body list, resets the score and speed, and restarts the game loop.
    - Press **[ E ]** to Exit: This displays a thank-you message, waits for 2 seconds, and safely closes the program window.

#### E. MAIN GAME LOOP
All the logic mentioned above runs inside a `WHILE` loop. This loop continuously executes as long as `game_running` is set to `TRUE`. Inside the loop, the program updates the screen, checks for collisions, executes movement, and pauses briefly based on the `delay` variable. This structure ensures the game runs smoothly and reacts instantly to user input and changes in game state.

### 4. SUMMARY AND CONCLUSION
This program serves as a complete demonstration of programming logic and structure. It effectively uses conditional statements to check game rules, loops to manage continuous actions, and lists to manage a growing number of objects. The error handling for missing background files and the inclusion of user-friendly controls such as restart and exit options show attention to detail and proper software development practices.

The resulting application is fully functional, visually clear, and follows the mechanics of the classic Worm game accurately.
