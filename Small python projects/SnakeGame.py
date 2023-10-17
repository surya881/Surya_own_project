import tkinter as tk
import random
WIDTH=400
HEIGHT=400
DELAY=100
SNAKE_SIZE=20
MOVE_INCREMENT=20
GAME_SPEED = 100
BG_COLOR="black"
SNAKE_COLOR="green"
FOOD_COLOR="red"
snake_direction = "Right"
score = 0
def start_game():
    global snake_direction, score
    score = 0
    snake_direction = "Right"
    snake_segments = [(100, 100), (80, 100), (60, 100)]
    food_position = generate_food()
    game_canvas.delete("all")
    game_loop(snake_segments, food_position)
def game_loop(snake_segments, food_position):
    global snake_direction, score
    if not is_collision(snake_segments):
        move_snake(snake_segments, snake_direction)
        if snake_segments[0] == food_position:
            score += 1
            snake_segments.append((0, 0))  
            food_position = generate_food()
        game_canvas.delete("all")
        game_canvas.create_rectangle(0, 0, WIDTH, HEIGHT, outline="white", width=2)
        for segment in snake_segments:
            x, y = segment
            game_canvas.create_rectangle(
                x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=SNAKE_COLOR
            )
        x, y = food_position
        game_canvas.create_oval(
            x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=FOOD_COLOR
        )
        score_label.config(text=f"Score: {score}")
        game_canvas.after(DELAY, game_loop, snake_segments, food_position)
    else:
        game_over()
def move_snake(snake_segments, direction):
    x, y = snake_segments[0]
    if direction == "Up":
        y -= MOVE_INCREMENT
    elif direction == "Down":
        y += MOVE_INCREMENT
    elif direction == "Left":
        x -= MOVE_INCREMENT
    elif direction == "Right":
        x += MOVE_INCREMENT
    snake_segments.pop()
    snake_segments.insert(0, (x, y))
def is_collision(snake_segments):
    x, y = snake_segments[0]
    if (
        x < 0
        or x >= WIDTH
        or y < 0
        or y >= HEIGHT
        or snake_segments[0] in snake_segments[1:]
    ):
        return True
    return False
def generate_food():
    x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    return x, y
def on_key_press(event):
    global snake_direction
    if event.keysym == "Up" and snake_direction != "Down":
        snake_direction = "Up"
    elif event.keysym == "Down" and snake_direction != "Up":
        snake_direction = "Down"
    elif event.keysym == "Left" and snake_direction != "Right":
        snake_direction = "Left"
    elif event.keysym == "Right" and snake_direction != "Left":
        snake_direction = "Right"
def game_over():
    game_canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2,
        text="Game Over!",
        fill="white",
        font=("Courier", 24, "bold")
    )
    game_canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2 + 50,
        text=f"Score: {score}",
        fill="white",
        font=("Courier", 18, "normal")
    )
    start_button.config(state=tk.NORMAL)
window = tk.Tk()
window.title("Snake Game")
game_canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
game_canvas.pack()
score_label = tk.Label(window, text="Score: 0", font=("Courier", 14))
score_label.pack()
start_button = tk.Button(window, text="Start", font=("Courier", 14), command=start_game)
start_button.pack()
game_canvas.bind("<KeyPress>", on_key_press)
game_canvas.focus_set()
window.mainloop()
