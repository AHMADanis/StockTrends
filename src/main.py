import streamlit as st
from data_fetcher import fetch_data
from chart_plotter import plot_custom_candlestick_chart

# available intervals supported by Yahoo Finance
VALID_INTERVALS = ["1m", "5m", "15m", "30m", "1h", "1d", "1wk", "1mo"]

def fetch_and_plot(symbol, interval):
    data = fetch_data(symbol.upper(), interval)
    if data.empty:
        st.error(f"No data found for {symbol.upper()} at {interval} timeframe. Please try another.")
    else:
        st.write(f"Displaying data for {symbol.upper()} at {interval} timeframe.")
        st.write(data.tail(5))  # Display last 5 rows of data
        fig = plot_custom_candlestick_chart(data)
        st.plotly_chart(fig)  # Use plotly_chart for interactive plot

def main():
    """
    Main function for the Stock Trends Analysis App.
    """
    st.title("Stock Trends Analysis")

    # Prepopulate ticker input with "Tesla"
    symbol = st.text_input("Enter Stock Ticker:", "TSLA")

    # Set default interval to "1d"
    default_interval = "1d"

    # Display buttons under the chart for each valid interval
    cols = st.columns(len(VALID_INTERVALS))  # Create columns for buttons
    for i, interval in enumerate(VALID_INTERVALS):
        if cols[i].button(interval, key=interval):  # Use `key` to distinguish between buttons
            st.session_state.selected_interval = interval  # Update the selected interval
            fetch_and_plot(symbol, interval)  # Fetch and plot data for the selected interval
        elif interval == default_interval:
            st.session_state.selected_interval = interval  # Set the default interval if no button is clicked

if __name__ == "__main__":
    main()
