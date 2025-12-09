"""
Girvan-Newman Community Detection Algorithm

This module implements the Girvan-Newman algorithm for community detection,
which identifies communities by progressively removing edges with the highest
betweenness centrality.
"""

import networkx as nx
from typing import List, Set, Tuple, Optional
from network_algorithms.utils.graph_utils import calculate_modularity


def girvan_newman_communities(
    G: nx.Graph,
    k: Optional[int] = None
) -> Tuple[List[Set], float]:
    """
    Detect communities using the Girvan-Newman algorithm.

    The algorithm works by iteratively removing edges with the highest
    edge betweenness centrality. This process naturally reveals the
    community structure of the network.

    Parameters
    ----------
    G : nx.Graph
        An undirected NetworkX graph. The algorithm is designed for
        undirected graphs.
    k : int, optional
        The desired number of communities. If specified, the algorithm
        will stop when k communities are found. If None, the algorithm
        will continue until no edges remain (returning the last valid
        partition). Default is None.

    Returns
    -------
    Tuple[List[Set], float]
        A tuple containing:
        - List of communities, where each community is a set of nodes
        - The modularity value of the partition

    Examples
    --------
    >>> G = nx.karate_club_graph()
    >>> communities, modularity = girvan_newman_communities(G, k=2)
    >>> len(communities)
    2
    >>> isinstance(modularity, float)
    True

    Notes
    -----
    - The algorithm is computationally expensive for large graphs as it
      recalculates betweenness centrality after each edge removal.
    - For large graphs, consider using the Louvain algorithm instead.
    - The algorithm works best on undirected graphs. If a directed graph
      is provided, it will be converted to undirected.
    """
    # Convert to undirected if needed
    if G.is_directed():
        G = G.to_undirected()

    # Make a copy to avoid modifying the original graph
    G_copy = G.copy()

    # If the graph is empty or has no edges, return trivial partition
    if G_copy.number_of_edges() == 0:
        communities = [set(G_copy.nodes())]
        modularity = calculate_modularity(G, communities)
        return communities, modularity

    # Track the best partition found so far
    best_partition = None
    best_modularity = float('-inf')
    best_num_components = 1

    # Continue until we have the desired number of communities or no edges remain
    while G_copy.number_of_edges() > 0:
        # Calculate the number of connected components (communities)
        num_components = nx.number_connected_components(G_copy)

        # Calculate modularity for current partition
        current_communities = [
            set(component) for component in nx.connected_components(G_copy)
        ]
        current_modularity = calculate_modularity(G, current_communities)

        # Update best partition if this is better
        if current_modularity > best_modularity:
            best_modularity = current_modularity
            best_partition = current_communities
            best_num_components = num_components

        # Check if we've reached the desired number of communities
        if k is not None and num_components >= k:
            break

        # Calculate edge betweenness centrality
        edge_betweenness = nx.edge_betweenness_centrality(G_copy)

        # Find edges with maximum betweenness
        max_betweenness = max(edge_betweenness.values())
        edges_to_remove = [
            edge for edge, betweenness in edge_betweenness.items()
            if betweenness == max_betweenness
        ]

        # Remove edges with maximum betweenness
        # If multiple edges have the same max betweenness, remove all of them
        G_copy.remove_edges_from(edges_to_remove)

    # Return the best partition found (or the final partition if k was specified)
    if best_partition is not None:
        return best_partition, best_modularity
    else:
        # Fallback: return components from the final state
        final_communities = [
            set(component) for component in nx.connected_components(G_copy)
        ]
        final_modularity = calculate_modularity(G, final_communities)
        return final_communities, final_modularity

