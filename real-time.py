

# código de https://rehn.me/posts/python-real-time-plotting.html


import numpy as np

from bokeh.driving import count
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure


UPDATE_INTERVAL = 100
ROLLOVER = 50

source = ColumnDataSource({"x": [], "y": []})

yb = 0

@count()
def update(x):
    global yb
    yb += np.random.normal()
    source.stream({"x": [x], "y": [yb]}, rollover=ROLLOVER)


p = figure()
p.line("x", "y", source=source)

doc = curdoc()
doc.add_root(p)
doc.add_periodic_callback(update, UPDATE_INTERVAL)

