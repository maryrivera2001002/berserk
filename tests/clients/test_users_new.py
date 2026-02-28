import pytest
from typing import List

from berserk import Client
from berserk.types.users import UserNote
from utils import validate, skip_if_older_3_dot_10


class TestUsers:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_get_notes(self):
        """Validate that the response matches the typed-dict"""
        res = Client().users.get_notes(username="DrNykterstein")
        validate(List[UserNote], res)

    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_write_note(self):
        """Validate that writing a note does not raise an exception"""
        Client().users.write_note(username="DrNykterstein", text="Test note")
