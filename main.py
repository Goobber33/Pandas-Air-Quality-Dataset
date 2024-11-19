import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Function to process each data chunk
def process_chunk(chunk):
    """
    Process a single chunk of data:
    - Select and copy 'title' and 'genres' columns.
    - Add a 'count' column to mark each entry.
    - Group by 'title' and 'genres' to calculate the count for each unique pair.
    """
    # Select and copy relevant columns
    details = chunk[['title', 'genres']].copy()
    # Add a 'count' column to mark each entry, initializing as 1
    details.loc[:, 'count'] = 1
    return details

# Connect to SQLite database
conn = sqlite3.connect('output_data.db')
cursor = conn.cursor()

# Create a table for temporary storage
cursor.execute("""
CREATE TABLE IF NOT EXISTS temp_table (
    title TEXT,
    genres TEXT,
    count INTEGER
)
""")
conn.commit()

try:
    # Read the data in chunks to manage large datasets efficiently
    df = pd.read_csv('data.csv', chunksize=100)

    # Process each chunk and store directly into SQLite
    for chunk in df:
        chunk = process_chunk(chunk)
        chunk.to_sql('temp_table', conn, if_exists='append', index=False)

    # Use SQL to aggregate data in the database
    query = """
        SELECT genres, title, SUM(count) as count
        FROM temp_table
        GROUP BY title, genres
    """
    output = pd.read_sql_query(query, conn)

    # Save aggregated results to a permanent table
    output.to_sql('hbo_max_summary', conn, if_exists='replace', index=False)
    print("Data saved to 'hbo_max_summary' table in output_data.db database.")

    # Display top 5 most common genres
    top_genres = output.groupby('genres')['count'].sum().sort_values(ascending=False).head(5)
    print("Top 5 Most Common Genres:")
    print(top_genres)

    # Plot the top 5 genres to visualize the most common types of content
    top_genres.plot(kind='bar', title='Top 5 Most Common Genres', xlabel='Genres', ylabel='Count')
    plt.show()

    # Additional Analysis: Top Titles Per Genre
    top_titles_per_genre = output.groupby('genres').apply(lambda x: x.nlargest(1, 'count')).reset_index(drop=True)
    print("Top Titles Per Genre:")
    print(top_titles_per_genre)

    # Pie Chart for Genre Distribution
    top_genres.plot(kind='pie', autopct='%1.1f%%', title='Genre Distribution')
    plt.ylabel('')
    plt.show()

except FileNotFoundError:
    print("Error: The data file was not found. Please ensure 'data.csv' is in the current directory.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()
