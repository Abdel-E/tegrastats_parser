import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

class Graph:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def plots(self):
        # Read CSV file
        df = pd.read_csv(self.csv_file, skiprows=[0])
        data = {}
        headers = df.columns
        for header in headers:
            data[header] = df[header].values

        # Create plots for CPU loads and RAM usage
        plots = []
        time = data['Time (mS)']
        
        # First plot (no linked ranges yet)
        p0 = figure(title='CPU 0 Load (%) vs Time (s)', 
                    x_axis_label='Time (s)', 
                    y_axis_label='CPU Load (%)',
                    x_range=[0, max(time) / 1000],
                    y_range=[0, 105],
                    width=620, height=500,
                    output_backend="webgl",
                    tools=["xpan", "xwheel_zoom", "reset", "save"],
                    )
        p0.vbar(x=(time/1000), top=data['CPU 0 Load (%)'], width=0.001)
        plots.append(p0)

        # Remaining CPU plots (linked to first plot's ranges)
        for i in range(1, 12):
            p = figure(title=f'CPU {i} Load (%) vs Time (s)', 
                      x_axis_label='Time (s)', 
                      y_axis_label='CPU Load (%)',
                      x_range=p0.x_range, 
                      y_range=p0.y_range,
                      width=620, height=500,
                      output_backend="webgl",
                      tools=["xpan", "xwheel_zoom", "reset", "save"],
                      
                      )
            p.vbar(x=(time/1000), top=data[f'CPU {i} Load (%)'], width=0.001)
            plots.append(p)

        # RAM usage plot (linked x only)
        p_emc = figure(title='Used EMC (%) vs Time (s)', 
                      x_axis_label='Time (s)', 
                      y_axis_label='Used EMC (%)',
                      x_range=p0.x_range,
                      y_range=[0, data['Used EMC (%)'].max() + 5],
                      width=620, height=500,
                      output_backend="webgl",
                      tools=["xpan", "xwheel_zoom", "reset", "save"],
                      )
        p_emc.vbar(x=(time/1000), top=data['Used EMC (%)'], width=0.001, color='green')
        plots.append(p_emc)

        # Arrange plots in a grid and show
        grid = gridplot(plots, ncols=3)
        output_file("tegrastats_plots.html")
        show(grid)

if __name__ == '__main__':
    csv_file = 'tegra_stats_log.csv'
    graph = Graph(csv_file)
    graph.plots()