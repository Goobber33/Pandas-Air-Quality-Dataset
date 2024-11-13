import unittest
import pandas as pd
from main import process_chunk

class TestProcessChunk(unittest.TestCase):
    
    def setUp(self):
        # Create a sample dataframe to act as a chunk
        self.chunk = pd.DataFrame({
            'title': ['Movie A', 'Movie B', 'Movie A', 'Movie C', 'Movie B'],
            'genres': ['Comedy', 'Drama', 'Comedy', 'Action', 'Drama']
        })

    def test_process_chunk(self):
        # Call the function with the sample chunk
        result = process_chunk(self.chunk)
        
        # Define the expected output
        expected_output = pd.DataFrame({
            'count': [2, 2, 1]
        }, index=pd.MultiIndex.from_tuples(
            [('Movie A', 'Comedy'), ('Movie B', 'Drama'), ('Movie C', 'Action')],
            names=['title', 'genres']
        ))
        
        # Check if the result matches the expected output
        pd.testing.assert_frame_equal(result, expected_output)

if __name__ == '__main__':
    unittest.main()
