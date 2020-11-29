import pygame
from pygame import mixer
pygame.init()
import time
window = pygame.display.set_mode((1000,500))

running = True

keyboardimg= pygame.image.load('keyboard.png')
keysX=500
keysY=250

def keyboard():
    window.blit(keyboardimg, (keysX-keyboardimg.get_width()/2,keysY-keyboardimg.get_height()/2))

w_glow=pygame.image.load('white glow.png')

def glow(x,y):
    window.blit(w_glow,(x,y))


while running:

    window.fill((30,30,30))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    keyboard()

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_a:
            keya=mixer.Sound('piano-g#.wav')
            keya.play()
            glow(180,30)
            pygame.display.update()
            time.sleep(0.4)

        if event.key==pygame.K_z:
            keya=mixer.Sound('piano-a.wav')
            keya.play()
            glow(235,30)
            pygame.display.update()
            time.sleep(0.4)


        if event.key==pygame.K_s:
            keya=mixer.Sound('piano-bb.wav')
            keya.play()
            glow(290,30)
            pygame.display.update()
            time.sleep(0.4)

        if event.key==pygame.K_x:
            keya=mixer.Sound('piano-b.wav')
            keya.play()
            glow(345,30)
            pygame.display.update()
            time.sleep(0.4)
 
        if event.key==pygame.K_c:
            keya=mixer.Sound('piano-c.wav')
            keya.play()
            glow(400,30)
            pygame.display.update()
            time.sleep(0.4)

        if event.key==pygame.K_f:
            keya=mixer.Sound('piano-c#.wav')
            keya.play()
            glow(460,30)
            pygame.display.update()
            time.sleep(0.4)

        if event.key==pygame.K_v:
            keya=mixer.Sound('piano-d.wav')
            keya.play()
            glow(517,30)
            pygame.display.update()
            time.sleep(0.4)

        if event.key==pygame.K_g:
            keya=mixer.Sound('piano-eb.wav')
            keya.play()
            glow(575,30)
            pygame.display.update()
            time.sleep(0.4)

        if event.key==pygame.K_b:
            keya=mixer.Sound('piano-e.wav')
            keya.play()
            glow(633,30)
            pygame.display.update()
            time.sleep(0.4)

        if event.key==pygame.K_n:
            keya=mixer.Sound('piano-f.wav')
            keya.play()
            glow(689,30)
            pygame.display.update()
            time.sleep(0.4)

        if event.key==pygame.K_j:
            keya=mixer.Sound('piano-f#.wav')
            keya.play()
            glow(745,30)
            pygame.display.update()
            time.sleep(0.4)

        if event.key==pygame.K_m:
            keya=mixer.Sound('piano-g.wav')
            keya.play()
            glow(800,30)
            pygame.display.update()
            time.sleep(0.4)

        # if event.key==pygame.K_q and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        #     keya=mixer.Sound('Piano.ff.C6.wav')
        #     keya.play()
        #     time.sleep(0.3)
        #     pygame.display.update()

    pygame.display.update()