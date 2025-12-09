# Network Algorithms for Data Science Library

A reusable Python package for network analysis algorithms including community detection and centrality measures.

## Features

This library provides clean and reusable implementations of:

- **Community Detection Algorithms:**
  - Girvan-Newman algorithm for hierarchical community detection
  - Louvain algorithm for fast modularity optimization

- **Centrality Measures:**
  - Degree centrality
  - In-degree and out-degree centrality (for directed graphs)
  - Betweenness centrality
  - Eigenvector centrality
  - Closeness centrality

- **Utilities:**
  - Graph creation and conversion functions
  - Modularity calculation
  - Network visualization (matplotlib and pyvis)

## Installation

### Prerequisites

- Python 3.8 or higher

### Install from source

1. Clone or download this repository
2. Navigate to the project directory
3. Install in editable mode:

```bash
pip install -e .
```

This will install the package and all its dependencies.

### Install dependencies only

```bash
pip install -r requirements.txt
```

## Quick Start

```python
import networkx as nx
import network_algorithms as na

# Create or load a graph
G = nx.karate_club_graph()

# Detect communities using Louvain algorithm
partition, modularity, communities = na.run_louvain(G)
print(f"Found {len(communities)} communities with modularity {modularity:.4f}")

# Detect communities using Girvan-Newman algorithm
communities_gn, mod_gn = na.girvan_newman_communities(G, k=2)
print(f"Found {len(communities_gn)} communities with modularity {mod_gn:.4f}")

# Calculate centrality measures
degree_cent = na.degree_centrality(G)
betweenness_cent = na.betweenness_centrality(G)

# Visualize the network
na.plot_network_matplotlib(G, communities=communities, title="Network with Communities")
```

## Usage Examples

See the `examples/example_usage.py` file for a complete working example that demonstrates:
- Community detection with both algorithms
- Multiple centrality measures
- Graph utilities
- Network visualization

Run the example:

```bash
python examples/example_usage.py
```

## Project Structure

```
network_algorithms/
├── network_algorithms/
│   ├── __init__.py
│   ├── community/
│   │   ├── __init__.py
│   │   ├── newman_girvan.py
│   │   └── louvain.py
│   ├── centrality/
│   │   ├── __init__.py
│   │   └── centrality.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── graph_utils.py
│   └── plotting/
│       ├── __init__.py
│       └── visualize.py
├── examples/
│   └── example_usage.py
├── tests/
│   └── test_algorithms.py
├── requirements.txt
├── setup.py
└── README.md
```

## Testing

Run the test suite:

```bash
python -m pytest tests/
```

Or using unittest:

```bash
python -m unittest tests.test_algorithms
```

## Dependencies

- `networkx`: Graph data structures and algorithms
- `python-louvain`: Louvain community detection algorithm
- `matplotlib`: Static network visualization
- `pyvis`: Interactive HTML network visualization
- `rapidfuzz`: String matching utilities (for future use)

## License

This project is provided as-is for educational and research purposes.

## Contributing

This library is designed to be modular and extensible. Feel free to add new algorithms or improve existing implementations.

## Notes

- The library is designed to work in standard Python environments (no Google Colab dependencies)
- All code is well-documented with docstrings
- Functions are designed to be reusable and modular
- The library supports both directed and undirected graphs where applicable

