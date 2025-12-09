"""
Network Visualization

This module provides functions for visualizing networks using matplotlib
and pyvis.
"""

import networkx as nx
from typing import Optional, List, Set, Dict, Union
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def plot_network_matplotlib(
    G: Union[nx.Graph, nx.DiGraph],
    communities: Optional[Union[List[Set], List[List], Dict]] = None,
    node_size: int = 500,
    figsize: tuple = (10, 8),
    layout: str = 'spring',
    show_labels: bool = True,
    title: Optional[str] = None
) -> None:
    """
    Plot a network using matplotlib with optional community coloring.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        The graph to visualize.
    communities : List[Set], List[List], Dict, optional
        Community partition for coloring nodes. Can be:
        - List of sets/lists, where each set/list contains nodes in a community
        - Dict mapping node -> community_id
        If None, all nodes will have the same color. Default is None.
    node_size : int, optional
        Size of nodes in the plot. Default is 500.
    figsize : tuple, optional
        Figure size (width, height) in inches. Default is (10, 8).
    layout : str, optional
        Layout algorithm to use. Options: 'spring', 'circular', 'kamada_kawai',
        'random'. Default is 'spring'.
    show_labels : bool, optional
        If True, display node labels. Default is True.
    title : str, optional
        Title for the plot. Default is None.

    Examples
    --------
    >>> G = nx.karate_club_graph()
    >>> plot_network_matplotlib(G, title="Karate Club Network")
    >>> # This will display the plot (requires matplotlib backend)

    Notes
    -----
    - Requires matplotlib to be installed.
    - The function will display the plot using plt.show().
    - For saving plots, use plt.savefig() after calling this function.
    """
    # Create figure
    plt.figure(figsize=figsize)

    # Choose layout
    if layout == 'spring':
        pos = nx.spring_layout(G, k=1, iterations=50)
    elif layout == 'circular':
        pos = nx.circular_layout(G)
    elif layout == 'kamada_kawai':
        try:
            pos = nx.kamada_kawai_layout(G)
        except:
            pos = nx.spring_layout(G)
    elif layout == 'random':
        pos = nx.random_layout(G)
    else:
        pos = nx.spring_layout(G)

    # Prepare community coloring
    if communities is not None:
        # Convert communities to node -> community_id mapping
        if isinstance(communities, dict):
            node_to_community = communities
        else:
            node_to_community = {}
            for comm_id, comm in enumerate(communities):
                for node in comm:
                    node_to_community[node] = comm_id

        # Get unique communities and assign colors
        num_communities = len(set(node_to_community.values()))
        colors = plt.cm.tab20(range(num_communities))
        node_colors = [colors[node_to_community.get(node, 0)] for node in G.nodes()]
    else:
        node_colors = 'lightblue'

    # Draw the graph
    nx.draw_networkx_nodes(
        G, pos,
        node_color=node_colors,
        node_size=node_size,
        alpha=0.9
    )

    nx.draw_networkx_edges(
        G, pos,
        alpha=0.5,
        edge_color='gray',
        arrows=G.is_directed(),
        arrowsize=20 if G.is_directed() else 0
    )

    if show_labels:
        nx.draw_networkx_labels(G, pos, font_size=10)

    plt.axis('off')
    if title:
        plt.title(title, fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.show()


def export_pyvis_html(
    G: Union[nx.Graph, nx.DiGraph],
    filepath: str,
    communities: Optional[Union[List[Set], List[List], Dict]] = None,
    height: str = "800px",
    width: str = "100%",
    title: str = "Network Visualization"
) -> None:
    """
    Export a network visualization to an interactive HTML file using pyvis.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        The graph to visualize.
    filepath : str
        Path where the HTML file will be saved (e.g., "network.html").
    communities : List[Set], List[List], Dict, optional
        Community partition for coloring nodes. Can be:
        - List of sets/lists, where each set/list contains nodes in a community
        - Dict mapping node -> community_id
        If None, all nodes will have the same color. Default is None.
    height : str, optional
        Height of the visualization in the HTML. Default is "800px".
    width : str, optional
        Width of the visualization in the HTML. Default is "100%".
    title : str, optional
        Title for the HTML page. Default is "Network Visualization".

    Examples
    --------
    >>> G = nx.karate_club_graph()
    >>> export_pyvis_html(G, "karate_club.html")
    >>> # This will create an interactive HTML file

    Notes
    -----
    - Requires pyvis to be installed.
    - The generated HTML file can be opened in any web browser.
    - The visualization is interactive: you can drag nodes, zoom, and pan.
    """
    try:
        from pyvis.network import Network
    except ImportError:
        raise ImportError(
            "pyvis package is required. Install it with: pip install pyvis"
        )

    # Create a pyvis Network object
    if G.is_directed():
        net = Network(directed=True, height=height, width=width, notebook=False)
    else:
        net = Network(directed=False, height=height, width=width, notebook=False)

    # Prepare community coloring
    if communities is not None:
        # Convert communities to node -> community_id mapping
        if isinstance(communities, dict):
            node_to_community = communities
        else:
            node_to_community = {}
            for comm_id, comm in enumerate(communities):
                for node in comm:
                    node_to_community[node] = comm_id

        # Get unique communities and assign colors
        num_communities = len(set(node_to_community.values()))
        # Generate colors for communities
        import colorsys
        colors = []
        for i in range(num_communities):
            hue = i / num_communities
            rgb = colorsys.hsv_to_rgb(hue, 0.7, 0.9)
            hex_color = '#{:02x}{:02x}{:02x}'.format(
                int(rgb[0] * 255),
                int(rgb[1] * 255),
                int(rgb[2] * 255)
            )
            colors.append(hex_color)
    else:
        node_to_community = None
        colors = ['#97c2fc']  # Default light blue

    # Add nodes
    for node in G.nodes():
        node_id = str(node)
        label = str(node)
        comm_id = node_to_community.get(node, 0) if node_to_community else 0
        color = colors[comm_id % len(colors)] if node_to_community else colors[0]

        net.add_node(
            node_id,
            label=label,
            color=color,
            title=f"Node: {node}"
        )

    # Add edges
    for source, target, data in G.edges(data=True):
        weight = data.get('weight', 1.0)
        net.add_edge(
            str(source),
            str(target),
            value=weight,
            title=f"Weight: {weight}"
        )

    # Set physics options for better layout
    net.set_options("""
    {
      "physics": {
        "enabled": true,
        "barnesHut": {
          "gravitationalConstant": -2000,
          "centralGravity": 0.1,
          "springLength": 200,
          "springConstant": 0.04,
          "damping": 0.09
        }
      }
    }
    """)

    # Generate and save HTML
    net.save_graph(filepath)
    print(f"Network visualization saved to {filepath}")

