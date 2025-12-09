"""
Network Algorithms for Data Science Library

A reusable Python package for network analysis algorithms including
community detection and centrality measures.
"""

__version__ = "0.1.0"

from network_algorithms.community import (
    girvan_newman_communities,
    run_louvain
)

from network_algorithms.centrality import (
    degree_centrality,
    in_out_degree_centrality,
    betweenness_centrality,
    eigenvector_centrality,
    closeness_centrality
)

from network_algorithms.utils import (
    create_graph_from_edge_list,
    graph_to_edge_list,
    graph_to_node_list,
    calculate_modularity
)

from network_algorithms.plotting import (
    plot_network_matplotlib,
    export_pyvis_html
)

__all__ = [
    # Community detection
    'girvan_newman_communities',
    'run_louvain',
    # Centrality measures
    'degree_centrality',
    'in_out_degree_centrality',
    'betweenness_centrality',
    'eigenvector_centrality',
    'closeness_centrality',
    # Utilities
    'create_graph_from_edge_list',
    'graph_to_edge_list',
    'graph_to_node_list',
    'calculate_modularity',
    # Plotting
    'plot_network_matplotlib',
    'export_pyvis_html',
]

