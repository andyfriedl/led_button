import sys
import pygame
from gpiozero import LED, Button

led = LED(17)
button = Button(2)

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
SONG_END = pygame.USEREVENT + 1
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('8bit.mp3')
while True:
    button.wait_for_press()

    print('Light up led')
    led.on()
    pygame.mixer.music.play()
    playing = True

    while playing == True:
        for event in pygame.event.get():
            if event.type == SONG_END:
                print("the song ended!")
                print('turn off led')
                led.off()
                playing = False

sys.exit(0)
SystemExit: 0