import random
import time
import json
import pygame

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
    "Small": pygame.font.Font(join(FONT_PATH, "ithaca.ttf"))
}

# Functions
def cc():
    system("cls" if name == "nt" else "clear")

# Classes
class DataLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = self.load()
    
    def begin_process(self, tp: str):
        pass

    def load(self) -> dict:
        data = {}

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at {self.file_path} in {self.__class__.__qualname__}")

        except Exception as e:
            raise ValueError(f"Something wrong with {self.file_path} in {self.__class__.__qualname__}. Details: {e}")
    
        return data
    
    def save(self, data: dict) -> None:
        try:
            with open(self.file_path, "w") as f:
                json.dump(data, f)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at {self.file_path} in {self.__class__.__qualname__}")
    
        except Exception as e:
            raise ValueError(f"Something wrong with {self.file_path} in {self.__class__.__qualname__}. Details: {e}")

