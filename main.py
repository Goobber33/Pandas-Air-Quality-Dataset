from sys import displayhook
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Function to process each data chunk
def process_chunk(chunk):
    # Select and copy 'title' and 'genres' columns to avoid modification warnings
    details = chunk[['title', 'genres']].copy()
    # Add a 'count' column to mark each entry, initializing as 1
    details.loc[:, 'count'] = 1
    # Group by 'title' and 'genres' and calculate the count for each unique pair
    return details.groupby(['title', 'genres']).sum()

# Read the data in chunks to manage large datasets efficiently
df = pd.read_csv('data.csv', chunksize=100)
output = pd.DataFrame()

# Process each chunk and accumulate the results
for chunk in df:
    summary = process_chunk(chunk)
    output = pd.concat([output, summary])

# Save the final output to a SQLite database for storage and later retrieval
conn = sqlite3.connect('output_data.db')
output.to_sql('hbo_max_summary', conn, if_exists='replace', index=False)
print("Data saved to output_data.db database.")

# Display top 5 most common genres
top_genres = output.groupby('genres')['count'].sum().sort_values(ascending=False).head(5)
print("Top 5 Most Common Genres:")
print(top_genres)

# Plot the top 5 genres to visualize the most common types of content
top_genres.plot(kind='bar', title='Top 5 Most Common Genres', xlabel='Genres', ylabel='Count')
plt.show()