import pygame as pg


WINDOW_HEIGTH = 600
WINDOW_WIDTH = 600
TITLE = "basic project"


class Game:
    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption(TITLE)
        self.surface = pg.display.set_mode((WINDOW_HEIGTH, WINDOW_WIDTH))
        self.clock = pg.time.Clock()
        self.loop = True
        

    def main(self):
        while self.loop:
            self.game_loop()
        pg.quit()

    
    def game_loop(self):
        self.surface.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
            elif event.type == pg.K_ESCAPE:
                self.loop = False

        # draw a cirle, delete later...
        pg.draw.circle(self.surface, (255, 0, 0), (100, 100), 20)

        self.clock.tick(60)
        pg.display.update()
        pg.time.delay(100)

    
if __name__ == "__main__":
    game = Game()
    game.main()
