"""Minimal benchmark helpers for spatial-temporal reasoning (baseline).
"""
import math

__all__ = ["distance", "time_delta"]


def distance(p1, p2):
    """Return Euclidean distance between two 3D points (iterables of length 3)."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


def time_delta(t1, t2):
    """Return absolute difference between two scalar timestamps."""
    return abs(t2 - t1)
