from bokeh.plotting import figure, show

p = figure(plot_width=800, plot_height=500)
p.annulus(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], inner_radius=0.1, outer_radius=0.25,
          color="orange", alpha=0.6)

show(p)

