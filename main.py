from sys import displayhook
import pandas as pd

# Read the data in chunks of 100 rows to handle large datasets efficiently
df = pd.read_csv('data.csv', chunksize=100)

# Initialize an empty DataFrame to accumulate results from each chunk
output = pd.DataFrame()

for chunk in df:
    # Create a copy of the 'title' and 'genres' columns to avoid modification warnings
    details = chunk[['title', 'genres']].copy()
    # Add a 'count' column to track occurrences, initializing each as 1
    details.loc[:, 'count'] = 1

    # Group by 'title' and 'genres' and get a summary count for each unique pair
    summary = details.groupby(['title', 'genres']).sum()

    # Append the current chunk’s summary to the output DataFrame
    output = pd.concat([output, summary])

# Shuffle all rows in the output to randomize the order of entries
random_sample = output.sample(frac=1)
# Display the first few rows of the randomized DataFrame
displayhook(random_sample.head())
