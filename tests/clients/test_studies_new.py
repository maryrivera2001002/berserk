import pytest

from berserk import Client
from utils import skip_if_older_3_dot_10


class TestStudiesNew:
    @skip_if_older_3_dot_10
    @pytest.mark.vcr
    def test_update_chapter_tags(self):
        """Validate that update_chapter_tags does not raise an exception"""
        Client().studies.update_chapter_tags(
            study_id="teststudy123",
            chapter_id="testchapter456",
            pgn='[White "Test Player"]',
        )
