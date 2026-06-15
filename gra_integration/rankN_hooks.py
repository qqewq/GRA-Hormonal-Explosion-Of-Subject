"""
Higher‑order stability derivatives for aesthetic refinement.
Based on Hierarchical‑Stability‑Rank‑N.
"""
import numpy as np


def first_derivative_of_hormonal_index(H_curve):
    """Approximate first derivative (emotional slope)."""
    return np.gradient(H_curve)


def second_derivative_of_hormonal_index(H_curve):
    """Acceleration of emotional intensity – controls 'explosiveness'."""
    grad = np.gradient(H_curve)
    return np.gradient(grad)


def rankN_correction(phi_history, target_rank=2):
    """
    Adjust nullification to achieve a target 'rank' of aesthetic stability.
    Higher rank = more nuanced control over emotional contours.
    """
    # Placeholder: in real system, this interfaces with Hierarchical-Stability-Rank-N
    # Returns a correction factor for the next GRA step.
    if len(phi_history) < 3:
        return 1.0
    # Simple example: boost reduction if second derivative is high (explosive moment)
    d2 = second_derivative_of_hormonal_index(phi_history)[-1]
    if abs(d2) > 0.1:
        return 1.2
    return 1.0
