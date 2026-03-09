import unittest
from unittest.mock import patch
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from quality import check_quality


class TestCheckQuality(unittest.TestCase):

    @patch("quality.pd.read_csv")
    def test_check_quality_runs(self, mock_read_csv):
        mock_df = pd.DataFrame({
            "BRAND": ["Toyota", "BMW", None],
            "MODEL": ["Corolla", "X5", "Leaf"],
            "FUEL": ["Бензин", "Дизель", "Електро"],
        })
        mock_read_csv.return_value = mock_df

        check_quality()

        mock_read_csv.assert_called_once_with("data/raw/vehicle_registrations.csv")

    @patch("quality.pd.read_csv")
    def test_check_quality_detects_nulls(self, mock_read_csv):
        mock_df = pd.DataFrame({
            "BRAND": [None, None, "Toyota"],
            "MODEL": ["Corolla", None, "Camry"],
        })
        mock_read_csv.return_value = mock_df

        check_quality()

    @patch("quality.pd.read_csv")
    def test_check_quality_detects_duplicates(self, mock_read_csv):
        mock_df = pd.DataFrame({
            "BRAND": ["Toyota", "Toyota", "BMW"],
            "MODEL": ["Corolla", "Corolla", "X5"],
        })
        mock_read_csv.return_value = mock_df

        check_quality()

    @patch("quality.pd.read_csv")
    def test_check_quality_empty_dataframe(self, mock_read_csv):
        mock_df = pd.DataFrame()
        mock_read_csv.return_value = mock_df

        check_quality()

    @patch("quality.pd.read_csv")
    def test_check_quality_reads_correct_file(self, mock_read_csv):
        mock_df = pd.DataFrame({"A": [1]})
        mock_read_csv.return_value = mock_df

        check_quality()

        mock_read_csv.assert_called_once_with("data/raw/vehicle_registrations.csv")


if __name__ == "__main__":
    unittest.main()

