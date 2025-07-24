import random # for generating random food positions
import time   # to control the speed of the game
import os   # to clear the terminal screen
import keyboard # to detect real time key presses

last_move_time = time.time()
move_delay = 0.3

# initialize game state

GRID_SIZE = 10
snake = [(5,5)]
direction = (0,1)
food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))

# Clears terminal window
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Draw the game board

def print_grid():
    for y in range(GRID_SIZE):
        row = ""
        for x in range(GRID_SIZE):
            if (x,y) == food:
                row += 'F'
            elif (x,y) == snake[0]:
                row += 'H'
            elif (x,y) in snake:
                row += 'S'
            else:
                row += '. '
        print(row)
    print(f"Score: {len(snake) - 1}")

# Snake movement

def move_snake():
    global food

    head = snake[0]
    new_head = (head[0] + direction[0],head[1]+direction[1])

    if (new_head[0]<0 or new_head[0]>=GRID_SIZE or
       new_head[1] < 0 or new_head[1]>= GRID_SIZE or
       new_head in snake):
           print('Game Over!')
           print(f"Final Score: {len(snake)-1}")
           return False

    snake.insert(0,new_head)

    if new_head == food:
        while food in snake:
            food = (random.randint(0,GRID_SIZE-1) , random.randint(0,GRID_SIZE-1))

    else:
        snake.pop()

    return True


# Read key presses

def update_direction():
    global direction

    if keyboard.is_pressed('w') and direction != (0,1):
        direction = (0,-1)
        print("W key detected")
    elif keyboard.is_pressed('a') and direction != (1,0):
        direction = (-1,0)
        print("A key detected")
    elif keyboard.is_pressed('s') and direction != (0,-1):
        direction = (0,1)
        print("S key detected")
    elif keyboard.is_pressed('d') and direction != (-1,0):
        direction = (1,0)
        print("D key detected")


# Game intro

clear_screen()
print("Use W/A/S/D to control the snake. Game starts in 3 seconds...")
time.sleep(3) # pauses the program for 3 seconds before continuing
# Game loop

while True:
    update_direction()
    if time.time() - last_move_time > move_delay:
        if not move_snake():
            break

        clear_screen()
        print_grid()
        last_move_time = time.time()
    time.sleep(0.01)
