import numpy as np
import pygame as pg
import random
from collections import Counter

def neighboringCells(position):
    for x,y in [(-1,-1),(0,-1),(1,-1),
                (-1,0),(1,0),
                (-1,1),(0,1),(1,1)]:
        yield position[0] + x, position[1] + y
def nextGenerationField(field):
    neighbors = Counter([position for cell in field for position in neighboringCells(cell)])
    return {position for position, counter in neighbors.items() if counter==3 or (counter==2 and position in field)}

def getFieldSize(field, width, height):
    Xs, Ys = zip(*field)
    minX, maxX, minY, maxY = min(Xs), max(Xs), min(Ys), max(Ys)
    columns, rows= maxX-minX+1, maxY-minY+1
    return width/columns, height/rows, -minX, -minY


field = {(random.randrange(200),random.randrange(200)) for I in range(2000)}

pg.init()
screenWidth = screenHeight = 1000
sceen = pg.display.set_mode([screenWidth, screenHeight])

while True:
    sceen.fill((0,0,0))
    field = nextGenerationField(field)
    for x,y in field:
        cellWidth, cellHeight, offsetX, offsetY = getFieldSize(field, screenWidth, screenHeight)
        pg.draw.rect(sceen, (255,0,0),((x+offsetX)*cellWidth, (y+offsetY)*cellHeight, 5, 5))
    pg.display.flip()
pg.quit()






