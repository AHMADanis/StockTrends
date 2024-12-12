# src/chart.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def plot_chart(data, timeframe, canvas):
    """
    Plots a candlestick chart on the provided canvas.
    
    Parameters:
    - data: pandas.DataFrame containing Open, High, Low, Close, and Volume.
    - timeframe: String representing the timeframe (e.g., "5m").
    - canvas: Tkinter canvas where the chart will be displayed.
    """
    fig, ax = plt.subplots(figsize=(8, 4))

    # Plot candlesticks
    for i, row in data.iterrows():
        color = "green" if row["Close"] > row["Open"] else "red"
        ax.plot([i, i], [row["Low"], row["High"]], color=color)  # High-Low line
        ax.plot([i], [row["Open"]], marker="_", color=color)  # Open
        ax.plot([i], [row["Close"]], marker="_", color=color)  # Close

    ax.set_title(f"Stock: {timeframe} Candlesticks")
    ax.set_xticks(range(len(data.index)))
    ax.set_xticklabels(data.index.strftime('%H:%M'), rotation=45)
    ax.set_ylabel("Price")
    ax.grid()

    # Clear canvas and draw new figure
    canvas.delete("all")
    figure_canvas = FigureCanvasTkAgg(fig, canvas)
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
