"""
Doctoral SNA quickstart.

This script demonstrates how to connect basic network algorithms with
sociological interpretation. It uses Zachary's karate club graph, a classic
pedagogical network.

Run:
    python examples/doctoral_sna_quickstart.py
"""

from __future__ import annotations

import networkx as nx


def top_items(scores: dict, n: int = 5):
    """Return the top-n nodes by score."""
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)[:n]


def main() -> None:
    # A classic social network: friendships among members of a karate club.
    G = nx.karate_club_graph()

    print("Graph summary")
    print("-------------")
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    print(f"Density: {nx.density(G):.3f}")
    print(f"Transitivity: {nx.transitivity(G):.3f}")
    print()

    # Local visibility / immediate relational activity
    degree = nx.degree_centrality(G)

    # Brokerage / control over shortest paths
    betweenness = nx.betweenness_centrality(G)

    # Prestige through connection to already central actors
    eigenvector = nx.eigenvector_centrality(G, max_iter=1000)

    # Recursive attention / authority
    pagerank = nx.pagerank(G)

    # Embeddedness in a cohesive core
    core_number = nx.core_number(G)

    print("Top degree centrality: local visibility")
    print(top_items(degree))
    print()

    print("Top betweenness centrality: brokerage")
    print(top_items(betweenness))
    print()

    print("Top eigenvector centrality: prestige by association")
    print(top_items(eigenvector))
    print()

    print("Top PageRank: recursive authority")
    print(top_items(pagerank))
    print()

    print("Top k-core values: cohesive embeddedness")
    print(top_items(core_number))
    print()

    communities = list(nx.algorithms.community.greedy_modularity_communities(G))
    print("Communities detected with greedy modularity")
    print("------------------------------------------")
    for i, community in enumerate(communities, start=1):
        print(f"Community {i}: {sorted(community)}")

    print()
    print("Sociological reminder:")
    print(
        "A centrality ranking is not a neutral list of 'important people'. "
        "It depends on the theory of importance encoded by the metric."
    )


if __name__ == "__main__":
    main()
