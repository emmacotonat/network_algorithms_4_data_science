"""
Louvain Community Detection Algorithm

This module provides a wrapper around the python-louvain library for
community detection using the Louvain algorithm, which is an efficient
greedy optimization method for modularity maximization.
"""

import networkx as nx
from typing import Dict, List, Set, Tuple, Optional, Union
try:
    import community.community_louvain as community_louvain
except ImportError:
    # Fallback import name
    try:
        import community_louvain
    except ImportError:
        raise ImportError(
            "python-louvain package is required. Install it with: pip install python-louvain"
        )

from network_algorithms.utils.graph_utils import calculate_modularity


def run_louvain(
    G: Union[nx.Graph, nx.DiGraph],
    resolution: float = 1.0
) -> Tuple[Dict, float, List[Set]]:
    """
    Detect communities using the Louvain algorithm.

    The Louvain algorithm is a fast and efficient method for community
    detection that optimizes modularity. It works well on both directed
    and undirected graphs.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        A NetworkX graph (directed or undirected). For directed graphs,
        the algorithm will work on the graph as-is, but note that
        python-louvain may convert it to undirected internally.
    resolution : float, optional
        Resolution parameter for modularity. Higher values (e.g., > 1.0)
        tend to find smaller communities, while lower values (e.g., < 1.0)
        tend to find larger communities. Default is 1.0.

    Returns
    -------
    Tuple[Dict, float, List[Set]]
        A tuple containing:
        - Dictionary mapping node -> community_id
        - The modularity value of the partition
        - List of communities, where each community is a set of nodes

    Examples
    --------
    >>> G = nx.karate_club_graph()
    >>> partition, modularity, communities = run_louvain(G)
    >>> len(partition) == len(G.nodes())
    True
    >>> isinstance(modularity, float)
    True
    >>> len(communities) > 0
    True

    Notes
    -----
    - The Louvain algorithm is much faster than Girvan-Newman for large graphs.
    - For directed graphs, python-louvain may convert to undirected internally.
    - The resolution parameter allows tuning the granularity of communities.
    """
    # Convert directed graph to undirected if needed
    # python-louvain works best with undirected graphs
    if G.is_directed():
        G_undirected = G.to_undirected()
    else:
        G_undirected = G

    # Run the Louvain algorithm
    partition = community_louvain.best_partition(
        G_undirected,
        resolution=resolution
    )

    # Calculate modularity using python-louvain's function
    modularity = community_louvain.modularity(partition, G_undirected)

    # Convert partition dict to list of communities (sets of nodes)
    communities_dict = {}
    for node, comm_id in partition.items():
        if comm_id not in communities_dict:
            communities_dict[comm_id] = set()
        communities_dict[comm_id].add(node)

    communities = list(communities_dict.values())

    return partition, modularity, communities

