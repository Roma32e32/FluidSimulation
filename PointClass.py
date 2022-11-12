import taichi as ti
import taichi_glsl as ts
from taichi_glsl import vec2


class Point():
    def __init__(self, press) -> None:
        self.press = press
        self.speed = vec2


    def press_grad(self, press_array):
        pass


    def viscosity(self, press_array, speed_array):
        pass


    def inflow_calc(self, press_array, speed_array):
        pass


    def update_press(self):
        pass
