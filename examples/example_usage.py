"""
Example Usage of Network Algorithms Library

This script demonstrates how to use the network_algorithms library
for community detection and centrality analysis.
"""

import networkx as nx
import network_algorithms as na


def main():
    """
    Main example function demonstrating library usage.
    """
    print("=" * 60)
    print("Network Algorithms Library - Example Usage")
    print("=" * 60)
    print()

    # Create or load a graph
    print("1. Creating a graph (Karate Club Network)...")
    G = nx.karate_club_graph()
    print(f"   Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    print()

    # Example 1: Girvan-Newman Community Detection
    print("2. Running Girvan-Newman algorithm (k=2 communities)...")
    communities_gn, modularity_gn = na.girvan_newman_communities(G, k=2)
    print(f"   Found {len(communities_gn)} communities")
    print(f"   Modularity: {modularity_gn:.4f}")
    print(f"   Community sizes: {[len(c) for c in communities_gn]}")
    print()

    # Example 2: Louvain Community Detection
    print("3. Running Louvain algorithm...")
    partition_louvain, modularity_louvain, communities_louvain = na.run_louvain(G)
    print(f"   Found {len(communities_louvain)} communities")
    print(f"   Modularity: {modularity_louvain:.4f}")
    print(f"   Community sizes: {[len(c) for c in communities_louvain]}")
    print()

    # Example 3: Centrality Measures
    print("4. Calculating centrality measures...")
    
    # Degree centrality
    degree_cent = na.degree_centrality(G)
    top_degree = sorted(degree_cent.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"   Top 5 nodes by degree centrality:")
    for node, cent in top_degree:
        print(f"      Node {node}: {cent:.4f}")
    print()

    # Betweenness centrality
    betweenness_cent = na.betweenness_centrality(G)
    top_betweenness = sorted(betweenness_cent.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"   Top 5 nodes by betweenness centrality:")
    for node, cent in top_betweenness:
        print(f"      Node {node}: {cent:.4f}")
    print()

    # Eigenvector centrality
    eigenvector_cent = na.eigenvector_centrality(G)
    top_eigenvector = sorted(eigenvector_cent.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"   Top 5 nodes by eigenvector centrality:")
    for node, cent in top_eigenvector:
        print(f"      Node {node}: {cent:.4f}")
    print()

    # Closeness centrality
    closeness_cent = na.closeness_centrality(G)
    top_closeness = sorted(closeness_cent.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"   Top 5 nodes by closeness centrality:")
    for node, cent in top_closeness:
        print(f"      Node {node}: {cent:.4f}")
    print()

    # Example 4: Graph Utilities
    print("5. Using graph utilities...")
    edge_list = na.graph_to_edge_list(G, include_weights=False)
    print(f"   Converted graph to edge list: {len(edge_list)} edges")
    node_list = na.graph_to_node_list(G)
    print(f"   Converted graph to node list: {len(node_list)} nodes")
    print()

    # Example 5: Visualization (commented out by default)
    print("6. Visualization options available:")
    print("   - plot_network_matplotlib(G, communities=communities_louvain)")
    print("   - export_pyvis_html(G, 'network.html', communities=communities_louvain)")
    print("   (Uncomment in code to generate visualizations)")
    print()

    # Uncomment the following lines to generate visualizations:
    # print("   Generating matplotlib visualization...")
    # na.plot_network_matplotlib(G, communities=communities_louvain, title="Karate Club - Louvain Communities")
    #
    # print("   Generating interactive HTML visualization...")
    # na.export_pyvis_html(G, "karate_club_network.html", communities=communities_louvain)

    print("=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

