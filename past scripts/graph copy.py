import csv
import matplotlib.pyplot as plt
import pandas as pd

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'black', 'orange',
          'purple', 'brown', 'gray', 'cyan', 'magenta']

pairs = [('Time (mS)', 'CPU 0 Load (%)'), ('Time (mS)', 'CPU 1 Load (%)'), ('Time (mS)', 'CPU 2 Load (%)'), ('Time (mS)', 'CPU 3 Load (%)'), ('Time (mS)', 'CPU 4 Load (%)'), ('Time (mS)', 'CPU 5 Load (%)'), ('Time (mS)', 'CPU 6 Load (%)'), ('Time (mS)', 'CPU 7 Load (%)'), ('Time (mS)', 'CPU 8 Load (%)'), ('Time (mS)', 'CPU 9 Load (%)'), ('Time (mS)', 'CPU 10 Load (%)'), ('Time (mS)', 'CPU 11 Load (%)'), ('Time (mS)', 'Used RAM (MB)')]

class Graph:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file, skiprows=[0], header=0, index_col=0)

    def bar_plot(self, x, y):
        plt.figure(figsize=(12, 6))
        plt.title(f'{y} over {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        # Change to scope in on portion of the data
        plt.bar(self.df.index[1000:3000], self.df[y][1000:3000], color='blue', alpha=0.7, width=self.df.index[1]-self.df.index[0] if len(self.df.index) > 1 else 1000)

        # Full data plot
        #plt.bar(self.df.index, self.df[y], color='blue', alpha=0.7, width=self.df.index[1]-self.df.index[0] if len(self.df.index) > 1 else 1000)
        plt.savefig(f'{y} vs {x}.png')
        plt.close()

    def plots(self):
        for pair in pairs:
            self.bar_plot(pair[0], pair[1])

if __name__ == '__main__':
    csv_file = 'tegra_stats_log.csv'

    graph = Graph(csv_file)
    graph.plots()
