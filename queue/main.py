import pathlib 
import pygame as pg

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

def main():
    pg.init()
    background_image = pg.image.load(str(pathlib.Path(__file__).parent.parent / "assets" / "title_screen_prototype.jpeg")).convert()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SCALED)
    pg.display.set_caption("The Queue")

    running = True
    while running:        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # GAME RENDER HERE
        scaled_background = pg.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        screen.blit(scaled_background, (0, 0))
        pg.display.flip()


    pg.quit()

if __name__ == "__main__":
    main()
