# Imports libraries and moodules
import pygame
from pygame.locals import *
import constants
import time
import random


class Guanabana():
    def __init__(self, parent_window):
        self.image = pygame.image.load("images\guanabana.png")
        self.parent_window = parent_window
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_window.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    # Move method
    def move(self):
        self.x = random.randint(32, 768)
        self.y = random.randint(32, 568)


class Snake():
    def __init__(self, parent_window, length):
        self.parent_window = parent_window
        self.snake_body = pygame.image.load("images\circulo.png")
        self.direction = "down"

        self.length = length
        self.x = [32]*length
        self.y = [32]*length

    def increse_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


    def draw(self):
        self.parent_window.fill(constants.BG_COLOR)

        for i in range(self.length):

           self.parent_window.blit(self.snake_body, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):
        # Update body
        for i in range (self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # Update head
        if self.direction == "left":
            self.x[0] -= constants.SIZE_SNAKE

        if self.direction == "right":
            self.x[0] += constants.SIZE_SNAKE

        if self.direction == "up":
            self.y[0] -= constants.SIZE_SNAKE

        if self.direction == "down":
            self.y[0] += constants.SIZE_SNAKE

        self.draw()


class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(constants.SIZE)
        self.title = pygame.display.set_caption(constants.TITLE)
        self.window.fill(constants.BG_COLOR)
        icon = pygame.image.load("images\serpiente.png")
        pygame.display.set_icon(icon)

        self.snake = Snake(self.window, 2)
        self.snake.draw()

        self.guanabana = Guanabana(self.window)
        self.guanabana.draw()
        
        pygame.display.update()

    # Collition logic
    def is_collition(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + constants.APPLE_SIZE:
            if y1 >= y2 and y1 < y2 + constants.APPLE_SIZE:
                return True
        return False

    # Play mathod
    def play(self):
        self.snake.walk()
        self.guanabana.draw() 

        if self.is_collition(self.snake.x[0], self.snake.y[0], self.guanabana.x, self.guanabana.y):
            #print("JH")
            self.snake.increse_length()
            self.guanabana.move()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()



                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.2)

game = Game()
game.run()




