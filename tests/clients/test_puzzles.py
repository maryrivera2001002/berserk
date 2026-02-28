import pytest

from berserk import Client, PuzzleData
from berserk.types.puzzles import (
    PuzzleBatchResponse,
    PuzzleReplayResponse,
    PuzzleRaceResult,
)
from utils import validate, skip_if_older_3_dot_10


class TestPuzzles:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_get_next(self):
        """Validate that the response matches the typed-dict"""
        res = Client().puzzles.get_next(angle="anastasiaMate", difficulty="hardest")
        validate(PuzzleData, res)

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_get_batch(self):
        """Validate that the response matches the typed-dict"""
        res = Client().puzzles.get_batch(angle="mix", nb=5)
        validate(PuzzleBatchResponse, res)

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_solve_batch(self):
        """Validate that solve_batch returns a PuzzleBatchResponse"""
        res = Client().puzzles.solve_batch(
            angle="mix",
            solved=[{"id": "abc123", "win": True}],
            nb=5,
        )
        validate(PuzzleBatchResponse, res)

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_get_replay(self):
        """Validate that the response matches the typed-dict"""
        res = Client().puzzles.get_replay(days=30, theme="mix")
        validate(PuzzleReplayResponse, res)

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_get_race(self):
        """Validate that the response matches the typed-dict"""
        res = Client().puzzles.get_race(race_id="test123")
        validate(PuzzleRaceResult, res)
