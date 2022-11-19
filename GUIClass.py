import pygame as pg
from config import resolution


class GUI:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode(resolution)