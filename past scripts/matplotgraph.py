import csv
import matplotlib.pyplot as plt
import pandas as pd

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'black', 'orange',
          'purple', 'brown', 'gray', 'cyan', 'magenta']

pairs = [('Time (mS)', 'CPU 0 Load (%)'), ('Time (mS)', 'CPU 1 Load (%)'), ('Time (mS)', 'CPU 2 Load (%)'), ('Time (mS)', 'CPU 3 Load (%)'), ('Time (mS)', 'CPU 4 Load (%)'), ('Time (mS)', 'CPU 5 Load (%)'), ('Time (mS)', 'CPU 6 Load (%)'), ('Time (mS)', 'CPU 7 Load (%)'), ('Time (mS)', 'CPU 8 Load (%)'), ('Time (mS)', 'CPU 9 Load (%)'), ('Time (mS)', 'CPU 10 Load (%)'), ('Time (mS)', 'CPU 11 Load (%)'), ('Time (mS)', 'Used RAM (MB)')]

class Graph:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file, skiprows=[0], header=0, index_col=1)

    def bar_plot(self, x, y):
        fig = plt.figure()
        gs = fig.add_gridspec(5, 3, hspace=1.2, wspace=0.4, height_ratios=[1, 1, 1, 1, 1])
        axs = gs.subplots(sharex=True)

        plt.subplots_adjust(left=0.05, right=0.95)
        # fig, axes = plt.subplots(nrows=5, ncols=3, sharex=True, squeeze=True, figsize=(20, 15))
        
        # Plot each cpu core and RAM in its own subplot
        for i, ax in enumerate(axs.flatten()):
            if i < 12:  # CPU cores
                column_name = f'CPU {i} Load (%)'
            elif i == 12:  # RAM
                column_name = 'Used RAM (MB)'
            else:
                ax.axis('off')  # Hide unused subplots
                continue

            ax.set_title(column_name + " vs. Time (mS)")
            ax.set_xlabel("Time (mS)")
            # ax.set_ylabel(column_name)

            ax.bar(self.df.index, self.df[column_name], color='blue', alpha=0.7, width=self.df.index[1]-self.df.index[0] if len(self.df.index) > 1 else 1000)
        
        plt.show()

    def plots(self):
        self.bar_plot(self.df.index[0], self.df.columns[0])


if __name__ == '__main__':
    csv_file = 'tegra_stats_log.csv'

    graph = Graph(csv_file)
    graph.plots()
