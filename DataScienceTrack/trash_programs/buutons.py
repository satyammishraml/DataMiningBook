from bokeh.models import Button
from bokeh.models import  ColumnDataSource
from bokeh.layouts import column
from bokeh.plotting import figure
import numpy as np
from bokeh.io import curdoc, output_file, show

source = ColumnDataSource(data = {'x':np.random.random(300), 'y':np.random.random(300)})
plot = figure()
plot.circle('x', 'y', source =source)


button = Button(label = 'Update Data')


def update():
    y = np.random.random(300)
    source.data = {'x':np.random.random(900), 'y':np.random.random(900)}

button.on_click(update)


layout = column(button, plot)
curdoc().add_root(layout)
