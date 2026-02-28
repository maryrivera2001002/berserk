import pytest

from berserk import Client
from berserk.types.challenges import ChallengeJson
from utils import validate, skip_if_older_3_dot_10


class TestChallenges:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_show(self):
        """Validate that the response matches the typed-dict"""
        res = Client().challenges.show(challenge_id="test123")
        validate(ChallengeJson, res)
