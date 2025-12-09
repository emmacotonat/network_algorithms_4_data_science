"""
Tests for Network Algorithms Library

This module contains unit tests for the community detection algorithms
and centrality measures.
"""

import unittest
import networkx as nx
import network_algorithms as na


class TestCommunityDetection(unittest.TestCase):
    """Test cases for community detection algorithms."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a simple test graph with known community structure
        self.G = nx.Graph()
        # Community 1: nodes 0-4
        self.G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
        # Community 2: nodes 5-9
        self.G.add_edges_from([(5, 6), (6, 7), (7, 8), (8, 9), (9, 5)])
        # Bridge between communities
        self.G.add_edge(2, 5)

    def test_girvan_newman_k_communities(self):
        """Test that Girvan-Newman returns the expected number of communities."""
        communities, modularity = na.girvan_newman_communities(self.G, k=2)
        
        self.assertEqual(len(communities), 2, "Should find 2 communities")
        self.assertIsInstance(modularity, float, "Modularity should be a float")
        self.assertGreaterEqual(modularity, -1.0, "Modularity should be >= -1.0")
        self.assertLessEqual(modularity, 1.0, "Modularity should be <= 1.0")
        
        # Check that all nodes are in communities
        all_nodes = set()
        for comm in communities:
            all_nodes.update(comm)
        self.assertEqual(all_nodes, set(self.G.nodes()), "All nodes should be in communities")

    def test_girvan_newman_no_k(self):
        """Test Girvan-Newman without specifying k."""
        communities, modularity = na.girvan_newman_communities(self.G, k=None)
        
        self.assertGreater(len(communities), 0, "Should find at least one community")
        self.assertIsInstance(modularity, float, "Modularity should be a float")

    def test_louvain_partition(self):
        """Test that Louvain returns a valid partition."""
        partition, modularity, communities = na.run_louvain(self.G)
        
        # Check partition is a dict
        self.assertIsInstance(partition, dict, "Partition should be a dictionary")
        
        # Check all nodes are in partition
        self.assertEqual(set(partition.keys()), set(self.G.nodes()),
                        "All nodes should be in partition")
        
        # Check modularity is valid
        self.assertIsInstance(modularity, float, "Modularity should be a float")
        self.assertGreaterEqual(modularity, -1.0, "Modularity should be >= -1.0")
        self.assertLessEqual(modularity, 1.0, "Modularity should be <= 1.0")
        
        # Check communities list
        self.assertIsInstance(communities, list, "Communities should be a list")
        self.assertGreater(len(communities), 0, "Should have at least one community")
        
        # Check all nodes are in communities
        all_nodes = set()
        for comm in communities:
            self.assertIsInstance(comm, set, "Each community should be a set")
            all_nodes.update(comm)
        self.assertEqual(all_nodes, set(self.G.nodes()),
                        "All nodes should be in communities")


class TestCentralityMeasures(unittest.TestCase):
    """Test cases for centrality measures."""

    def setUp(self):
        """Set up test fixtures."""
        self.G = nx.Graph()
        self.G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (1, 3)])

    def test_degree_centrality(self):
        """Test degree centrality returns correct format."""
        centrality = na.degree_centrality(self.G)
        
        self.assertIsInstance(centrality, dict, "Should return a dictionary")
        self.assertEqual(set(centrality.keys()), set(self.G.nodes()),
                        "Should have all nodes")
        
        # Check values are between 0 and 1
        for node, value in centrality.items():
            self.assertGreaterEqual(value, 0.0, f"Node {node} centrality should be >= 0")
            self.assertLessEqual(value, 1.0, f"Node {node} centrality should be <= 1")

    def test_betweenness_centrality(self):
        """Test betweenness centrality returns correct format."""
        centrality = na.betweenness_centrality(self.G)
        
        self.assertIsInstance(centrality, dict, "Should return a dictionary")
        self.assertEqual(set(centrality.keys()), set(self.G.nodes()),
                        "Should have all nodes")
        
        # Check values are non-negative
        for node, value in centrality.items():
            self.assertGreaterEqual(value, 0.0, f"Node {node} centrality should be >= 0")

    def test_eigenvector_centrality(self):
        """Test eigenvector centrality returns correct format."""
        centrality = na.eigenvector_centrality(self.G)
        
        self.assertIsInstance(centrality, dict, "Should return a dictionary")
        self.assertEqual(set(centrality.keys()), set(self.G.nodes()),
                        "Should have all nodes")
        
        # Check values are non-negative
        for node, value in centrality.items():
            self.assertGreaterEqual(value, 0.0, f"Node {node} centrality should be >= 0")

    def test_closeness_centrality(self):
        """Test closeness centrality returns correct format."""
        centrality = na.closeness_centrality(self.G)
        
        self.assertIsInstance(centrality, dict, "Should return a dictionary")
        self.assertEqual(set(centrality.keys()), set(self.G.nodes()),
                        "Should have all nodes")
        
        # Check values are between 0 and 1 (for normalized)
        for node, value in centrality.items():
            self.assertGreaterEqual(value, 0.0, f"Node {node} centrality should be >= 0")
            self.assertLessEqual(value, 1.0, f"Node {node} centrality should be <= 1")

    def test_in_out_degree_centrality_directed(self):
        """Test in/out degree centrality for directed graphs."""
        G_directed = nx.DiGraph()
        G_directed.add_edges_from([(0, 1), (1, 2), (2, 0)])
        
        result = na.in_out_degree_centrality(G_directed)
        
        self.assertIn('in_degree', result, "Should have 'in_degree' key")
        self.assertIn('out_degree', result, "Should have 'out_degree' key")
        
        self.assertEqual(set(result['in_degree'].keys()), set(G_directed.nodes()))
        self.assertEqual(set(result['out_degree'].keys()), set(G_directed.nodes()))

    def test_in_out_degree_centrality_undirected_error(self):
        """Test that in/out degree centrality raises error for undirected graphs."""
        with self.assertRaises(ValueError):
            na.in_out_degree_centrality(self.G)


class TestGraphUtils(unittest.TestCase):
    """Test cases for graph utility functions."""

    def test_create_graph_from_edge_list(self):
        """Test creating a graph from an edge list."""
        edge_list = [(0, 1), (1, 2), (2, 0)]
        G = na.create_graph_from_edge_list(edge_list, directed=False)
        
        self.assertIsInstance(G, nx.Graph, "Should create a Graph")
        self.assertEqual(G.number_of_nodes(), 3)
        self.assertEqual(G.number_of_edges(), 3)

    def test_create_graph_from_weighted_edge_list(self):
        """Test creating a graph from a weighted edge list."""
        edge_list = [(0, 1, 0.5), (1, 2, 1.0)]
        G = na.create_graph_from_edge_list(edge_list, directed=True)
        
        self.assertIsInstance(G, nx.DiGraph, "Should create a DiGraph")
        self.assertEqual(G[0][1]['weight'], 0.5)
        self.assertEqual(G[1][2]['weight'], 1.0)

    def test_graph_to_edge_list(self):
        """Test converting a graph to an edge list."""
        G = nx.Graph()
        G.add_edge(0, 1, weight=0.5)
        G.add_edge(1, 2)
        
        edge_list = na.graph_to_edge_list(G, include_weights=True)
        
        self.assertIsInstance(edge_list, list, "Should return a list")
        self.assertIn((0, 1, 0.5), edge_list, "Should include weighted edge")
        self.assertIn((1, 2), edge_list, "Should include unweighted edge")

    def test_graph_to_node_list(self):
        """Test converting a graph to a node list."""
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3])
        
        node_list = na.graph_to_node_list(G)
        
        self.assertIsInstance(node_list, list, "Should return a list")
        self.assertEqual(set(node_list), {0, 1, 2, 3}, "Should contain all nodes")

    def test_calculate_modularity(self):
        """Test modularity calculation."""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)])
        
        communities = [{0, 1, 2}, {3, 4, 5}]
        modularity = na.calculate_modularity(G, communities)
        
        self.assertIsInstance(modularity, float, "Should return a float")
        self.assertGreater(modularity, 0.0, "Should have positive modularity for clear communities")


if __name__ == '__main__':
    unittest.main()

