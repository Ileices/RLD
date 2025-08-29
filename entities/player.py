"""Player entity implementation."""
from __future__ import annotations
from dataclasses import dataclass, field
import pygame

from .components.movement import MovementComponent

@dataclass
class Player:
    position: pygame.Vector2
    movement: MovementComponent
    color: pygame.Color = field(default_factory=lambda: pygame.Color('white'))
    radius: int = 15

    def handle_input(self) -> pygame.Vector2:
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            direction.x += 1
        return direction

    def update(self, dt: float) -> None:
        direction = self.handle_input()
        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.position += direction * self.movement.speed * dt
        self.movement.update(dt, direction)

    def anchor(self) -> None:
        self.movement.try_anchor()

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.position, self.radius)

