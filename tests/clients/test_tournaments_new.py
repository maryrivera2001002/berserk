import pytest

from berserk import Client
from utils import skip_if_older_3_dot_10


class TestTournamentsNew:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_played_by_user(self):
        """Validate that played_by_user returns an iterator"""
        res = Client().tournaments.played_by_user(username="DrNykterstein", nb=5)
        assert hasattr(res, '__iter__')
