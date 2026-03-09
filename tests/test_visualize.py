import unittest
from unittest.mock import patch
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from visualize import create_viz


class TestCreateViz(unittest.TestCase):

    @patch("visualize.plt")
    @patch("visualize.pd.read_csv")
    def test_create_viz_runs(self, mock_read_csv, mock_plt):
        mock_df = pd.DataFrame({
            "FUEL": ["Бензин", "Дизель", "Бензин", "Електро", "Дизель"],
        })
        mock_read_csv.return_value = mock_df

        create_viz()

        mock_read_csv.assert_called_once_with("data/raw/vehicle_registrations.csv")

    @patch("visualize.plt")
    @patch("visualize.pd.read_csv")
    def test_create_viz_saves_figure(self, mock_read_csv, mock_plt):
        mock_df = pd.DataFrame({
            "FUEL": ["Бензин", "Дизель", "Електро"],
        })
        mock_read_csv.return_value = mock_df

        create_viz()

        mock_plt.savefig.assert_called_once_with("reports/figures/fuel_distribution.png")

    @patch("visualize.plt")
    @patch("visualize.pd.read_csv")
    def test_create_viz_tight_layout(self, mock_read_csv, mock_plt):
        mock_df = pd.DataFrame({
            "FUEL": ["Бензин"],
        })
        mock_read_csv.return_value = mock_df

        create_viz()

        mock_plt.tight_layout.assert_called_once()

    @patch("visualize.plt")
    @patch("visualize.pd.read_csv")
    def test_create_viz_reads_correct_file(self, mock_read_csv, mock_plt):
        mock_df = pd.DataFrame({"FUEL": ["Бензин"]})
        mock_read_csv.return_value = mock_df

        create_viz()

        mock_read_csv.assert_called_once_with("data/raw/vehicle_registrations.csv")

    @patch("visualize.plt")
    @patch("visualize.pd.read_csv")
    def test_create_viz_multiple_fuel_types(self, mock_read_csv, mock_plt):
        mock_df = pd.DataFrame({
            "FUEL": ["Бензин"] * 50 + ["Дизель"] * 30 + ["Електро"] * 15 + ["Газ"] * 5,
        })
        mock_read_csv.return_value = mock_df

        create_viz()

        mock_plt.savefig.assert_called_once()


if __name__ == "__main__":
    unittest.main()

