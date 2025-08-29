"""Anchor-related combat utilities."""
from __future__ import annotations

from entities.components.movement import MovementComponent, MovementState


def attack_multiplier(movement: MovementComponent) -> float:
    """Return attack multiplier based on movement state."""
    return movement.attack_multipliers[movement.state]


def defense_multiplier(movement: MovementComponent) -> float:
    """Return defense multiplier based on movement state."""
    return movement.defense_multipliers[movement.state]


def can_anchor(movement: MovementComponent) -> bool:
    """Check if the component can enter anchor state."""
    return movement.state is MovementState.STOPPED

