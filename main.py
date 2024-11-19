import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Function to process each data chunk
def process_chunk(chunk):
    """
    Process a single chunk of data:
    - Rename columns to remove special characters.
    - Select relevant columns.
    - Add a 'count' column to mark each entry.
    """
    # Rename columns to remove special characters
    chunk.columns = chunk.columns.str.replace('[^A-Za-z0-9_]', '_', regex=True)

    # Display sanitized column names for debugging
    print("Sanitized Column Names:", chunk.columns.tolist())

    # Select and copy relevant columns (updated for sanitized names)
    details = chunk[['Date', 'Time', 'CO_GT_', 'C6H6_GT_', 'T', 'RH']].copy()

    # Add a 'count' column to mark each entry, initializing as 1
    details.loc[:, 'count'] = 1
    return details


# Connect to SQLite database
conn = sqlite3.connect('output_data.db')
cursor = conn.cursor()

# Drop the table if it already exists to avoid schema conflicts
cursor.execute("DROP TABLE IF EXISTS temp_table")

# Create a table for temporary storage
cursor.execute("""
CREATE TABLE temp_table (
    Date TEXT,
    Time TEXT,
    CO_GT_ REAL,
    C6H6_GT_ REAL,
    T REAL,
    RH REAL,
    count INTEGER
)
""")
conn.commit()

try:
    # Read the data in chunks to manage large datasets efficiently
    df = pd.read_csv('processed_air_quality.csv', chunksize=100)

    # Process each chunk and store directly into SQLite
    for chunk in df:
        chunk = process_chunk(chunk)
        chunk.to_sql('temp_table', conn, if_exists='append', index=False)

    # Use SQL to aggregate data in the database
    query = """
        SELECT Date, AVG(CO_GT_) as Avg_CO_GT, AVG(C6H6_GT_) as Avg_C6H6_GT, 
               AVG(T) as Avg_Temperature, AVG(RH) as Avg_Relative_Humidity
        FROM temp_table
        GROUP BY Date
    """
    output = pd.read_sql_query(query, conn)

    # Save aggregated results to a permanent table
    output.to_sql('air_quality_summary', conn, if_exists='replace', index=False)
    print("Data saved to 'air_quality_summary' table in output_data.db database.")

    # Display the top 5 days with the highest average CO levels
    top_days_CO = output.nlargest(5, 'Avg_CO_GT')
    print("Top 5 Days with Highest Average CO Levels:")
    print(top_days_CO)

    # Plot average CO levels over time
    output.plot(x='Date', y='Avg_CO_GT', kind='line', title='Average CO Levels Over Time', xlabel='Date', ylabel='Average CO (GT)')
    plt.show()

    # Additional Analysis: Correlation between Benzene (C6H6) and CO Levels
    output.plot(x='Avg_CO_GT', y='Avg_C6H6_GT', kind='scatter', title='Correlation between CO and C6H6 Levels', xlabel='Average CO (GT)', ylabel='Average C6H6 (GT)')
    plt.show()

    # Pie Chart for Average Relative Humidity Distribution
    top_days_humidity = output.nlargest(5, 'Avg_Relative_Humidity')
    top_days_humidity.plot(kind='pie', y='Avg_Relative_Humidity', labels=top_days_humidity['Date'], autopct='%1.1f%%', title='Top 5 Days with Highest Relative Humidity')
    plt.ylabel('')
    plt.show()

except FileNotFoundError:
    print("Error: The data file was not found. Please ensure 'processed_air_quality.csv' is in the current directory.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()
