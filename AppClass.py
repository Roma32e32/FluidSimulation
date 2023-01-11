import pygame as pg
from GlobalData import GlobalData
from GUIClass import GUI
from SimulationClass import Simulation
from config import FPS

class App:
    def __init__(self) -> None:
        self.global_data = GlobalData()
        self.clock = pg.time.Clock()

        self.GUI = GUI(self.global_data)
        self.SIM = Simulation(self.global_data)

    def quiting(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()


    def run(self):
        while True:
            self.quiting()
            pg.display.set_caption(f"FPS: {self.clock.get_fps()}")
            self.clock.tick(FPS)
