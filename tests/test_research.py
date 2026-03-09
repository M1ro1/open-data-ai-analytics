import unittest
from unittest.mock import patch
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from research import research_data


class TestResearchData(unittest.TestCase):

    @patch("research.pd.read_csv")
    def test_research_data_runs(self, mock_read_csv):
        mock_df = pd.DataFrame({
            "BRAND": ["Toyota", "BMW", "Toyota", "Audi", "BMW"],
        })
        mock_read_csv.return_value = mock_df

        research_data()

        mock_read_csv.assert_called_once_with("data/raw/vehicle_registrations.csv")

    @patch("research.pd.read_csv")
    def test_research_data_top_brands(self, mock_read_csv):
        mock_df = pd.DataFrame({
            "BRAND": ["Toyota"] * 10 + ["BMW"] * 8 + ["Audi"] * 5 + ["Ford"] * 3 + ["Fiat"] * 2 + ["Kia"],
        })
        mock_read_csv.return_value = mock_df

        research_data()

    @patch("research.pd.read_csv")
    def test_research_data_reads_correct_file(self, mock_read_csv):
        mock_df = pd.DataFrame({"BRAND": ["Toyota"]})
        mock_read_csv.return_value = mock_df

        research_data()

        mock_read_csv.assert_called_once_with("data/raw/vehicle_registrations.csv")

    @patch("research.pd.read_csv")
    def test_research_data_single_brand(self, mock_read_csv):
        mock_df = pd.DataFrame({
            "BRAND": ["Toyota", "Toyota", "Toyota"],
        })
        mock_read_csv.return_value = mock_df

        research_data()

    @patch("research.pd.read_csv")
    def test_research_data_many_brands(self, mock_read_csv):
        brands = [f"Brand_{i}" for i in range(100)]
        mock_df = pd.DataFrame({"BRAND": brands})
        mock_read_csv.return_value = mock_df

        research_data()


if __name__ == "__main__":
    unittest.main()

