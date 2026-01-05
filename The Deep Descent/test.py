import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 40)


class ScreenBase:
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass


class MainMenu(ScreenBase):
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return GameScreen()  # switch screen
        return None

    def draw(self, surface):
        surface.fill((30, 30, 30))
        text = FONT.render("Press ENTER to Play", True, (200, 200, 200))
        surface.blit(text, (150, 180))


class GameScreen(ScreenBase):
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return MainMenu()  # go back
        return None

    def draw(self, surface):
        surface.fill((10, 10, 40))
        text = FONT.render("Game Screen (ESC to Menu)", True, (200, 200, 200))
        surface.blit(text, (90, 180))


def main():
    current_screen = MainMenu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            next_screen = current_screen.handle_event(event)
            if next_screen:
                current_screen = next_screen

        current_screen.update()
        current_screen.draw(screen)

        pygame.display.flip()
        clock.tick(60)


main()
