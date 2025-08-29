"""Entry point for Roam Loot Defend prototype."""
from __future__ import annotations
import os
import sys

import pygame

from core.clock import Clock
from entities.player import Player
from entities.components.movement import MovementComponent


def main() -> None:
    os.environ.setdefault("SDL_VIDEODRIVER", "dummy" if os.environ.get("CI") else "")
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Roam Loot Defend")
    clock = Clock()

    player = Player(position=pygame.Vector2(400, 300), movement=MovementComponent())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.anchor()

        dt = clock.tick()
        player.update(dt)

        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

