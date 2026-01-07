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

        self.bcolor = "White"
        self.border_rect = pygame.Rect(self.main_rect.topleft, size)

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
        self.screen.blit(self.main_surf, self.main_rect)
        pygame.draw.rect(self.screen, self.bcolor, self.border_rect, 2)
        self.screen.blit(self.text, self.text_rect)
    
    def update(self) -> None:
        self.draw()
        self.check_pressed()