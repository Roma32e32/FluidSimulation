import pygame as pg
import numpy as np
from config import screen_resolution


class GUI:
    def __init__(self, global_data) -> None:
        self.screen = pg.display.set_mode(screen_resolution)