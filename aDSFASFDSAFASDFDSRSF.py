import time
import random
from adafruit_circuitplayground.express import cpx

select = 0
volume = 0
volSelect = 5

while True:
    cpx.pixels[select] = (255,255,255)
    cpx.volume = volume

    if (cpx.button_a) and select < 4:
        select += 1
        cpx.pixels[select - 1] = (0,0,0)
        time.sleep(0.2)

    if (cpx.button_b) and select > 0:
        select -= 1
        cpx.pixels[select + 1] = (0,0,0)
        time.sleep(0.2)

    if cpx.touch_A2 and volume < 1:
        volume += 0.25
        print(volume)
        time.sleep(0.2)
        cpx.pixels[volSelect] = (0,255,0)

    if cpx.touch_A3 and volume > 0:
        volume -= 0.25
        print(volume)
        time.sleep(0.2)
        cpx.pixels[volSelect] = (0,255,0)




    if (cpx.touch_A1) and select == 0:
        cpx.play_tone(15000, 2)