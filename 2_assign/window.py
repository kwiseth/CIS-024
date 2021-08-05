#!/usr/bin/python3.6/window.py

"""Exercising the ezgraphics library
"""
from ezgraphics import GraphicsWindow

# create window access canvas
win = GraphicsWindow()
canvas = win.canvas()

# draw on the canvas
canvas.drawRect(15, 20, 30, 30)

# Wait for user to close GraphicsWindow
win.wait()
