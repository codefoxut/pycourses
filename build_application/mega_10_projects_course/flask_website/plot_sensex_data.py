import pandas_datareader.data as web
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import CDN


def plot_data():
    dfs = web.DataReader('^SNX', 'stooq')

    def inc_dec(c, o):
        if c > o:
            value = "inc"
        elif o > c:
            value = "dec"
        else:
            value = "same"
        return value

    dfs["status"] = [inc_dec(c, o) for c, o in zip(dfs.Close, dfs.Open)]
    dfs["mid"] = (dfs.Close + dfs.Open) / 2
    dfs["height"] = abs(dfs.Close - dfs.Open)

    f = figure(x_axis_type='datetime', width=1000, height=300, title='Candlestick Chart', sizing_mode="scale_width")
    f.grid.grid_line_alpha = 0.3

    hours_12 = 12 * 60 * 60 * 1000
    # hover = HoverTool(tooltips=[("Start", "@Open"), ("End", "@Close")])
    # f.add_tools(hover)
    df = dfs[:200]
    f.segment(df.index, df.High, df.index, df.Low, color="black")
    f.rect(df.index[df.status == "inc"],
           df.mid[df.status == "inc"],
           hours_12,
           df.height[df.status == "inc"],
           fill_color="green",
           line_color="black")

    f.rect(df.index[df.status == "dec"],
           df.mid[df.status == "dec"],
           hours_12,
           df.height[df.status == "dec"],
           fill_color="red",
           line_color="black")

    script1, div1 = components(f)
    cdn_js = CDN.js_files
    return script1, div1, cdn_js
