import time
import datetime
import pandas as pd

# List of tickers
tickers = ['TSLA', 'BTC-USD', 'SNAP', 'AMZN', 'GOOG', 'NFLX', 'META']

# Define the time period
interval = '1d'
period1 = int(time.mktime(datetime.datetime(2019, 1, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2024, 3, 10, 23, 59).timetuple()))

# Initialize an empty DataFrame to hold all the data
all_data = pd.DataFrame()

for ticker in tickers:
    # Construct the query URL
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    # Download the data into a DataFrame
    df = pd.read_csv(query_string)
    # Add a column to identify the ticker
    df['Ticker'] = ticker
    # Append this data to the main DataFrame
    all_data = pd.concat([all_data, df], ignore_index=True)

# Save the concatenated DataFrame to a single CSV file
all_data.to_csv('historical_prices_all.csv', index=False)
