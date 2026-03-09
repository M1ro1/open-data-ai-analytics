import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_load import download_data


class TestDownloadData(unittest.TestCase):

    @patch("data_load.os.makedirs")
    @patch("data_load.pd.read_csv")
    def test_download_data_success(self, mock_read_csv, mock_makedirs):
        mock_df = MagicMock(spec=pd.DataFrame)
        mock_df.__len__ = MagicMock(return_value=100)
        mock_df.head.return_value = "mocked head"
        mock_read_csv.return_value = mock_df

        download_data()

        mock_read_csv.assert_called_once()
        args, kwargs = mock_read_csv.call_args
        self.assertEqual(kwargs["sep"], ";")
        self.assertEqual(kwargs["encoding"], "utf-8")

        mock_makedirs.assert_called_once_with("data/raw", exist_ok=True)
        mock_df.to_csv.assert_called_once_with("data/raw/vehicle_registrations.csv", index=False)

    @patch("data_load.pd.read_csv", side_effect=Exception("Network error"))
    def test_download_data_failure(self, mock_read_csv):
        try:
            download_data()
        except Exception:
            self.fail("download_data() raised an unexpected exception")

    @patch("data_load.os.makedirs")
    @patch("data_load.pd.read_csv")
    def test_download_data_creates_directory(self, mock_read_csv, mock_makedirs):
        mock_df = MagicMock(spec=pd.DataFrame)
        mock_df.__len__ = MagicMock(return_value=5)
        mock_df.head.return_value = "head"
        mock_read_csv.return_value = mock_df

        download_data()

        mock_makedirs.assert_called_once_with("data/raw", exist_ok=True)

    @patch("data_load.os.makedirs")
    @patch("data_load.pd.read_csv")
    def test_download_data_saves_without_index(self, mock_read_csv, mock_makedirs):
        mock_df = MagicMock(spec=pd.DataFrame)
        mock_df.__len__ = MagicMock(return_value=10)
        mock_df.head.return_value = "head"
        mock_read_csv.return_value = mock_df

        download_data()

        mock_df.to_csv.assert_called_once_with("data/raw/vehicle_registrations.csv", index=False)


if __name__ == "__main__":
    unittest.main()

