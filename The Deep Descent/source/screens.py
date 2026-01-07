from .settings import *
from .gui import Button

class BaseScreen:
    def __init__(self):
        self.return_button = Button(
            text = "Return",
            font = FONTS["Small"],
            pos = (1050, 50),
            size = (150, 50)
        )

    def handle_event(self, events: list[pygame.Event]):
        pass

    def draw(self):
        pass

    def update(self):
        pass

class MainMenu(BaseScreen):
    def __init__(self):
        super().__init__()

        self.resource_button = Button(
            text = "Gather Resources",
            font = FONTS["Small"],
            pos = (50, 50),
            size = (150, 50)
        )

        self.mining_button = Button(
            text = "Go Mine",
            font = FONTS["Small"],
            pos = (300, 50),
            size = (150, 50)
        )

        self.forge_button = Button(
            text = "Quests",
            font = FONTS["Small"],
            pos = (550, 50),
            size = (150, 50)
        )

        self.quests_button = Button(
            text = "Forge",
            font = FONTS["Small"],
            pos = (800, 50),
            size = (150, 50)
        )

        self.exit_button = Button(
            text = "Exit",
            font = FONTS["Small"],
            pos = (1050, 50),
            size = (150, 50)
        )

    def draw(self):
        for button in [self.exit_button, self.resource_button, self.mining_button, self.forge_button, self.quests_button]:
            button.draw()
    
    def update(self):
        for button in [self.exit_button, self.resource_button, self.mining_button, self.forge_button, self.quests_button]:
            button.check_pressed()
        
        if self.exit_button.clicked:
            cc()
            pygame.quit()
            close_game()
        
        if self.resource_button.clicked:
            return ResourceScreen()
    
        if self.mining_button.clicked:
            return MiningScreen()

        if self.quests_button.clicked:
            return QuestsScreen()

        if self.forge_button.clicked:
            return ForgingScreen()

        return None

class ResourceScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        self.gather_button = Button(
            text = "Gather",
            font = FONTS["Small"],
            pos = (1250 // 2 - 150 // 2, 750 // 2 - 50 // 2),
            size = (150, 50)
        )

    def roll(self) -> dict:
        return {}

    def draw(self):
        for btn in [self.gather_button, self.return_button]:
            btn.draw()
    
    def update(self):
        for btn in [self.gather_button, self.return_button]:
            btn.update()

        if self.gather_button.clicked:
            return RollScreen(ResourceScreen, self.roll())
        
        if self.return_button.clicked:
            return MainMenu()

class MiningScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        self.mining_button = Button(
            text = "Mine",
            font = FONTS["Small"],
            pos = (1250 // 2 - 150 // 2, 750 // 2 - 50 // 2),
            size = (150, 50)
        )

        self.current_place = "Beginners Hole"

    def roll(self) -> dict:
        items = mining_data.data[self.current_place]

        return random.choices(items, weights = [item["Chance"] for item in items], k = 1)[0]

    def draw(self):
        for btn in [self.mining_button, self.return_button]:
            btn.draw()
    
    def update(self):
        for btn in [self.mining_button, self.return_button]:
            btn.update()
    
        if self.return_button.clicked:
            return MainMenu()
    
        if self.mining_button.clicked:
            return RollScreen(MiningScreen, self.roll())

class ForgingScreen(BaseScreen):
    def __init__(self):
        super().__init__()

    def draw(self):
        self.return_button.draw()
    
    def update(self):
        self.return_button.check_pressed()
    
        if self.return_button.clicked:
            return MainMenu()

class QuestsScreen(BaseScreen):
    def __init__(self):
        super().__init__()

    def draw(self):
        self.return_button.draw()
    
    def update(self):
        self.return_button.check_pressed()
    
        if self.return_button.clicked:
            return MainMenu()

class RollScreen(BaseScreen):
    def __init__(self, return_class: ResourceScreen | MiningScreen, item: dict):
        super().__init__()

        self.continue_button = Button(
            text = "Continue",
            font = FONTS["Small"],
            pos = (SCREEN_WIDTH // 2 - 150 // 2, 565),
            size = (150, 50)
        )
        self.return_class = return_class
        self.item_rolled = item
        print(self.item_rolled)

    def draw(self):
        self.continue_button.draw()
    
    def update(self):
        self.continue_button.check_pressed()

        if self.continue_button.clicked:
            return self.return_class()
        