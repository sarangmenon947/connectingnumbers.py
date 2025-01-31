import pgzrun
import random
from time import time
import pygame

# Constants for screen dimensions
WIDTH = 800
HEIGHT = 600

# Global variables
numbers = []
number_of_numbers = 8
next_number_index = 0
lines = []
start_time = 0
total_time = 0

def create_numbers():
    global start_time, numbers
    # Creating a list of numbers and shuffling them
    numbers_list = list(range(1, number_of_numbers + 1))
    random.shuffle(numbers_list)

    for number in numbers_list:
        actor_number = Actor(f"number_{number}") 
        # Resize the image to 50x50 pixels
        original_surface = actor_number._surf
        resized_surface = pygame.transform.scale(original_surface, (50, 50))
        actor_number._surf = resized_surface
        
        # Set random position for the resized actor
        actor_number.pos = random.randint(40, WIDTH - 90), random.randint(40, HEIGHT - 90)  # Adjusted for new size
        numbers.append(actor_number)

    start_time = time()

def draw():
    global total_time
    screen.blit("space", (0, 0))  # Background image

    # Drawing numbers and their positions
    for i, number_actor in enumerate(numbers):
        number_actor.draw()
        screen.draw.text(str(i + 1), (number_actor.pos[0], number_actor.pos[1] + 20), fontsize=30)

    # Drawing lines connecting numbers
    for line in lines:
        screen.draw.line(line[0], line[1], "white")

    # Displaying total time elapsed
    total_time = time() - start_time
    screen.draw.text(str(round(total_time, 1)), (20, 20), fontsize=40)

def update():
    pass

def on_mouse_down(pos):
    global next_number_index, lines
    if next_number_index < number_of_numbers:
        if numbers[next_number_index].collidepoint(pos):
            if next_number_index > 0:
                lines.append((numbers[next_number_index - 1].pos, numbers[next_number_index].pos))
            next_number_index += 1
        else: 
            lines = []
            next_number_index = 0

create_numbers()
pgzrun.go()
