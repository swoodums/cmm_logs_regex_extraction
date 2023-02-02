import unittest
import os
from cmm_logs_regex_extraction_v2 import logs_to_csv
import pandas as pd
class TestLogsToCsv(unittest.TestCase):
    def setUp(self) -> None:
        self.input_filepath = os.path.abspath('./test_data')
        self.output_filepath = os.path.abspath('./example_output.csv')

    def test_execute(self):
        logs_to_csv(self.input_filepath,self.output_filepath)
        results_df = pd.read_csv(self.output_filepath)
        self.assertTrue(len(results_df)>0)

    def tearDown(self) -> None:
        if os.path.exists(self.output_filepath):
            os.remove(self.output_filepath)
