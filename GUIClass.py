import pygame as pg
from config import resolution


class GUI():
    def __init__(self, vars) -> None:
        self.screen = pg.display.set_mode(resolution)

        self.press_field = vars.press_field
        self.speed_field = vars.speed_field


    def render(self):
        pass


    def draw(self):
        pass


    def update(self):
        self.render()
        self.draw()