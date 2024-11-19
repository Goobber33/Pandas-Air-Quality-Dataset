import unittest
import sqlite3
import pandas as pd

class TestDatabaseOperations(unittest.TestCase):
    
    def setUp(self):
        # Connect to an in-memory SQLite database
        self.conn = sqlite3.connect(':memory:')
        self.df = pd.DataFrame({
            'Datetime': ['2004-03-10 18:00:00', '2004-03-10 19:00:00'],
            'CO_GT_': [2.6, 1.2],
            'NOx_GT_': [166, 103],
            'Temperature': [13.6, 13.3],
            'Humidity': [48.9, 47.7],
            'Average_Pollution': [84.3, 52.1]
        })

    def test_save_to_database(self):
        # Save the dataframe to the database
        self.df.to_sql('air_quality', self.conn, if_exists='replace', index=False)

        # Read back from the database
        result_df = pd.read_sql('SELECT * FROM air_quality', self.conn)

        # Check if the result matches the original dataframe
        pd.testing.assert_frame_equal(result_df, self.df)

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
