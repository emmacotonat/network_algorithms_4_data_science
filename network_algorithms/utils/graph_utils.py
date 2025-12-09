"""
Graph Utility Functions

This module provides utility functions for creating, converting, and
analyzing graphs using NetworkX.
"""

import networkx as nx
from typing import List, Tuple, Union, Dict, Set


def create_graph_from_edge_list(
    edge_list: List[Tuple],
    directed: bool = False
) -> nx.Graph:
    """
    Create a NetworkX graph from a list of edges.

    Parameters
    ----------
    edge_list : List[Tuple]
        List of edges. Each edge can be:
        - (source, target) for unweighted edges
        - (source, target, weight) for weighted edges
    directed : bool, optional
        If True, create a directed graph (DiGraph), otherwise create
        an undirected graph (Graph). Default is False.

    Returns
    -------
    nx.Graph or nx.DiGraph
        A NetworkX graph object.

    Examples
    --------
    >>> edges = [(1, 2), (2, 3), (3, 1)]
    >>> G = create_graph_from_edge_list(edges)
    >>> len(G.nodes())
    3
    >>> len(G.edges())
    3

    >>> weighted_edges = [(1, 2, 0.5), (2, 3, 1.0)]
    >>> G = create_graph_from_edge_list(weighted_edges, directed=True)
    >>> G[1][2]['weight']
    0.5
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    for edge in edge_list:
        if len(edge) == 2:
            source, target = edge
            G.add_edge(source, target)
        elif len(edge) == 3:
            source, target, weight = edge
            G.add_edge(source, target, weight=weight)
        else:
            raise ValueError(
                f"Edge tuple must have 2 (source, target) or 3 "
                f"(source, target, weight) elements, got {len(edge)}"
            )

    return G


def graph_to_edge_list(
    G: Union[nx.Graph, nx.DiGraph],
    include_weights: bool = True
) -> List[Tuple]:
    """
    Convert a NetworkX graph to a list of edges.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        The graph to convert.
    include_weights : bool, optional
        If True and edges have weights, include weights in the output.
        If False or edges have no weights, return (source, target) tuples.
        Default is True.

    Returns
    -------
    List[Tuple]
        List of edge tuples. If include_weights is True and edges have
        weights, returns (source, target, weight) tuples.
        Otherwise returns (source, target) tuples.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_edge(1, 2, weight=0.5)
    >>> G.add_edge(2, 3)
    >>> edges = graph_to_edge_list(G, include_weights=True)
    >>> (1, 2, 0.5) in edges
    True
    >>> (2, 3) in edges
    True
    """
    edge_list = []
    for source, target, data in G.edges(data=True):
        if include_weights and 'weight' in data:
            edge_list.append((source, target, data['weight']))
        else:
            edge_list.append((source, target))

    return edge_list


def graph_to_node_list(G: Union[nx.Graph, nx.DiGraph]) -> List:
    """
    Extract a list of all nodes from a graph.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        The graph to extract nodes from.

    Returns
    -------
    List
        List of all nodes in the graph.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_nodes_from([1, 2, 3])
    >>> nodes = graph_to_node_list(G)
    >>> sorted(nodes)
    [1, 2, 3]
    """
    return list(G.nodes())


def calculate_modularity(
    G: Union[nx.Graph, nx.DiGraph],
    communities: Union[List[Set], List[List], Dict]
) -> float:
    """
    Calculate the modularity of a graph partition.

    This function computes modularity using the standard formula.
    It can handle both undirected and directed graphs.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        The graph to calculate modularity for.
    communities : List[Set], List[List], or Dict
        Community partition. Can be:
        - List of sets/lists, where each set/list contains nodes in a community
        - Dict mapping node -> community_id

    Returns
    -------
    float
        The modularity value. Higher values indicate better community structure.

    Examples
    --------
    >>> G = nx.karate_club_graph()
    >>> communities = [{0, 1, 2, 3}, {4, 5, 6, 7}]
    >>> mod = calculate_modularity(G, communities)
    >>> isinstance(mod, float)
    True
    """
    # Convert communities to a consistent format (dict: node -> community_id)
    if isinstance(communities, dict):
        partition = communities
    else:
        # Convert list of sets/lists to dict
        partition = {}
        for comm_id, comm in enumerate(communities):
            for node in comm:
                partition[node] = comm_id

    # Use NetworkX modularity function if available
    try:
        return nx.community.modularity(G, [set(nodes) for nodes in
                                           _partition_to_communities(partition)])
    except AttributeError:
        # Fallback to manual calculation for older NetworkX versions
        return _calculate_modularity_manual(G, partition)


def _partition_to_communities(partition: Dict) -> List[Set]:
    """Convert a partition dict to a list of community sets."""
    communities_dict = {}
    for node, comm_id in partition.items():
        if comm_id not in communities_dict:
            communities_dict[comm_id] = set()
        communities_dict[comm_id].add(node)
    return list(communities_dict.values())


def _calculate_modularity_manual(
    G: Union[nx.Graph, nx.DiGraph],
    partition: Dict
) -> float:
    """
    Manual calculation of modularity (fallback for older NetworkX versions).

    Uses the standard modularity formula:
    Q = (1/(2m)) * sum_ij [A_ij - (k_i * k_j)/(2m)] * delta(c_i, c_j)
    where m is the number of edges, A_ij is the adjacency matrix,
    k_i is the degree of node i, and delta is 1 if nodes are in same community.
    """
    if isinstance(G, nx.DiGraph):
        m = G.number_of_edges()
        if m == 0:
            return 0.0

        # For directed graphs
        in_degree = dict(G.in_degree())
        out_degree = dict(G.out_degree())

        modularity = 0.0
        for u, v in G.edges():
            if partition.get(u) == partition.get(v):
                weight = G[u][v].get('weight', 1.0)
                modularity += weight - (out_degree.get(u, 0) * in_degree.get(v, 0)) / m

        return modularity / m
    else:
        # For undirected graphs
        m = G.number_of_edges()
        if m == 0:
            return 0.0

        degree = dict(G.degree())
        modularity = 0.0

        for u, v in G.edges():
            if partition.get(u) == partition.get(v):
                weight = G[u][v].get('weight', 1.0)
                modularity += weight - (degree.get(u, 0) * degree.get(v, 0)) / (2 * m)

        return modularity / (2 * m)

