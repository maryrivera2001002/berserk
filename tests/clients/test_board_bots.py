import pytest

from berserk import Client
from utils import skip_if_older_3_dot_10


class TestBoard:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_claim_draw(self):
        """Validate that claim_draw does not raise an exception"""
        Client().board.claim_draw(game_id="testgame123")


class TestBots:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_claim_victory(self):
        """Validate that claim_victory does not raise an exception"""
        Client().bots.claim_victory(game_id="testgame123")

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_claim_draw(self):
        """Validate that claim_draw does not raise an exception"""
        Client().bots.claim_draw(game_id="testgame123")
