import random
import time
import json
import pygame
import threading

from VividText import VividText as vt
from sys import exit as close_game
from os import system, name
from os.path import join

pygame.init()

# Variables
DATA_PATH = join("data")
FONT_PATH = join("fonts")

SCREEN_WIDTH, SCREEN_HEIGHT = 1250, 750
COLORS = {
    "Background": (0, 0, 0)
}
FONTS = {
    "Small": pygame.font.Font(join(FONT_PATH, "ithaca.ttf")),
    "Medium": pygame.font.Font(join(FONT_PATH, "ithaca.ttf"), 30),
    "Large": pygame.font.Font(join(FONT_PATH, "ithaca.ttf"), 45)
}

AMOUNT_WEIGHTS = [0.4, 0.4, 0.3, 0.2, 0.1]

# Functions
def cc():
    system("cls" if name == "nt" else "clear")

# Classes
class DataLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = None
        self.load()
    
    def begin_process(self, tp: str, data: dict | None = None):
        if tp == "Load":
            threading.Thread(target = self.load, daemon = True).start()
        
        elif tp == "Save":
            if data is None:
                raise ValueError(f"Data in {self.__class__.__qualname__} cannot be empty...")
            elif not isinstance(data, dict):
                raise ValueError(f"Data in {self.__class__.__qualname__} must be a dict.")
            threading.Thread(target = self.save, args = (data, ), daemon = False).start()

        else:
            raise ValueError(f"TP in {self.__class__.__qualname__} must be either load or save.")

    def load(self) -> None:
        try:
            with open(self.file_path, "r") as f:
                self.data = json.load(f)

        except Exception as e:
            raise ValueError(f"Something wrong with {self.file_path} in {self.__class__.__qualname__}. Details: {e}")
    
    def save(self, data: dict) -> None:
        try:
            with open(self.file_path, "w") as f:
                json.dump(data, f)
    
        except Exception as e:
            raise ValueError(f"Something wrong with {self.file_path} in {self.__class__.__qualname__}. Details: {e}")

# Shared Data
gathering_data = DataLoader(join(DATA_PATH, "gathering_items.json"))
mining_data = DataLoader(join(DATA_PATH, "mining_items.json"))
