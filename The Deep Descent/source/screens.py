from .settings import *
from .gui import Button, BaseItem

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

    def draw(self, dt):
        pass

    def update(self, dt):
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

    def draw(self, dt):
        for button in [self.exit_button, self.resource_button, self.mining_button, self.forge_button, self.quests_button]:
            button.draw()
    
    def update(self, dt):
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

        self.current_place = "Vigilant Forest"

    def roll(self) -> dict:
        items = gathering_data.data[self.current_place]["Items"]

        item = random.choices(items, weights = [itm["Chance"] for itm in items], k = 1)[0]
        item["Amount"] = random.choices([1, 2, 3, 4, 5], weights = AMOUNT_WEIGHTS, k = 1)[0]

        return item

    def misc_items(self) -> list[str]:
        return [(item["Name"], item["Dis-Color"]) for item in gathering_data.data[self.current_place]["Items"]]

    def draw(self, dt):
        for btn in [self.gather_button, self.return_button]:
            btn.draw()
    
    def update(self, dt):
        for btn in [self.gather_button, self.return_button]:
            btn.update()

        if self.gather_button.clicked:
            return RollScreen(ResourceScreen, self.roll(), self.misc_items())
        
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
        items = mining_data.data[self.current_place]["Items"]

        item = random.choices(items, weights = [itm["Chance"] for itm in items], k = 1)[0]
        item["Amount"] = random.choices([1, 2, 3, 4, 5], weights = AMOUNT_WEIGHTS, k = 1)[0]
        item["Purity Rate"] = random.choices([amt for amt in item["Purity"]], weights = [item["Purity"][amt] for amt in item["Purity"]], k = 1)[0]

        return item

    def misc_items(self) -> list[str]:
        return [(item["Name"], item["Dis-Color"]) for item in mining_data.data[self.current_place]["Items"]]

    def draw(self, dt):
        for btn in [self.mining_button, self.return_button]:
            btn.draw()
    
    def update(self, dt):
        for btn in [self.mining_button, self.return_button]:
            btn.update()
    
        if self.return_button.clicked:
            return MainMenu()
    
        if self.mining_button.clicked:
            return RollScreen(MiningScreen, self.roll(), self.misc_items())

class ForgingScreen(BaseScreen):
    def __init__(self):
        super().__init__()

    def draw(self, dt):
        self.return_button.draw()
    
    def update(self, dt):
        self.return_button.check_pressed()
    
        if self.return_button.clicked:
            return MainMenu()

class QuestsScreen(BaseScreen):
    def __init__(self):
        super().__init__()

    def draw(self, dt):
        self.return_button.draw()
    
    def update(self, dt):
        self.return_button.check_pressed()
    
        if self.return_button.clicked:
            return MainMenu()

class RollScreen(BaseScreen):
    def __init__(self, return_class: ResourceScreen | MiningScreen, item: dict, misc_items: list[tuple[str, str]]):
        super().__init__()

        # Button Stuff
        self.continue_button = Button(
            text = "Continue",
            font = FONTS["Small"],
            pos = (SCREEN_WIDTH // 2 - 150 // 2, 565),
            size = (150, 50)
        )
        
        self.button_alpha = 0
        self.fade_speed = 75

        self.animated_buttons = []

        self.add_button(
            self.continue_button,
            offset_y = 20,
            speed = 0.5
        )

        # Return Class
        self.return_class = return_class

        # Item Stuff
        self.item_rolled = item
        self.items = random.choices(misc_items, k = 5)
        self.items.append((self.item_rolled["Name"], self.item_rolled["Dis-Color"]))
    
        self.starting_point = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150)
        self.ending_point = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)

        self.time = pygame.time.get_ticks()
        self.cd = 500
        self.index = 0

        self.item = BaseItem(*self.items[self.index], FONTS["Large"], self.starting_point)

    def add_button(self, button: Button, offset_y = 20, speed = 1.5) -> None:
        start_pos = button.get_pos()
        end_pos = (start_pos[0], start_pos[1] + offset_y)

        self.animated_buttons.append({
            "button": button,
            "start": start_pos,
            "end": end_pos,
            "progress": 0.0,
            "speed": speed
        })
 
    def smooth_step(self, t) -> int | float:
        return 1 - (1 - t) ** 3

    def fade_in_buttons(self, dt) -> None:
        for animation in self.animated_buttons:
            animation["progress"] += animation["speed"] * dt
            animation["progress"] = min(animation["progress"], 1.0)

            p = self.smooth_step(animation["progress"])
            btn = animation["button"]

            # Fade
            btn.set_alpha(int(255 * p))

            # Movement
            sx, sy = animation["start"]
            ex, ey = animation["end"]
            
            x = sx + (ex - sx) * p
            y = sy + (ey - sy) * p

            btn.reset_pos((x, y))

    def draw_item(self) -> None:
        self.item.draw()

    def draw(self, dt) -> None:
        current_time = pygame.time.get_ticks()

        if current_time - self.time >= self.cd:
            self.time = pygame.time.get_ticks()
            self.index = self.index + 1 if self.index < len(self.items) - 1 else len(self.items) - 1
            self.item = BaseItem(*self.items[self.index], FONTS["Large"], self.starting_point)
        
        self.draw_item()

        # Draw continue button ONLY if self.index == len(self.items) - 1 (Fade in???)
        if self.index == len(self.items) - 1:
            self.fade_in_buttons(dt)

            for animation in self.animated_buttons:
                animation["button"].draw()
    
    def update(self, dt) -> None | MiningScreen | ResourceScreen:
        if not self.index == len(self.items) - 1:
            return

        self.continue_button.check_pressed()

        if self.continue_button.clicked:
            return self.return_class()
        