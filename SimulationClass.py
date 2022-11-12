import taichi as ti
import taichi_glsl as ts
from config import resolution


class Simulation():
    def __init__(self, vars) -> None:
        self.press_field = vars.press_field
        self.speed_field = vars.speed_field


    def simulation(self):
        pass