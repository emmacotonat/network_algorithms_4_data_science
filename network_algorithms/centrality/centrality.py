"""
Centrality Measures

This module provides implementations of various centrality measures
for network analysis, including degree, betweenness, eigenvector,
and closeness centrality.
"""

import networkx as nx
from typing import Dict


def degree_centrality(G: nx.Graph) -> Dict:
    """
    Calculate degree centrality for all nodes in the graph.

    Degree centrality measures the number of connections a node has.
    It is normalized by dividing by the maximum possible degree
    (n-1 for a graph with n nodes).

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        A NetworkX graph (directed or undirected).

    Returns
    -------
    Dict
        Dictionary mapping node -> degree centrality value.
        Values range from 0 to 1.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_edges_from([(1, 2), (2, 3), (2, 4)])
    >>> centrality = degree_centrality(G)
    >>> centrality[2] > centrality[1]
    True

    Notes
    -----
    - For undirected graphs, degree centrality counts all connections.
    - For directed graphs, it counts both in-degree and out-degree.
    - Use this measure when you want to identify highly connected nodes.
    """
    return nx.degree_centrality(G)


def in_out_degree_centrality(G: nx.DiGraph) -> Dict[str, Dict]:
    """
    Calculate in-degree and out-degree centrality separately for directed graphs.

    This function returns both in-degree and out-degree centrality measures,
    which are useful for understanding the directionality of connections
    in directed networks.

    Parameters
    ----------
    G : nx.DiGraph
        A directed NetworkX graph.

    Returns
    -------
    Dict[str, Dict]
        Dictionary with two keys:
        - 'in_degree': Dict mapping node -> in-degree centrality
        - 'out_degree': Dict mapping node -> out-degree centrality

    Examples
    --------
    >>> G = nx.DiGraph()
    >>> G.add_edges_from([(1, 2), (2, 3), (3, 2)])
    >>> result = in_out_degree_centrality(G)
    >>> 'in_degree' in result
    True
    >>> 'out_degree' in result
    True
    >>> result['in_degree'][2] > 0
    True

    Notes
    -----
    - In-degree centrality: measures how many nodes point to this node
      (popularity or influence received).
    - Out-degree centrality: measures how many nodes this node points to
      (activity or influence given).
    - Use this for directed networks where directionality matters
      (e.g., citation networks, social media follows).
    """
    if not G.is_directed():
        raise ValueError(
            "in_out_degree_centrality requires a directed graph. "
            "Use degree_centrality() for undirected graphs."
        )

    return {
        'in_degree': nx.in_degree_centrality(G),
        'out_degree': nx.out_degree_centrality(G)
    }


def betweenness_centrality(G: nx.Graph, normalized: bool = True) -> Dict:
    """
    Calculate betweenness centrality for all nodes.

    Betweenness centrality measures how often a node lies on the shortest
    path between pairs of other nodes. Nodes with high betweenness are
    important bridges in the network.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        A NetworkX graph (directed or undirected).
    normalized : bool, optional
        If True, normalize the values by dividing by the maximum possible
        betweenness. Default is True.

    Returns
    -------
    Dict
        Dictionary mapping node -> betweenness centrality value.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_path([1, 2, 3, 4])
    >>> centrality = betweenness_centrality(G)
    >>> centrality[2] > centrality[1]
    True

    Notes
    -----
    - High betweenness indicates nodes that act as bridges or bottlenecks.
    - Useful for identifying critical nodes whose removal would fragment
      the network.
    - Computationally expensive for large graphs (O(n*m) for unweighted,
      O(n*m + n^2*log(n)) for weighted).
    """
    return nx.betweenness_centrality(G, normalized=normalized)


def eigenvector_centrality(G: nx.Graph, max_iter: int = 100, tol: float = 1e-06) -> Dict:
    """
    Calculate eigenvector centrality for all nodes.

    Eigenvector centrality measures a node's importance based on the
    importance of its neighbors. A node is important if it is connected
    to other important nodes.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        A NetworkX graph (directed or undirected).
    max_iter : int, optional
        Maximum number of iterations for the power method. Default is 100.
    tol : float, optional
        Tolerance for convergence. Default is 1e-06.

    Returns
    -------
    Dict
        Dictionary mapping node -> eigenvector centrality value.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 4)])
    >>> centrality = eigenvector_centrality(G)
    >>> len(centrality) == len(G.nodes())
    True

    Notes
    -----
    - Eigenvector centrality considers both the number and quality of connections.
    - Useful for identifying influential nodes in social networks.
    - For directed graphs, use PageRank instead for better results.
    - The algorithm uses the power method to find the principal eigenvector.
    """
    try:
        return nx.eigenvector_centrality(G, max_iter=max_iter, tol=tol)
    except nx.PowerIterationFailedConvergence:
        # Fallback: use a more lenient tolerance
        return nx.eigenvector_centrality(G, max_iter=max_iter * 2, tol=tol * 10)


def closeness_centrality(G: nx.Graph, normalized: bool = True) -> Dict:
    """
    Calculate closeness centrality for all nodes.

    Closeness centrality measures how close a node is to all other nodes
    in the network. It is the inverse of the average shortest path distance
    to all other nodes.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        A NetworkX graph (directed or undirected).
    normalized : bool, optional
        If True, normalize the values. Default is True.

    Returns
    -------
    Dict
        Dictionary mapping node -> closeness centrality value.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_path([1, 2, 3, 4])
    >>> centrality = closeness_centrality(G)
    >>> centrality[2] > centrality[1]
    True

    Notes
    -----
    - High closeness indicates nodes that can quickly reach all other nodes.
    - Useful for identifying nodes that are central in terms of information
      spreading or resource distribution.
    - Requires the graph to be connected. For disconnected graphs, consider
      using harmonic centrality instead.
    - Computationally expensive for large graphs (requires all-pairs shortest paths).
    """
    return nx.closeness_centrality(G, normalized=normalized)

