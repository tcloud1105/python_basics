#making a basic Bokeh line graph

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_csv("data.csv")

#prepare some data
x=df["x"]
y=df["y"]

#prepare the output file
output_file("line.html")

#create a figure object
f=figure()

#create a line plot
f.line(x,y)

#write the plot in the figure object
show(f)


