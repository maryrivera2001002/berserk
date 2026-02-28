import pytest

from berserk import Client
from utils import skip_if_older_3_dot_10


class TestBulkPairingsNew:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_export_games_ndjson(self):
        """Validate that export_games returns an iterator in NDJSON mode"""
        res = Client().bulk_pairings.export_games(
            bulk_pairing_id="test123",
            as_pgn=False,
        )
        # Just verify it returns an iterator
        assert hasattr(res, '__iter__')

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_export_games_pgn(self):
        """Validate that export_games returns an iterator in PGN mode"""
        res = Client().bulk_pairings.export_games(
            bulk_pairing_id="test123",
            as_pgn=True,
        )
        assert hasattr(res, '__iter__')
