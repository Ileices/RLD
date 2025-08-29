from entities.components.movement import MovementComponent, MovementState
from combat import anchor


def test_attack_multiplier_order():
    mc = MovementComponent()
    mc.state = MovementState.MOVING
    moving = anchor.attack_multiplier(mc)
    mc.state = MovementState.STOPPED
    stopped = anchor.attack_multiplier(mc)
    mc.state = MovementState.ANCHORED
    anchored = anchor.attack_multiplier(mc)
    assert moving <= stopped <= anchored


def test_defense_multiplier_order():
    mc = MovementComponent()
    mc.state = MovementState.MOVING
    moving = anchor.defense_multiplier(mc)
    mc.state = MovementState.STOPPED
    stopped = anchor.defense_multiplier(mc)
    mc.state = MovementState.ANCHORED
    anchored = anchor.defense_multiplier(mc)
    assert moving <= stopped <= anchored

