import pytest
from typing import List

from berserk import Client
from berserk.types.broadcast import (
    BroadcastPlayerEntry,
    BroadcastPlayerEntryWithFideAndGames,
    BroadcastTeamEntry,
)
from utils import validate, skip_if_older_3_dot_10


class TestBroadcastsNew:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_reset_round(self):
        """Validate that reset_round does not raise an exception"""
        Client().broadcasts.reset_round(broadcast_round_id="test123")

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_get_players(self):
        """Validate that the response matches the typed-dict"""
        res = Client().broadcasts.get_players(broadcast_tournament_id="test123")
        validate(List[BroadcastPlayerEntry], res)

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_get_player(self):
        """Validate that the response matches the typed-dict"""
        res = Client().broadcasts.get_player(
            broadcast_tournament_id="test123",
            player_id="player456",
        )
        validate(BroadcastPlayerEntryWithFideAndGames, res)

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_get_team_standings(self):
        """Validate that the response matches the typed-dict"""
        res = Client().broadcasts.get_team_standings(
            broadcast_tournament_id="test123",
        )
        validate(List[BroadcastTeamEntry], res)
