import unittest
import sqlite3
import pandas as pd

class TestDatabaseOperations(unittest.TestCase):
    
    def test_save_to_database(self):
        # Connect to an in-memory SQLite database to avoid file creation
        conn = sqlite3.connect(':memory:')
        
        # Create a simple dataframe to save to the database
        df = pd.DataFrame({
            'title': ['Movie A', 'Movie B'],
            'genres': ['Comedy', 'Drama'],
            'count': [5, 3]
        })
        
        # Save the dataframe to the database
        df.to_sql('hbo_max_summary', conn, if_exists='replace', index=False)
        
        # Read back from the database
        result_df = pd.read_sql('SELECT * FROM hbo_max_summary', conn)
        
        # Check if the result matches the original dataframe
        pd.testing.assert_frame_equal(result_df, df)

        # Close the connection
        conn.close()

if __name__ == '__main__':
    unittest.main()
