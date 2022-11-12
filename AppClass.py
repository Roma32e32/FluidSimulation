import pygame as pg
from GUIClass import GUI
from SimulationClass import Simulation
from VariablesClass import Variables
from config import FPS
import taichi as ti


class App():
    def __init__(self):
        ti.init(arch=ti.cuda)

        self.vars = Variables()
        self.QUI = GUI(self.vars)
        self.sim = Simulation(self.vars)

        self.clock = pg.time.Clock()


    def quiting(self):
        "Обрабатывает закрытие окна приложения"
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()


    def run(self):
        while True:
            self.quiting()
            self.sim.simulation()

            pg.display.set_caption(f"FPS: {round(self.clock.get_fps(), 2)}")
            self.clock.tick(FPS)