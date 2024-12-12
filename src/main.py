import streamlit as st
from data_fetcher import fetch_data
from chart_plotter import plot_custom_candlestick_chart

# available intervals supported by Yahoo Finance
VALID_INTERVALS = ["1m", "5m", "15m", "30m", "1h", "1d", "1wk", "1mo"]

def main():
    """
    Main function for the Stock Trends Analysis App.
    """
    st.title("Stock Trends Analysis")

    # Text input to select ticker
    symbol = st.text_input("Enter Stock Ticker:", value="TSLA")

    # session state variable to track the selected timeframe
    if "selected_interval" not in st.session_state:
        st.session_state.selected_interval = "1m"

    # Display buttons for each valid interval
    st.write("Select Time Frame:")
    cols = st.columns(len(VALID_INTERVALS))  # Create columns for buttons
    for i, interval in enumerate(VALID_INTERVALS):
        if cols[i].button(interval):
            st.session_state.selected_interval = interval  # Update the selected interval

    # Fetch and display data
    if st.button("Fetch Data"):
        selected_interval = st.session_state.selected_interval  # Use the selected interval
        data = fetch_data(symbol.upper(), selected_interval)
        if data.empty:
            st.error(f"No data found for {symbol.upper()} at {selected_interval} timeframe. Please try another.")
        else:
            st.write(f"Displaying data for {symbol.upper()} at {selected_interval} timeframe.")
            st.write(data.tail(5))  # Display last 5 rows of data

            # Plot custom filled candlestick chart
            fig = plot_custom_candlestick_chart(data)
            st.plotly_chart(fig)  # Use plotly_chart for interactive plot

if __name__ == "__main__":
    main()
