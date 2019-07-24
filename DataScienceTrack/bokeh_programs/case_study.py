# Neccessary Imports
from bokeh.io import curdoc, output_file, show
from bokeh.plotting import figure
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, CategoricalColorMapper
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row
from bokeh.models import Slider, HoverTool, Select


# Read data into dataframe
df = pd.read_csv('gapminder_tidy.csv', index_col= 'Year')
df.columns
# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x'       : df.loc[1970].fertility,
    'y'       : df.loc[1970].life,
    'region' : df.loc[1970].region,
    'gdp':    df.loc[1970].gdp,
    'fertility':df.loc[1970].fertility,
    'life':df.loc[1970].life,
    'cmortality': df.loc[1970].child_mortality,
    'country': df.loc[1970].Country,
    'pop': (df.loc[1970].population/ 20000000) + 2,
})
# Save the minimum and maximum values of the fertility column: xmin, xmax
xmin, xmax = min(df.fertility), max(df.fertility)
# Save the minimum and maximum values of the life expectancy column: ymin, ymax
ymin, ymax = min(df.life), max(df.life)

# Create the figure: plot
p = figure(title='Gapminder Data for 1970', plot_height=400, plot_width=700,
              x_range=(xmin, xmax), y_range=(ymin, ymax))
p.yaxis.axis_label = 'Life Expectancy (years)'
p.xaxis.axis_label = 'Fertility (children per woman)'

# Make a list of the unique values from the region column: regions_list
regions_list = df.region.unique().tolist()
# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors = regions_list, palette=Spectral6)
# Add a circle glyph to the figure p
p.circle(x='x', y='y', source=source, fill_alpha = 0.8, color = dict(field = 'region', transform = color_mapper), legend = 'region')
slider = Slider(title = 'Change Year', start= 1970, end = 2010, step = 1, value = 1970)

#define the callback function : update_plot
def update_plot(attr, old, new):
    yr = slider.value
    x = x_select.value
    y = y_select.value
    p.xaxis.axis_label = x
    p.yaxis.axis_label = y
    new_data = {
    'x' : df.loc[yr][x],
    'y' : df.loc[yr][y],
    'region' : df.loc[yr].region,
    'gdp': df.loc[yr].gdp,
    'fertility':df.loc[yr].fertility,
    'life':df.loc[yr].life,
    'cmortality': df.loc[yr].child_mortality,
    'country': df.loc[yr].Country,
    'pop': (df.loc[yr].population/ 20000000) + 2,
    }
    source.data = new_data
    p.title.text ='Gapminder Data for %d' %yr

slider.on_change('value', update_plot)
x_select = Select(options = ['fertility', 'life', 'population', 'gdp'], title= 'x-axis data', value='fertility')
x_select.on_change('value', update_plot)

y_select = Select(options = ['fertility', 'life', 'population', 'gdp'], title= 'y-axis data', value='life')
y_select.on_change('value', update_plot)


hover = HoverTool(tooltips =[('Country', '@country')] )
p.add_tools(hover)
# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider, x_select, y_select), p)
curdoc().add_root(layout)
curdoc().title = 'Gapminder'
