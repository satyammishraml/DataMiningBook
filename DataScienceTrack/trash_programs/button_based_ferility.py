import numpy as np
from bokeh.models import Button
import pandas as pd
from bokeh.plotting import ColumnDataSource
from bokeh.models import Select
from bokeh.io import curdoc, output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.layouts import widgetbox, row

lf = pd.read_csv('../data/female_literacy_fertility.csv')
lf.columns = ['Country ', 'Continent', 'female_literacy', 'fertility', 'population']

fertility = lf.iloc[:, 3].values
female_literacy = lf.iloc[:, 2].values
population = female_literacy+np.random.random(female_literacy.size)*10

plot = figure()


source = ColumnDataSource(data={
    'x' : fertility,
    'y' : female_literacy
})
plot.circle('x', 'y', source=source)

button = Button(label = 'Update Data')

def update():
    source.data = {'x':fertility, 'y':population}



button.on_click(update)

layout = row(button, plot)
curdoc().add_root(layout)
