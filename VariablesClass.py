import taichi as ti
from dataclasses import dataclass
from config import resolution


@dataclass
class Variables():
    ti.init(arch=ti.cuda)
    press_field = ti.field(dtype=ti.float64, shape=resolution)
    speed_field = ti.Vector.field(n=2, dtype=ti.float64, shape=resolution)