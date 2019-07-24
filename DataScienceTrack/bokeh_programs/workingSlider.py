import numpy as np
from bokeh.models import Slider
from bokeh.io import  curdoc

from bokeh.layouts import widgetbox, column
from bokeh.plotting import figure, ColumnDataSource
data ={'x':np.random.random(300), 'y':np.random.random(300)}
x= np.random.random(300)
source = ColumnDataSource(data ={'x':np.random.random(300), 'y':np.random.random(300)})
plot = figure()
plot.circle('x', 'y', source = source)

slider = Slider(title = 'slider', start = 0, end = 10, step = 1, value = 2)

def callback(attr, old, new):
    # Read the current value of the slider: scale
    scale = slider.value
    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)
     # Update source with the new data values
    source.data = {'x':x ,'y': new_y}

    
layout = column(widgetbox(slider), plot)


slider.on_change('value', callback)
curdoc().add_root(layout)

