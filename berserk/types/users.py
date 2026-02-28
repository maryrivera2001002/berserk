from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class UserNote(TypedDict):
    """A private note about a user."""

    from_: NotRequired[str]
    to: NotRequired[str]
    text: str
    date: NotRequired[int]
