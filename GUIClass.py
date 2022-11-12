import pygame as pg
from config import resolution


class GUI():
    def __init__(self) -> None:
        self.screen = pg.display.set_mode(resolution)


    def render(self):
        pass


    def draw(self):
        pass


    def update(self):
        self.render()
        self.draw()