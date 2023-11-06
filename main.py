import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle
import PySimpleGUI as sg
import math
import matplotlib as mt
import numpy as np
h = 12
w = 2
dt = 0.001
L = 0.5
I0 = 10
b = 0.05
c = 0.01
q0 = 1

class Canvas(FigureCanvasTkAgg):
  """
    Create a canvas for matplotlib pyplot under tkinter/PySimpleGUI canvas
    """

  def __init__(self, figure=None, master=None):
    super().__init__(figure=figure, master=master)
    self.canvas = self.get_tk_widget()
    self.canvas.pack(side='top', fill='both', expand=1)
def cm_to_inch(value):
  return value / 2.54
def f(I,b,w,q, dt):
    return (I - (2 * b * I + w * w * q) * dt)

def plot_figure(b,I0,q0,L,c):
    # if True:
    try:
        ax.cla()
        b = float(b)
        I0 = float(I0)
        q0 = float(q0)
        L = float(L)
        c = float(c)
        w0 = 1/(L*c);
        I = f(I0, b, w0, q0, 0.5 * dt);
        t = [0]
        q = [0]
        i = 0
        while True:
            t.append(t[i]+dt)
            q.append(q[i]+I*dt)
            i = i + 1
            I = f(I, b, w0, q[i], dt)
            if i > 100:
                break
        ax.set_title(r'Затухающие колебания q/t', fontsize=16)
        ax.plot(t, q, color='g')
        canvas.draw()
    except:
        print("err")
        ax.cla()
        return
sg.theme('DefaultNoMoreNagging')
layout = [
    [sg.Canvas(size=(640, 480), key='Canvas')],
    [sg.Text('L'), sg.Input(0.5,enable_events=True,k='-L-',size=(9, 1)),
    sg.Text('I0'), sg.Input(10,enable_events=True,k='-I0-',size=(7, 1)),
    sg.Text('Beta'), sg.Input(0.05,enable_events=True,k='-B-',size=(7, 1)),
    sg.Text('c'), sg.Input(0.01,enable_events=True,k='-C-',size=(7, 1)),
    sg.Text('q0'), sg.Input(1,enable_events=True,k='-Q0-',size=(7, 1))],
    [[sg.Push(), sg.Button('go'), sg.Push()]]
    ]
window = sg.Window('Модель опыта Резерфорда',
                   layout,
                   finalize=True,
                   resizable=True)

fig = Figure(figsize=(cm_to_inch(16), cm_to_inch(10)))

ax = fig.add_subplot()
canvas = Canvas(fig, window['Canvas'].Widget)
def launch():
    plot_figure(b,I0,q0,L,c)
while True:
  event, values = window.read()
  # print(event)
  if event in (sg.WIN_CLOSED, 'Exit'):
    break
  elif event == 'go':
      launch()
  elif event == '-L-':
      L = values[event]
  elif event == '-I0-':
      I0 = values[event]
  elif event == '-Q0-':
      q0 = values[event]
  elif event == '-B-':
      b = values[event]
  elif event == '-C-':
      c = values[event]
