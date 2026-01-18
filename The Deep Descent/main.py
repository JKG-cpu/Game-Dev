from source import *

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The Deep Descent")
        self.clock = pygame.time.Clock()

        icon_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.display.set_icon(icon_surface)

        self.current_screen = MainMenu()

    def events(self, events: list[pygame.Event]):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                cc()
                close_game()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    cc()
                    close_game()

    def main(self) -> None:
        while True:
            self.screen.fill(COLORS["Background"])
            dt = self.clock.tick() / 1000

            events = pygame.event.get()
            self.events(events)

            self.current_screen.draw(dt)

            next_screen = self.current_screen.handle_event(events)
            if next_screen:
                self.current_screen = next_screen
                continue

            next_screen = self.current_screen.update(dt)
            if next_screen:
                self.current_screen = next_screen

            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.main()