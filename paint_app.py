from tkinter import *
import  PIL
from PIL import Image,ImageDraw

def save():
    filename = 'image.png'
    image1.save(filename)

def paint(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x), (event.y)