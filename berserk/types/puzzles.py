from __future__ import annotations

from typing import Literal, List
from typing_extensions import NotRequired, TypedDict

from .common import Color


DifficultyLevel = Literal["easiest", "easier", "normal", "harder", "hardest"]


class PuzzleUser(TypedDict):
    id: str
    name: str
    color: Color
    rating: int


class PuzzlePerf(TypedDict):
    key: str
    name: str


class PuzzleGame(TypedDict):
    id: str
    perf: PuzzlePerf
    rated: bool
    players: List[PuzzleUser]
    pgn: str
    clock: str


class PuzzleInfo(TypedDict):
    id: str
    rating: int
    plays: int
    solution: List[str]
    themes: List[str]
    initialPly: int


class PuzzleData(TypedDict):
    game: PuzzleGame
    puzzle: PuzzleInfo


class PuzzleRace(TypedDict):
    # Puzzle race ID
    id: str
    # Puzzle race URL
    url: str


class PuzzleBatchResponse(TypedDict):
    """Response from getting a batch of puzzles."""

    puzzles: List[PuzzleData]


class SolvedPuzzle(TypedDict):
    """A puzzle that was solved, for submission in a batch solve."""

    id: str
    win: bool


class PuzzleReplayResponse(TypedDict):
    """Response from getting puzzle replay IDs."""

    ids: List[str]


class PuzzleRacePlayer(TypedDict):
    """A player in a puzzle race."""

    name: str
    score: NotRequired[int]


class PuzzleRaceResult(TypedDict):
    """Result of a puzzle race."""

    id: str
    players: NotRequired[List[PuzzleRacePlayer]]
