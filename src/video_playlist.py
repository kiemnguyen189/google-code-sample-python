"""A video playlist class."""

from typing import Sequence
from .video import Video


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_title: str, videos: Sequence[Video]):
        """Video constructor."""
        self._title = playlist_title
        self._videos = list(videos)

    @property
    def title(self) -> str:
        """Returns the title of a playlist."""
        return self._title

    @property
    def tags(self) -> Sequence[Video]:
        """Returns the list of videos in a playlist."""
        return self._videos
