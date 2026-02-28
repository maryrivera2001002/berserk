from __future__ import annotations

from typing import List
from typing_extensions import NotRequired, TypedDict


class FidePlayer(TypedDict):
    id: int
    name: str
    federation: str
    year: int
    title: NotRequired[str]
    standard: NotRequired[int]
    rapid: NotRequired[int]
    blitz: NotRequired[int]


class FideRatingEntry(TypedDict):
    """A single monthly rating entry for a FIDE player."""

    date: str
    rating: NotRequired[int]


class FideRatingHistory(TypedDict):
    """Rating history of a FIDE player across time controls."""

    standard: NotRequired[List[FideRatingEntry]]
    rapid: NotRequired[List[FideRatingEntry]]
    blitz: NotRequired[List[FideRatingEntry]]
