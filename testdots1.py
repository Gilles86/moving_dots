from psychopy import visual, clock, event
from numpy import random

win = visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

n_frames = 3

n_dots = 100

dot_arrays = []

for frame in range(n_frames):

    dot_xys = random.uniform(-200, 200, (n_dots, 2))

    dot_stim = visual.ElementArrayStim(
        win=win,
        units="pix",
        nElements=n_dots,
        elementTex=None,
        elementMask="circle",
        xys=dot_xys,
        sizes=10
    )

    dot_arrays.append(dot_stim)


for dot_stim in dot_arrays:
    dot_stim.draw()

    win.flip()

    event.waitKeys()

win.close()
