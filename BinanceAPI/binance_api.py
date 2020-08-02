from BinanceAPI.util.binance_historical_data import fetch_trading_data as fetch


if __name__ == "__main__":
    """ set defalt value """
    symbol = "BTCUSDT"
    start_time = "01 Jan 2018"
    end_time = "10 May 2018"
    interval = "1d"

    """ fetch historical data """
    json_file = fetch(symbol, start_time, end_time, interval)
