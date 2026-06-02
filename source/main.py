# WORM Game - FINAL
import turtle
import time
import random
import math

# ─────────────────────────────────────────────
#  CROSS-PLATFORM SOUND SUPPORT
# ─────────────────────────────────────────────
HAS_PYGAME = False
HAS_WINSOUND = False

try:
    import pygame
    pygame.mixer.init()
    HAS_PYGAME = True
except ImportError:
    pass

if not HAS_PYGAME:
    try:
        import winsound
        HAS_WINSOUND = True
    except ImportError:
        pass


def generate_sine_wave(frequency, duration_ms, sample_rate=22050):
    """Generate a stereo sine-wave buffer."""
    import array
    num_samples = int(sample_rate * duration_ms / 1000)
    frames = array.array('h')
    for i in range(num_samples):
        sample = int(32767 * 0.3 * math.sin(2 * math.pi * frequency * i / sample_rate))
        frames.append(sample)
        frames.append(sample)          # stereo duplicate
    return frames


def play_sound(frequency, duration):
    """Cross-platform beep. Fails silently when no audio back-end is available."""
    if HAS_PYGAME:
        try:
            sound_array = generate_sine_wave(frequency, duration)
            sound = pygame.sndarray.make_sound(sound_array)
            sound.play()
        except Exception:
            pass
    elif HAS_WINSOUND:
        try:
            winsound.Beep(frequency, duration)
        except Exception:
            pass


# ─────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────
SCREEN_SIZE   = 600
BORDER_MARGIN = 20          # pixels from the edge where the visible border sits
PLAY_LIMIT    = 270         # head xcor/ycor must stay inside ±PLAY_LIMIT
CELL_SIZE     = 20          # movement step size

BORDER_COLOR  = "#8B0000"   # dark-red border line
BORDER_WIDTH  = 4           # pen thickness in pixels

FONT_SCORE    = ("Arial", 18, "bold")
FONT_BIG      = ("Arial", 40, "bold")
FONT_SMALL    = ("Arial", 16, "bold")


# ─────────────────────────────────────────────
#  STATE
# ─────────────────────────────────────────────
delay       = 0.1
score       = 0
high_score  = 0
game_running = True
game_state  = "play"


# ─────────────────────────────────────────────
#  SCREEN
# ─────────────────────────────────────────────
wn = turtle.Screen()
wn.title("Classic Worm - Python Style")
wn.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
wn.tracer(0)

try:
    wn.bgpic("worm_bg.png")
except Exception:
    wn.bgcolor("lightgreen")
    print("GAME IS NOW RUNNING")


def close_game():
    global game_running
    game_running = False
    wn.bye()


wn._root.protocol("WM_DELETE_WINDOW", close_game)


# ─────────────────────────────────────────────
#  BORDER  ← NEW
#  Draws a solid rectangle that marks the play
#  area boundary so the player always knows
#  where the wall is.
# ─────────────────────────────────────────────
def draw_border():
    """Draw a fixed rectangular border around the play field."""
    b = BORDER_MARGIN - SCREEN_SIZE // 2   # e.g. 20 - 300 = -280
    t = SCREEN_SIZE // 2 - BORDER_MARGIN   # e.g. 300 - 20 =  280

    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.penup()
    border_pen.hideturtle()
    border_pen.color(BORDER_COLOR)
    border_pen.pensize(BORDER_WIDTH)

    # Outer filled rectangle (gives the wall a thick, solid look)
    border_pen.fillcolor(BORDER_COLOR)
    border_pen.goto(b, b)
    border_pen.pendown()
    border_pen.begin_fill()
    for _ in range(4):
        border_pen.forward(t - b)
        border_pen.left(90)
    border_pen.end_fill()

    # Inner cutout (the actual play area background shows through here)
    inner_offset = BORDER_WIDTH * 2          # wall visual thickness
    bi = b + inner_offset
    ti = t - inner_offset

    border_pen.penup()
    border_pen.goto(bi, bi)
    border_pen.pendown()

    # Erase the interior by drawing a filled rectangle in the background colour
    bg = wn.bgcolor()
    border_pen.fillcolor(bg if bg else "lightgreen")
    border_pen.begin_fill()
    for _ in range(4):
        border_pen.forward(ti - bi)
        border_pen.left(90)
    border_pen.end_fill()
    border_pen.penup()

    # Corner label so the player knows it is a wall
    label_pen = turtle.Turtle()
    label_pen.speed(0)
    label_pen.penup()
    label_pen.hideturtle()
    label_pen.color(BORDER_COLOR)
    label_pen.goto(0, t + 4)
    label_pen.write("─── WALL ───", align="center", font=("Arial", 9, "bold"))
    label_pen.goto(0, b - 14)
    label_pen.write("─── WALL ───", align="center", font=("Arial", 9, "bold"))


draw_border()


# ─────────────────────────────────────────────
#  SNAKE HEAD
# ─────────────────────────────────────────────
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("circle")
snake_head.color("darkgreen")
snake_head.shapesize(stretch_wid=1.3, stretch_len=1.3)
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

snake_body = []


# ─────────────────────────────────────────────
#  FOOD
# ─────────────────────────────────────────────
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.shapesize(stretch_wid=1.0, stretch_len=1.0)
food.penup()
food.goto(0, 100)


# ─────────────────────────────────────────────
#  HUD TURTLES
# ─────────────────────────────────────────────
pen_score = turtle.Turtle()
pen_score.speed(0)
pen_score.color("black")
pen_score.penup()
pen_score.hideturtle()
pen_score.goto(0, 260)

