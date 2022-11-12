import pygame as pg
from GUIClass import GUI
from SimulationClass import Simulation
from config import FPS


class App():
    def __init__(self):
        self.QUI = GUI()
        self.sim = Simulation()

        self.clock = pg.time.Clock()


    def quiting(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()


    def run(self):
        while True:
            self.quiting()
            self.sim.simulation()

            pg.display.set_caption(f"FPS: {round(self.clock.get_fps(), 2)}")
            self.clock.tick(FPS)