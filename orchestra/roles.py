"""
Agent roles for GRA‑Orchestra.
"""
from abc import ABC, abstractmethod


class CriticAgent(ABC):
    def __init__(self, name, taste_vector):
        self.name = name
        self.taste_vector = taste_vector  # e.g., preferences for genres, styles
        self.local_foam_tolerance = 0.3   # how much madness they accept

    @abstractmethod
    def critique(self, composition):
        """Return a score and suggested modifications."""
        pass


class HorrorCritic(CriticAgent):
    def critique(self, composition):
        # Loves tension, darkness, psychological breakdown
        score = self._measure_darkness(composition)
        suggestion = "increase the unresolved dissonance" if score < 0.7 else "keep as is"
        return score, suggestion

    def _measure_darkness(self, comp):
        # dummy
        return 0.8


class ArtHouseCritic(CriticAgent):
    def critique(self, composition):
        score = self._measure_ambiguity(composition)
        suggestion = "add more symbolic layers" if score < 0.6 else "good"
        return score, suggestion

    def _measure_ambiguity(self, comp):
        return 0.7


class DirectorAgent:
    def __init__(self):
        self.global_foam_target = 0.05

    def decide_changes(self, critiques, current_foam):
        """
        Aggregates critiques and proposes structural edits.
        """
        if current_foam > self.global_foam_target:
            return "remove weakest links (elements with highest local foam)"
        else:
            return "freeze – composition is stable"


class ComposerAgent:
    def __init__(self):
        self.sequence = []

    def arrange(self, elements, ordering_constraints):
        """Re‑order elements to minimize global foam."""
        # simplistic: sort by some metric
        self.sequence = sorted(elements, key=lambda x: x.get('id', 0))
        return self.sequence
