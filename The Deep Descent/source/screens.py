from .settings import *
from .gui import Button

class BaseScreen:
    def handle_event(self, events: list[pygame.Event]):
        pass

    def draw(self):
        pass

    def update(self):
        pass

class MainMenu(BaseScreen):
    def __init__(self):
        self.resource_button = Button(
            text = "Gather Resources",
            font = FONTS["Small"],
            pos = (50, 50),
            size = (150, 50),
            color = "Black",
            border_color = "White"
        )

        self.mining_button = Button(
            text = "Go Mine",
            font = FONTS["Small"],
            pos = (300, 50),
            size = (150, 50),
            color = "Black",
            border_color = "White"
        )

        self.exit_button = Button(
            text = "Exit",
            font = FONTS["Small"],
            pos = (1000, 50),
            size = (150, 50),
            color = "Black",
            border_color = "White"
        )

    def draw(self):
        for button in [self.exit_button, self.resource_button, self.mining_button]:
            button.draw()
    
    def update(self):
        for button in [self.exit_button, self.resource_button, self.mining_button]:
            button.check_pressed()
        
        if self.exit_button.clicked:
            cc()
            pygame.quit()
            close_game()
        
        if self.resource_button.clicked:
            return ResourceScreen()
    
        if self.mining_button.clicked:
            return MiningScreen()

        return None

class ResourceScreen(BaseScreen):
    def __init__(self):
        self.gather_button = Button(
            text = "Gather",
            font = FONTS["Small"],
            pos = (1250 // 2 - 150 // 2, 750 // 2 - 50 // 2),
            size = (150, 50),
            color = "Black",
            border_color = "White"
        )

        self.return_button = Button(
            text = "Return",
            font = FONTS["Small"],
            pos = (1000, 50),
            size = (150, 50),
            color = "Black",
            border_color = "White"
        )

    def draw(self):
        self.gather_button.draw()
        self.return_button.draw()
    
    def update(self):
        self.gather_button.check_pressed()
        self.return_button.check_pressed()

        if self.gather_button.clicked:
            print("Gathering")
        
        if self.return_button.clicked:
            return MainMenu()

class MiningScreen(BaseScreen):
    def __init__(self):
        self.return_button = Button(
            text = "Return",
            font = FONTS["Small"],
            pos = (1000, 50),
            size = (150, 50),
            color = "Black",
            border_color = "White"
        )
    
    def draw(self):
        self.return_button.draw()
    
    def update(self):
        self.return_button.check_pressed()
    
        if self.return_button.clicked:
            return MainMenu()

