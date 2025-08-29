"""Movement component handling movement/stop/anchor states."""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto

class MovementState(Enum):
    MOVING = auto()
    STOPPED = auto()
    ANCHORED = auto()

@dataclass
class MovementComponent:
    """Track movement state and basic power multipliers."""
    speed: float = 200.0
    anchor_time: float = 1.0

    state: MovementState = MovementState.STOPPED
    _anchor_timer: float = 0.0

    # Multipliers that follow the design rule: anchored >= stopped >= moving
    attack_multipliers = {
        MovementState.MOVING: 0.5,
        MovementState.STOPPED: 1.0,
        MovementState.ANCHORED: 2.0,
    }
    defense_multipliers = {
        MovementState.MOVING: 0.5,
        MovementState.STOPPED: 1.0,
        MovementState.ANCHORED: 2.0,
    }

    def update(self, dt: float, input_vector) -> None:
        """Update position/state based on input and timers."""
        if self.state is MovementState.ANCHORED:
            self._anchor_timer -= dt
            if self._anchor_timer <= 0:
                self.state = MovementState.STOPPED
        elif input_vector.length_squared() > 0:
            self.state = MovementState.MOVING
        else:
            self.state = MovementState.STOPPED

    def try_anchor(self) -> bool:
        """Attempt to enter the anchor state.

        Returns ``True`` if anchoring succeeds.
        """
        if self.state is MovementState.STOPPED:
            self.state = MovementState.ANCHORED
            self._anchor_timer = self.anchor_time
            return True
        return False

