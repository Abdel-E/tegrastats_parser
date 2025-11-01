import argparse
from tegrastats import Tegrastats
from parse import Parse
from graph import Graph

if __name__ == '__main__':
    # User friendly cmd line interface instead of args

    # Collect user input
    action = input("Choose action - (r)un tegrastats, (p)arse log file, (g)raph data, (a)ll steps: ").strip().lower()

    if action == 'r':
        # Run tegrastats
        interval = int(input("Enter logging interval in milliseconds (default 1000): ") or 1000)
        log_file = input("Enter log file name (default output_log.txt): ") or 'output_log.txt'
        verbose = input("Enable verbose output? (y/n): ").strip().lower() == 'y'
        tegrastats = Tegrastats(interval, log_file, verbose)
        tegrastats.run()
    elif action == 'p':
        # Parse log file
        log_file = input("Enter log file name (default output_log.txt): ")
        interval = input("Enter logging interval in milliseconds (default 1000): ")
        parser = Parse(interval, log_file)
        csv_file = parser.parse_file()
    elif action == 'g':
        # Graph data
        csv_file = input("Enter CSV file path: ")
        # data_range = input("Enter data range to plot (e.g., 3600-3700) or leave blank for full data: ")
        graph = Graph(csv_file)
        graph.plots()
        # graph.plots(data_range)
    elif action == 'a':
        # All steps
        interval = int(input("Enter logging interval in milliseconds (default 1000): ") or 1000)
        log_file = input("Enter log file name (default output_log.txt): ") or 'output_log.txt'
        verbose = input("Enable verbose output? (y/n): ").strip().lower() == 'y'
        tegrastats = Tegrastats(interval, log_file, verbose)
        tegrastats.run()
        parser = Parse(interval, log_file)
        csv_file = parser.parse_file()
        graph = Graph(csv_file)
        graph.plots()
    else:
        print("Invalid action. Please choose again.")

    # Command line argument parser
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--interval', '-i', type=int, default=1000, help='Logging interval in milliseconds for tegrastats')
    # parser.add_argument('--log_file', '-f', default='output_log.txt', help='Log file name for tegrastats data')
    # parser.add_argument('--verbose', '-v', action='store_true', help='Prints verbose messages while running tegrastats')
    # parser.add_argument('--only_parse', '-p', action='store_true', help='Parse tegrastats log file without running tegrastats')
    # parser.add_argument('--graph', '-g', action='store_true', help='Plots some useful graphs from tegrastats data parsed')
    # parser.add_argument('--csv', help='Path to existing CSV file to plot (skips parsing)')
    # options = parser.parse_args()

    # # If --csv is provided, skip parsing and go straight to graphing
    # if options.csv:
    #     if options.graph:
    #         graph = Graph(options.csv)
    #         graph.plots()
    #     else:
    #         print("Use --graph with --csv to plot the CSV file")
    #     exit(0)

    # # Otherwise, parse the log file
    # parser = Parse(options.interval, options.log_file)
    # csv_file = parser.parse_file()

    # if not csv_file:
    #     print("Error: Parsing failed. No CSV file generated.")
    #     exit(1)

    # if options.graph:
    #     graph = Graph(csv_file)
    #     graph.plots()