pen_message = turtle.Turtle()
pen_message.speed(0)
pen_message.color("red")
pen_message.penup()
pen_message.hideturtle()


# ─────────────────────────────────────────────
#  MOVEMENT CALLBACKS
# ─────────────────────────────────────────────
def go_up():
    if snake_head.direction != "down" and game_state == "play":
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != "up" and game_state == "play":
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != "right" and game_state == "play":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left" and game_state == "play":
        snake_head.direction = "right"


# ─────────────────────────────────────────────
#  GAME-STATE CALLBACKS
# ─────────────────────────────────────────────
def try_again():
    global score, delay, game_state
    if game_state != "game_over":
        return

    pen_message.clear()
    pen_score.clear()

    snake_head.goto(0, 0)
    snake_head.direction = "stop"

    for segment in snake_body:
        segment.goto(1000, 1000)
    snake_body.clear()

    score = 0
    delay = 0.1

    pen_score.write(
        f"Score: {score}  |  Highest: {high_score}",
        align="center", font=FONT_SCORE
    )
    game_state = "play"


def exit_game():
    global game_running
    pen_message.clear()
    pen_message.goto(0, 0)
    pen_message.color("darkgreen")
    pen_message.write("THANK YOU FOR PLAYING!!", align="center", font=("Arial", 22, "bold"))
    wn.update()
    time.sleep(2)
    game_running = False
    wn.bye()


# ─────────────────────────────────────────────
#  MOVE
# ─────────────────────────────────────────────
def move():
    if not game_running or game_state != "play":
        return

    # Shift body segments forward
    for index in range(len(snake_body) - 1, 0, -1):
        x = snake_body[index - 1].xcor()
        y = snake_body[index - 1].ycor()
        snake_body[index].goto(x, y)

    if snake_body:
        snake_body[0].goto(snake_head.xcor(), snake_head.ycor())

    # Advance head
    direction = snake_head.direction
    if direction == "up":
        snake_head.sety(snake_head.ycor() + CELL_SIZE)
    elif direction == "down":
        snake_head.sety(snake_head.ycor() - CELL_SIZE)
    elif direction == "left":
        snake_head.setx(snake_head.xcor() - CELL_SIZE)
    elif direction == "right":
        snake_head.setx(snake_head.xcor() + CELL_SIZE)


# ─────────────────────────────────────────────
#  GAME-OVER DISPLAY
# ─────────────────────────────────────────────
def show_game_over():
    """Render the game-over overlay."""
    global game_state
    game_state = "game_over"
    pen_message.goto(0, 50)
    pen_message.color("red")
    pen_message.write("GAME OVER GG!!", align="center", font=FONT_BIG)
    pen_message.goto(0, -20)
    pen_message.color("black")
    pen_message.write("Click [ R ]  TRY AGAIN", align="center", font=FONT_SMALL)
    pen_message.goto(0, -50)
    pen_message.write("Click [ E ]  EXIT", align="center", font=FONT_SMALL)


# ─────────────────────────────────────────────
#  KEY BINDINGS
# ─────────────────────────────────────────────
wn.listen()
wn.onkeypress(go_up,    "w")
wn.onkeypress(go_down,  "s")
wn.onkeypress(go_left,  "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up,    "Up")
wn.onkeypress(go_down,  "Down")
wn.onkeypress(go_left,  "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(try_again,  "r")
wn.onkeypress(exit_game,  "e")


# ─────────────────────────────────────────────
#  SPAWN FOOD HELPER  (keeps food inside walls)
# ─────────────────────────────────────────────
def spawn_food():
    """Place food at a random cell inside the play area."""
    safe = PLAY_LIMIT - CELL_SIZE            # stay a full step away from the wall
    steps_x = random.randint(-safe // CELL_SIZE, safe // CELL_SIZE)
    steps_y = random.randint(-safe // CELL_SIZE, safe // CELL_SIZE)
    food.goto(steps_x * CELL_SIZE, steps_y * CELL_SIZE)


spawn_food()   # initial placement


# ─────────────────────────────────────────────
#  MAIN GAME LOOP
# ─────────────────────────────────────────────
try:
    pen_score.write("Score: 0  |  Highest: 0", align="center", font=FONT_SCORE)

    while game_running:
        wn.update()

        if game_state == "play":

            # ── Wall collision ──────────────────────────────
            if abs(snake_head.xcor()) > PLAY_LIMIT or abs(snake_head.ycor()) > PLAY_LIMIT:
                play_sound(250, 300)
                show_game_over()

            # ── Food collision ──────────────────────────────
            elif snake_head.distance(food) < CELL_SIZE:
                play_sound(700, 120)
                spawn_food()

                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("circle")
                new_segment.color("limegreen")
                new_segment.shapesize(stretch_wid=1.1, stretch_len=1.1)
                new_segment.penup()
                snake_body.append(new_segment)

                delay = max(delay - 0.001, 0.05)   # cap minimum speed
                score += 10
                if score > high_score:
                    high_score = score

                pen_score.clear()
                pen_score.write(
                    f"Score: {score}  |  Highest: {high_score}",
                    align="center", font=FONT_SCORE
                )

            # ── Self collision ──────────────────────────────
            else:
                for segment in snake_body:
                    if segment.distance(snake_head) < CELL_SIZE:
                        play_sound(200, 400)
                        show_game_over()
                        break

        move()
        time.sleep(delay)

except turtle.Terminator:
    pass                       # user closed the window normally
except Exception as e:
    if game_running:
        print("Unexpected error:", e)