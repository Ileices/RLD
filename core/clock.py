"""Game clock utilities."""
from __future__ import annotations
import pygame

class Clock:
    """Wrapper around ``pygame.time.Clock`` that tracks delta time.

    This helps keep the rest of the code independent from ``pygame``
    specifics while still providing frame-rate limiting and tick duration.
    """

    def __init__(self, fps: int = 60) -> None:
        self._clock = pygame.time.Clock()
        self.fps = fps
        self.dt = 0.0

    def tick(self) -> float:
        """Advance the clock and return delta time in seconds."""
        self.dt = self._clock.tick(self.fps) / 1000.0
        return self.dt

