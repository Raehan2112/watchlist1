from abc import ABC, abstractmethod

class WatchItem(ABC):
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.watched = False

    def mark_as_watched(self):
        self.watched = True

    @abstractmethod
    def display_info(self):
        pass


class Movie(WatchItem):
    def __init__(self, title, genre, duration):
        super().__init__(title, genre)
        self.duration = duration

    def display_info(self):
        status = "✓ Watched" if self.watched else "✗ Not Watched"
        print(f"[Movie] {self.title} ({self.genre}) - {self.duration} min | {status}")


class Series(WatchItem):
    def __init__(self, title, genre, seasons):
        super().__init__(title, genre)
        self.seasons = seasons

    def display_info(self):
        status = "✓ Watched" if self.watched else "✗ Not Watched"
        print(f"[Series] {self.title} ({self.genre}) - {self.seasons} Seasons | {status}")
