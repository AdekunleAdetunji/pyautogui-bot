import pyautogui as pag
import pyinputplus as pyip

def down(distance):
    pag.drag(0, -distance, duration = 0.2)

def right(distance):
    pag.drag(distance, 0, duration = 0.2)

def up(distance):
    pag.drag(0, distance, duration = 0.2)

def left(distance):
    pag.drag(-distance, 0, duration = 0.2)

def colorChange(x, y):
    position = pag.position()
    pag.moveTo(x, y, duration = 0.2), pag.click()
    pag.moveTo(position[0], position[1], duration = 0.2)

def bot():
    size = pyip.inputInt('Enter the size of the spiral: ')
    start = pyip.inputInt('Enter the lenght of the innermost shell: ')
    space = pyip.inputInt('Enter the spacing to be between sides: ')
    distance = start
    pag.sleep(5)
    while size > distance:
        colorChange(1191,88)
        down(distance)
        colorChange(1262,86)
        right(distance)
        distance += space
        colorChange(1358,85)
        up(distance)
        colorChange(1289,119)
        left(distance)
        distance += space
