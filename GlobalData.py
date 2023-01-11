import numpy as np
from config import main_resolution


class GlobalData:
    def __init__(self) -> None:
        self.press_array = np.full(main_resolution)