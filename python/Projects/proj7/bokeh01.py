# need to import at least 3 things to make your
# bokeh plots work
from bokeh.plotting import figure, show, output_file
#
# we specify an HTML file where the output will go
# if we don't - output goes to bokeh01.html (filename.html)
#
output_file("plot.html")

# load our x and y data
x = [10, 20, 30]
y = [4, 5, 6]

# create a figure
p = figure()

# create a histogram
p.vbar(x=x, top=y, width=0.5)

# render (show) the plot
show(p)
