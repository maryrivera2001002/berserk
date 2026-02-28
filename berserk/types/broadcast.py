from __future__ import annotations

from typing import List

from typing_extensions import NotRequired, TypedDict

from .common import LightUser, Title


class BroadcastPlayer(TypedDict):
    # The name of the player as it appears on the source PGN
    source_name: str
    # The name of the player as it will be displayed on Lichess
    display_name: str
    # Rating, optional
    rating: NotRequired[int]
    # Title, optional
    title: NotRequired[Title]


class BroadcastTourInfo(TypedDict):
    website: NotRequired[str]
    players: NotRequired[str]
    location: NotRequired[str]
    tc: NotRequired[str]
    fideTc: NotRequired[str]
    timeZone: NotRequired[str]
    standings: NotRequired[str]
    format: NotRequired[str]


class BroadcastTour(TypedDict):
    id: str
    name: str
    slug: str
    createdAt: int
    dates: NotRequired[List[int]]
    info: NotRequired[BroadcastTourInfo]
    tier: NotRequired[int]
    image: NotRequired[str]
    description: NotRequired[str]
    leaderboard: NotRequired[bool]
    teamTable: NotRequired[bool]
    url: str
    communityOwner: NotRequired[LightUser]


class BroadcastCustomPointsPerColor(TypedDict):
    win: float
    draw: float


class BroadcastCustomScoring(TypedDict):
    white: BroadcastCustomPointsPerColor
    black: BroadcastCustomPointsPerColor


class BroadcastRoundInfo(TypedDict):
    id: str
    name: str
    slug: str
    createdAt: int
    rated: bool
    ongoing: NotRequired[bool]
    startsAt: NotRequired[int]
    startsAfterPrevious: NotRequired[bool]
    finishedAt: NotRequired[int]
    finished: NotRequired[bool]
    url: NotRequired[str]
    delay: NotRequired[int]
    customScoring: NotRequired[BroadcastCustomScoring]


class BroadcastWithLastRound(TypedDict):
    group: NotRequired[str]
    tour: BroadcastTour
    round: BroadcastRoundInfo
    roundToLink: NotRequired[BroadcastRoundInfo]


class PaginatedBroadcasts(TypedDict):
    currentPage: int
    maxPerPage: int
    currentPageResults: List[BroadcastWithLastRound]
    previousPage: NotRequired[int | None]
    nextPage: NotRequired[int | None]


class BroadcastTop(TypedDict):
    active: List[BroadcastWithLastRound]
    upcoming: List[None]  # deprecated
    past: PaginatedBroadcasts


class BroadcastByUser(TypedDict):
    tour: BroadcastTour


class BroadcastsByUser(TypedDict):
    currentPage: int
    maxPerPage: int
    currentPageResults: List[BroadcastByUser]
    nbResults: int
    previousPage: int | None
    nextPage: int | None
    nbPages: int


class BroadcastPlayerFideInfo(TypedDict):
    """FIDE info for a broadcast player."""

    id: NotRequired[int]
    name: NotRequired[str]
    federation: NotRequired[str]


class BroadcastPlayerEntry(TypedDict):
    """A player entry in a broadcast tournament."""

    name: str
    rating: NotRequired[int]
    title: NotRequired[str]
    fideId: NotRequired[int]
    fed: NotRequired[str]
    played: NotRequired[int]
    score: NotRequired[float]


class BroadcastPlayerGame(TypedDict):
    """A game played by a broadcast player."""

    id: NotRequired[str]
    round: NotRequired[str]
    opponent: NotRequired[str]
    color: NotRequired[str]
    result: NotRequired[str]


class BroadcastPlayerEntryWithFideAndGames(TypedDict):
    """A single broadcast player with FIDE info and games."""

    name: str
    rating: NotRequired[int]
    title: NotRequired[str]
    fideId: NotRequired[int]
    fed: NotRequired[str]
    played: NotRequired[int]
    score: NotRequired[float]
    fide: NotRequired[BroadcastPlayerFideInfo]
    games: NotRequired[List[BroadcastPlayerGame]]


class BroadcastTeamEntry(TypedDict):
    """A team entry in a broadcast tournament team leaderboard."""

    name: str
    score: NotRequired[float]
    played: NotRequired[int]
    players: NotRequired[List[str]]
