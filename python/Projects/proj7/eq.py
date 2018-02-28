from bokeh.plotting import figure, output_file, show

#x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
x = []
x2 = []
for i in range(1,50,1):
	x.append(i)
	x2.append(0-i)

#y = [xx**2 for xx in x]
y = [1/xx for xx in x]
y2 = [1/xx for xx in x2]
output_file("log.html")

# create a new plot with a log axis type
p = figure(plot_width=400, plot_height=400, y_axis_type="log")

p.line(x, y, line_width=2)
p.line(x2, y2, line_width=2)
p.circle(x, y, fill_color="white", size=8)

show(p)
