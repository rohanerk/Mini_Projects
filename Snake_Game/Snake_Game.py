#!python3
#Snake_Game.py

import random

GRID_SIZE = 5
snake = [(2,2)] # The snake is a list of co-ordinates, head is the first element
direction = (0,1)
food = (random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1))

# Printing the grid

def print_grid():
    for y in range(GRID_SIZE):
        row = ""
        for x in range(GRID_SIZE):
            if (x,y) == food:
                row += "F"
            elif (x,y) in snake:
                row += "S"
            else:
                row += ". "

        print(row)

def move_snake(direction):
    global food
    head = snake[0]
    new_head = (head[0] + direction[0] , head[1] + direction[1])

    # Check boundaries
    if (new_head[0] < 0 or new_head[0] >= GRID_SIZE or
        new_head[1] < 0 or new_head[1] >= GRID_SIZE or
        new_head in snake):# snake hit itself
        print("Game Over!")
        return False

    snake.insert(0,new_head) # inserting the new_head at index 0

    if new_head == food:
        while food in snake:
            food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)) # if snake eats, generate a new position for food

    else:
        snake.pop()

    return True

while True:
    print_grid()
    move = input("Move (w/a/s/d): ")

    if move == "w":
        direction = (0, -1)
    elif move == "s":
        direction = (0, 1)
    elif move == "a":
        direction = (-1, 0)
    elif move == "d":
        direction = (1, 0)
    else:
        print("Invalid move")
        continue

    if not move_snake(direction):
        break
