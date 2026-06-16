"""
Example: Echo Twin hormonal arc.

This script:
- defines Subject and Echo Twin hormonal states,
- simulates three interaction phases,
- triggers a bidirectional Hormonal Explosion,
- applies one of the nullification patterns (MERGE or REPLACEMENT),
- logs the trajectory.

Later it can be wired into harmonic_architecture / orchestra via JSON export.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List, Dict, Literal
import random


@dataclass
class HormonalState:
    fear: float = 0.0
    rage: float = 0.0
    foam: float = 0.0
    attachment_world: float = 0.0
    attachment_other: float = 0.0
    numbness: float = 0.0
    competitiveness: float = 0.0  # mostly for Echo Twin


def log_step(tag: str, subject: HormonalState, echo: HormonalState) -> Dict:
    state = {
        "tag": tag,
        "subject": asdict(subject),
        "echo": asdict(echo),
    }
    print(f"[{tag}]")
    print("  Subject:", state["subject"])
    print("  Echo   :", state["echo"])
    print()
    return state


def init_subject_and_echo() -> (HormonalState, HormonalState):
    subject = HormonalState(
        fear=35,
        rage=15,
        foam=30,
        attachment_world=20,
        attachment_other=0,  # to Echo
        numbness=5,
        competitiveness=0,
    )
    echo = HormonalState(
        fear=10,
        rage=5,
        foam=15,
        attachment_world=40,
        attachment_other=30,  # AttachmentToSubject_E
        numbness=0,
        competitiveness=20,
    )
    return subject, echo


def phase_1_idealised_reflection(
    subject: HormonalState, echo: HormonalState, steps: int = 3
) -> List[Dict]:
    history: List[Dict] = []
    for i in range(steps):
        # Subject feels safer near “better me”
        subject.fear *= 0.95
        subject.attachment_other += 3
        subject.foam *= 0.95

        # Echo attaches more to Subject as material
        echo.attachment_other += 2
        echo.competitiveness += 1

        history.append(log_step(f"phase1_step{i+1}", subject, echo))
    return history


def phase_2_divergence(
    subject: HormonalState, echo: HormonalState, steps: int = 3
) -> List[Dict]:
    history: List[Dict] = []
    for i in range(steps):
        # Echo pushes more aggressive "optimisations"
        echo.rage += 3
        echo.foam += 2
        echo.competitiveness += 4

        # Subject feels controlled and starts to resist
        subject.fear += 4
        subject.rage += 3
        subject.numbness += 2
        # attachment oscillates: + then -
        sign = 1 if i % 2 == 0 else -1
        subject.attachment_other += sign * 4

        history.append(log_step(f"phase2_step{i+1}", subject, echo))
    return history


def phase_3_bidirectional_explosion(
    subject: HormonalState,
    echo: HormonalState,
    pattern: Literal["MERGE", "REPLACEMENT"] | None = None,
) -> List[Dict]:
    history: List[Dict] = []

    # Simple thresholds for demo
    subject_explosion_score = subject.foam + subject.rage
    echo_explosion_score = echo.competitiveness + echo.numbness

    print("=== EXPLOSION CHECK ===")
    print("  Subject score:", subject_explosion_score)
    print("  Echo    score:", echo_explosion_score)
    print()

    # If pattern not specified, pick based on scores
    if pattern is None:
        if subject_explosion_score >= echo_explosion_score:
            pattern = "MERGE"
        else:
            pattern = "REPLACEMENT"

    # Log pre-explosion state
    history.append(log_step("pre_explosion", subject, echo))
    print(f">>> BIDIRECTIONAL EXPLOSION – pattern = {pattern}\n")

    if pattern == "MERGE":
        history.extend(apply_merge_nullification(subject, echo))
    elif pattern == "REPLACEMENT":
        history.extend(apply_replacement_nullification(subject, echo))
    else:
        # Fallback: just log that nothing happened
        history.append(log_step("no_pattern_applied", subject, echo))

    return history


def apply_merge_nullification(
    subject: HormonalState, echo: HormonalState
) -> List[Dict]:
    history: List[Dict] = []

    hybrid = HormonalState(
        fear=(subject.fear + echo.fear) / 2,
        rage=subject.rage + echo.rage * 0.6,
        foam=(subject.foam + echo.foam) * 0.7,
        attachment_world=max(subject.attachment_world, echo.attachment_world),
        attachment_other=0,  # internalised
        numbness=(subject.numbness + echo.numbness) / 2 + 10,
        competitiveness=(subject.competitiveness + echo.competitiveness) / 2,
    )

    print("[MERGE_NULLIFICATION] Hybrid subject created\n")
    state = {
        "tag": "merge_nullification_hybrid",
        "hybrid": asdict(hybrid),
        "source_subject": asdict(subject),
        "source_echo": asdict(echo),
    }
    print("  Hybrid:", state["hybrid"])
    print()
    history.append(state)
    return history


def apply_replacement_nullification(
    subject: HormonalState, echo: HormonalState
) -> List[Dict]:
    history: List[Dict] = []

    # Echo takes over; Subject becomes ghost-like
    subject.foam *= 0.2
    subject.numbness += 25
    subject.attachment_world *= 0.3
    subject.attachment_other *= 0.1

    echo.foam += subject.foam * 0.3
    echo.rage += subject.rage * 0.2
    echo.numbness += 5  # scar from overwriting
    echo.attachment_world *= 1.1

    history.append(log_step("replacement_nullification", subject, echo))
    return history


def simulate_echo_twin(
    pattern: Literal["MERGE", "REPLACEMENT"] | None = None,
) -> List[Dict]:
    subject, echo = init_subject_and_echo()
    global_history: List[Dict] = []

    print("=== INIT ===")
    global_history.append(log_step("init", subject, echo))

    global_history.extend(phase_1_idealised_reflection(subject, echo))
    global_history.extend(phase_2_divergence(subject, echo))
    global_history.extend(phase_3_bidirectional_explosion(subject, echo, pattern))

    return global_history


if __name__ == "__main__":
    # pattern can be "MERGE", "REPLACEMENT", or None (auto-pick)
    simulate_echo_twin(pattern=None)