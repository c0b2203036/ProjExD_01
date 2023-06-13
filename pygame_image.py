import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    kk_img01 = pg.image.load("ex01-20230613/fig/3.png")
    kk_img01 = pg.transform.flip(kk_img01,True,False)
    kk_img02 = pg.transform.rotozoom(kk_img01,10,1.0)
    kk_imgs = [kk_img01, kk_img02]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img, [1600-tmr, 0])
        screen.blit(kk_imgs[tmr%2], [300,200])
        
        pg.display.update()
        tmr += 1        
        clock.tick(100)

        if tmr == 1599:
            tmr = 0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()