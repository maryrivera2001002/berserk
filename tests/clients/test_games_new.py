import pytest

from berserk import Client
from utils import skip_if_older_3_dot_10


class TestGamesNew:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_export_bookmarks_ndjson(self):
        """Validate that export_bookmarks returns an iterator in NDJSON mode"""
        res = Client().games.export_bookmarks(as_pgn=False)
        assert hasattr(res, '__iter__')

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_export_bookmarks_pgn(self):
        """Validate that export_bookmarks returns an iterator in PGN mode"""
        res = Client().games.export_bookmarks(as_pgn=True)
        assert hasattr(res, '__iter__')
