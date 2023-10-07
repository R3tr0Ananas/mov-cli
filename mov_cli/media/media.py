from __future__ import annotations

__all__ = ("Media", "Series", "Movie", "LiveTV")

class Media():
    """Represents any piece of media in mov-cli that can be streamed or downloaded."""
    def __init__(self, url: str, title: str, referrer: str) -> None:
        self.url = url
        """The stream-able url."""
        self.title = title
        """A title to represent this stream-able media."""
        self.referrer = referrer # TODO: Add docstring for this.

class Series(Media):
    """Represents a TV Show. E.g an Anime or Cartoon"""
    def __init__(
        self, 
        url: str, 
        title: str, 
        referrer: str, 
        episode: int, 
        season: int,
        subtitles: dict | None
    ) -> None:
        self.season = season
        """The season this series belongs to."""
        self.episode = episode
        """The episode number of this series."""
        self.subtitles = subtitles

        super().__init__(
            url, title, referrer
        )

class Movie(Media):
    """Represents a Film/Movie."""
    def __init__(
        self, 
        url: str, 
        title: str, 
        referrer: str, 
        year: int,
        subtitles: dict | None
    ) -> None:
        self.year = year
        """The year this film was released."""
        self.subtitles = subtitles

        super().__init__(
            url, title, referrer
        )

class LiveTV(Media):
    """Represents a live TV Station."""
    def __init__(
        self, 
        url: str, 
        title: str, 
        referrer: str, 
    ) -> None:

        super().__init__(
            url, title, referrer
        )