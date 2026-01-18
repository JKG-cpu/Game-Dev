from ..settings import *

class Button:
    def __init__(self, 
                text: str, 
                font: pygame.font.Font, 
                pos: tuple[int, int], 
                size: tuple[int, int]
        ) -> None:
        self.screen = pygame.display.get_surface()
        self.clicked = False

        self.main_surf = pygame.Surface(size, pygame.SRCALPHA)
        self.main_surf.fill("Black")
        self.main_rect = self.main_surf.get_frect(topleft = pos)

        self.border_surf = pygame.Surface((size[0] + 5, size[1] + 5), pygame.SRCALPHA)
        self.border_surf.fill("White")
        self.border_rect = self.border_surf.get_frect(center = self.main_rect.center)

        self.text = font.render(text, False, "White")
        self.text_rect = self.text.get_frect(center = self.main_rect.center)

        self.main_surf.blit(self.text, self.text_rect)

    def check_pressed(self) -> None:
        mouse_pos = pygame.mouse.get_pos()

        if self.main_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_just_pressed()[0]:
                self.clicked = True
            
            else:
                self.clicked = False
        
        else:
            self.clicked = False

    def draw(self) -> None:
        self.screen.blit(self.border_surf, self.border_rect)
        self.screen.blit(self.main_surf, self.main_rect)
        self.screen.blit(self.text, self.text_rect)
    
    def update(self) -> None:
        self.draw()
        self.check_pressed()

    def set_alpha(self, alpha: int) -> None:
        alpha = max(0, min(alpha, 255))
        
        for item in [self.text, self.border_surf]:
            item.set_alpha(alpha)

    def reset_pos(self, pos: tuple[int, int]) -> None:
        for rect in [self.border_rect, self.main_rect, self.text_rect]:
            rect.center = pos

    def get_pos(self) -> tuple[int, int]:
        return self.main_rect.center

class BaseItem:
    def __init__(self, text: str, text_color: str, font: pygame.font.Font, pos: tuple[int, int]):
        self.screen = pygame.display.get_surface()
        self.text = font.render(f"{text}", True, text_color).convert_alpha()
        self.text_rect = self.text.get_frect(center = pos)

    def reset_pos(self, pos: tuple[int, int]):
        self.text_rect.center = pos

    def get_pos(self) -> tuple[float, float] | tuple[int, int]:
        return self.text_rect.center

    def draw(self):
        self.screen.blit(self.text, self.text_rect)