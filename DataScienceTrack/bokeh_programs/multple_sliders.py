from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

Slider1 = Slider(title ='slider1', start=0, end =10, step =0.1, value = 2)
Slider2 = Slider(title ='slider2', start=10, end =100, step =1, value = 20)
layout = widgetbox(Slider1, Slider2)
curdoc().add_root(layout)
