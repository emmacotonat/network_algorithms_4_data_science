"""
Community Detection Algorithms

This module provides implementations of community detection algorithms
for network analysis.
"""

from network_algorithms.community.newman_girvan import girvan_newman_communities
from network_algorithms.community.louvain import run_louvain

__all__ = [
    'girvan_newman_communities',
    'run_louvain',
]

