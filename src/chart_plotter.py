import plotly.graph_objs as go

def plot_custom_candlestick_chart(data):
    """
    Creates a custom candlestick chart using Plotly.

    Parameters:
        data (pandas.DataFrame): DataFrame containing stock data with columns 'Open', 'High', 'Low', 'Close'.

    Returns:
        plotly.graph_objs.Figure: A Plotly figure object representing the candlestick chart.
    """
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        increasing_line_color='#7FFF00',  # Custom fill color for bullish
        decreasing_line_color='#FF4040',  # Custom fill color for bearish
        increasing_line_width=1,
        decreasing_line_width=1
    )])

    fig.update_layout(
        title='Customized Stock Price Trend',
        xaxis_title='Date',
        yaxis_title='Price',
        showlegend=False,
        height=800  # Adjust this value for the desired height
    )

    return fig
