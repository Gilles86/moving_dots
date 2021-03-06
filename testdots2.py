from psychopy import visual, clock, event, core
from numpy import random

win = visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

n_frames = 3

n_dots = 25

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


current_frame = 0

while not event.getKeys():

    ISI = core.StaticPeriod(screenHz=60)
    ISI.start(0.1)

    dot_arrays[current_frame].draw()

    win.flip()

    current_frame += 1
    current_frame %= n_frames

    ISI.complete()

win.close()
