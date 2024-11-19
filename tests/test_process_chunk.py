import unittest
import pandas as pd
from main import process_chunk

class TestProcessChunk(unittest.TestCase):
    
    def setUp(self):
        # Create a sample dataframe to act as a chunk
        self.chunk = pd.DataFrame({
            'Date': ['10/03/2004', '10/03/2004'],
            'Time': ['18.00.00', '19.00.00'],
            'CO(GT)': [2.6, '-200'],  # Mixed numeric and invalid
            'NOx(GT)': [166, 'not_a_number'],  # Invalid string
            'T': [13.6, 13.3],
            'RH': [48.9, 47.7]
        })

    def test_process_chunk(self):
        # Call the function with the sample chunk
        result = process_chunk(self.chunk)

        # Define the expected output
        expected_output = pd.DataFrame({
            'Datetime': pd.to_datetime(['2004-03-10 18:00:00', '2004-03-10 19:00:00']),
            'CO_GT_': [2.6, pd.NA],
            'NOx_GT_': [166, pd.NA],
            'Temperature': [13.6, 13.3],
            'Humidity': [48.9, 47.7],
            'Average_Pollution': [84.3, pd.NA]
        })

        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_output)

if __name__ == '__main__':
    unittest.main()
