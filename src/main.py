import streamlit as st
from data_fetcher import fetch_data
from chart_plotter import plot_custom_candlestick_chart

def main():
    """
    Main function for the Stock Trends Analysis App.
    """
    st.title("Stock Trends Analysis")

    # Text input to select ticker
    symbol = st.text_input("Enter Stock Ticker:", value="TSLA")

    # Fetch and display data
    if st.button("Fetch Data"):
        data = fetch_data(symbol.upper())
        if data.empty:
            st.error("No data found for the entered ticker symbol. Please try again.")
        else:
            st.write(f"Displaying data for {symbol.upper()}")
            st.write(data.tail(5))  # Display last 5 rows of data

            # Plot custom filled candlestick chart
            fig = plot_custom_candlestick_chart(data)
            st.plotly_chart(fig)  # Use plotly_chart for interactive plot

if __name__ == "__main__":
    main()
