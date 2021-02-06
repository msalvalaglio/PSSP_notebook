<table style="float:left; border:none">
   <tr style="border:none">
       <td style="border:none">
           <a href="https://bokeh.org/">     
           <img 
               src="assets/bokeh-transparent.png" 
               style="width:50px"
           >
           </a>    
       </td>
       <td style="border:none">
           <h1>Bokeh Tutorial</h1>
       </td>
   </tr>
</table>
<div style="float:right;"><h2>00. Introduction and Setup</h2></div>

# Tutorial Overview

The tutorial is broken into several sections, which are each presented in their own notebook:

1.  [Basic Plotting](01%20-%20Basic%20Plotting.ipynb)
2.  [Styling and Theming](02%20-%20Styling%20and%20Theming.ipynb)
3.  [Data Sources and Transformations](03%20-%20Data%20Sources%20and%20Transformations.ipynb)
4.  [Adding Annotations](04%20-%20Adding%20Annotations.ipynb)
5.  [Presentation and Layouts](05%20-%20Presentation%20Layouts.ipynb)
6.  [Linking and Interactions](06%20-%20Linking%20and%20Interactions.ipynb)
7.  [Bar and Categorical Data Plots](07%20-%20Bar%20and%20Categorical%20Data%20Plots.ipynb)
8.  [Graph and Network Plots](08%20-%20Graph%20and%20Network%20Plots.ipynb)
9.  [Geographic Plots](09%20-%20Geographic%20Plots.ipynb)
10. [Exporting and Embedding](10%20-%20Exporting%20and%20Embedding.ipynb)
11. [Running Bokeh Applications](11%20-%20Running%20Bokeh%20Applications.ipynb)

As well as some extra topic appendices:

A1. [Models and Primitives](A1%20-%20Models%20and%20Primitives.ipynb)<br />
A2. [Visualizing Big Data with Datashader](A2%20-%20Visualizing%20Big%20Data%20with%20Datashader.ipynb)<br />
A3. [High-Level Charting with Holoviews](A3%20-%20High-Level%20Charting%20with%20Holoviews.ipynb)<br />
A4. [Additional Resources](A4%20-%20Additional%20Resources.ipynb)

## What is Bokeh

Bokeh is an interactive visualization library that targets modern web browsers for presentation. It is good for:

* Interactive visualization in modern browsers
* Standalone HTML documents, or server-backed apps
* Expressive and versatile graphics
* Large, dynamic or streaming data
* Easy usage from python (or Scala, or R, or...)

And most importantly:

## <center><i>NO JAVASCRIPT REQUIRED</i></center>

Bokeh is an interactive visualization library for modern web browsers. It provides elegant, concise construction of versatile graphics, and affords high-performance interactivity over large or streaming datasets. Bokeh can help anyone who would like to quickly and easily make interactive plots, dashboards, and data applications.

## What can I *do* with Bokeh

# Standard imports 

from bokeh.io import output_notebook, show
output_notebook()

# Plot a complex chart with interactive hover in a few lines of code

from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.sampledata.autompg import autompg_clean as df
from bokeh.transform import factor_cmap

df.cyl = df.cyl.astype(str)
df.yr = df.yr.astype(str)

group = df.groupby(by=['cyl', 'mfr'])
source = ColumnDataSource(group)

p = figure(plot_width=800, plot_height=300, title="Mean MPG by # Cylinders and Manufacturer",
           x_range=group, toolbar_location=None, tools="")

p.xgrid.grid_line_color = None
p.xaxis.axis_label = "Manufacturer grouped by # Cylinders"
p.xaxis.major_label_orientation = 1.2

index_cmap = factor_cmap('cyl_mfr', palette=['#2b83ba', '#abdda4', '#ffffbf', '#fdae61', '#d7191c'], 
                         factors=sorted(df.cyl.unique()), end=1)

p.vbar(x='cyl_mfr', top='mpg_mean', width=1, source=source,
       line_color="white", fill_color=index_cmap, 
       hover_line_color="darkgrey", hover_fill_color=index_cmap)

p.add_tools(HoverTool(tooltips=[("MPG", "@mpg_mean"), ("Cyl, Mfr", "@cyl_mfr")]))

show(p)

# Create and deploy interactive data applications

from IPython.display import IFrame
IFrame('https://demo.bokeh.org/sliders', width=900, height=500)

# Getting set up

from IPython.core.display import Markdown
Markdown(open("README.md").read())

### Setup-test, run the next cell. Hopefully you should see output that looks something like this:

    IPython - 7.9.0
    Pandas - 0.25.2
    Bokeh - 1.4.0
    
If this isn't working for you, see the [`README.md`](README.md) in this directory.

from IPython import __version__ as ipython_version
from pandas import __version__ as pandas_version
from bokeh import __version__ as bokeh_version
print("IPython - %s" % ipython_version)
print("Pandas - %s" % pandas_version)
print("Bokeh - %s" % bokeh_version)

# Next Section

Click on this link to go to the next notebook: [01 - Basic Plotting](01%20-%20Basic%20Plotting.ipynb)

