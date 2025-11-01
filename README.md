# tegrastats_parser

Script to run Tegrastats and then parse data from the time-stamped log file obtained. Graphing capabilities are also available.

To run:

```
py main.py
```

Action options will be shown in the command line:
- r (run tegrastats)
- p (parse log file)
- g (graph data)
- a (execute all steps)

### Graphing
Graphing is done using the Bokeh library and axes are synced such that panning/zooming on one plot is mirrored on every other plot for easy comparison.

<img width="1892" height="539" alt="image" src="https://github.com/user-attachments/assets/da815698-00e2-4a63-9b32-1e8db972515b" />

<img width="1889" height="507" alt="image" src="https://github.com/user-attachments/assets/46fe6b63-4180-4594-a02a-e11dbea8fae5" />


To install all dependency libraries, execute the following command
```
pip3 install -r requirements.txt
```
