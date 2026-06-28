# Social Network Analysis Algorithms for Doctoral Research

A doctoral-level, research-oriented repository for studying, comparing and implementing algorithms used in **Social Network Analysis (SNA)**, **computational sociology**, **network science** and **graph machine learning**.

The goal is not only to collect algorithms, but to connect each method with sociological reasoning: power, brokerage, cohesion, homophily, diffusion, inequality, social capital, institutional fields, digital platforms and relational structure.

> Working principle: an algorithm is not neutral. In sociology, each metric operationalises a theory of social relations.

---

## What this repository covers

This repository is organised around a broad taxonomy of network methods:

1. **Graph foundations**
   - adjacency matrices, incidence matrices, edge lists
   - directed, undirected, weighted, signed and multiplex graphs
   - paths, walks, geodesics, connected components
   - density, reciprocity, transitivity, assortativity

2. **Centrality and power**
   - degree, strength, closeness, harmonic closeness
   - betweenness, edge betweenness
   - eigenvector centrality, Katz, PageRank, HITS
   - k-core, coreness, structural holes, constraint, effective size

3. **Cohesion and subgroup detection**
   - connected components, biconnected components
   - cliques, k-cliques, k-plexes, k-clans
   - cores, trusses, communities and blocks

4. **Community detection**
   - Girvan-Newman
   - modularity optimisation
   - Louvain and Leiden
   - label propagation
   - Infomap
   - spectral clustering
   - stochastic block models
   - overlapping communities

5. **Blockmodelling and positional analysis**
   - structural equivalence
   - regular equivalence
   - CONCOR
   - role discovery
   - stochastic blockmodels and mixed-membership models

6. **Diffusion, contagion and social influence**
   - independent cascade
   - linear threshold
   - Bass diffusion
   - SIR/SIS/SEIR models
   - complex contagion
   - threshold cascades
   - influence maximisation

7. **Temporal and dynamic networks**
   - temporal paths
   - dynamic centrality
   - event-based graphs
   - relational event models
   - temporal exponential random graph models
   - dynamic stochastic block models

8. **Multilayer, multiplex and heterogeneous networks**
   - multiplex social ties
   - inter-layer coupling
   - multilayer modularity
   - heterogeneous information networks
   - meta-path based measures

9. **Signed, semantic and valued networks**
   - balance theory
   - status theory
   - positive and negative ties
   - trust, conflict and reputation networks
   - semantic similarity and discourse networks

10. **Probabilistic and statistical network models**
    - ERGM
    - TERGM
    - SAOM/SIENA
    - latent space models
    - stochastic block models
    - graphons
    - network autocorrelation models

11. **Graph embeddings and representation learning**
    - DeepWalk
    - node2vec
    - LINE
    - GraphSAGE
    - GCN
    - GAT
    - heterogeneous graph embeddings

12. **Graph neural networks**
    - message passing
    - graph convolutional networks
    - graph attention networks
    - temporal GNNs
    - explainable GNNs
    - sociological cautions about prediction and interpretation

13. **Anomaly, fraud and outlier detection**
    - unusual degree profiles
    - egonet anomalies
    - community outliers
    - temporal bursts
    - role anomalies
    - graph-based fraud detection

14. **Recommendation and link prediction**
    - common neighbours
    - Jaccard, Adamic-Adar, preferential attachment
    - matrix factorisation
    - random walks
    - graph embeddings
    - GNN-based recommendation

15. **Causal inference with networks**
    - interference
    - spillovers
    - peer effects
    - network experiments
    - exposure mappings
    - causal diffusion models
    - homophily vs influence

---

## Repository structure

```text
.
├── README.md
├── docs/
│   ├── algorithm_taxonomy.md
│   ├── doctoral_learning_path.md
│   ├── sociological_interpretation.md
│   ├── implementation_matrix.md
│   └── bibliography.md
├── examples/
│   └── doctoral_sna_quickstart.py
├── notebooks/
│   └── README.md
├── data/
│   └── README.md
├── ROADMAP.md
├── CONTRIBUTING.md
└── network_algorithms/
```

The existing Python package can be progressively expanded with implementations grouped by topic: `centrality`, `community`, `diffusion`, `temporal`, `statistical_models`, `embeddings`, `gnn`, `causal_networks` and `visualization`.

---

## Minimal quick start

```bash
pip install -r requirements.txt
python examples/doctoral_sna_quickstart.py
```

Example:

```python
import networkx as nx

G = nx.karate_club_graph()

degree = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)
pagerank = nx.pagerank(G)

print(sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5])
```

---

## How to read algorithms sociologically

| Algorithmic object | Sociological question |
|---|---|
| Degree | Who is immediately visible, popular or connected? |
| Betweenness | Who brokers between otherwise separated groups? |
| Eigenvector/PageRank | Who is connected to already powerful actors? |
| Modularity/community | Where do social boundaries appear? |
| k-core | Who belongs to the cohesive centre of a field? |
| Structural holes | Who gains advantage from bridging disconnected circles? |
| Homophily measures | How strongly do social attributes organise relations? |
| Diffusion models | How do practices, ideas, rumours or norms spread? |
| ERGM/SAOM | Which micro-mechanisms generate observed structure? |
| Embeddings/GNNs | What latent relational patterns can be learned computationally? |

---

## Recommended Python ecosystem

| Task | Libraries |
|---|---|
| General SNA | NetworkX, igraph, graph-tool |
| Large graphs | graph-tool, SNAP, NetworKit |
| Statistical network models | statnet/ergm in R, RSiena, latentnet |
| Embeddings | node2vec, gensim, PyTorch Geometric |
| GNNs | PyTorch Geometric, DGL |
| Visualisation | matplotlib, pyvis, Gephi, Cytoscape |
| Data handling | pandas, polars, numpy, scipy |
| Reproducible research | Jupyter, Quarto, pytest, pre-commit |

---

## Doctoral research orientation

This repository is designed for research questions such as:

- How are inequalities reproduced through relational structures?
- Which actors occupy brokerage positions in institutional fields?
- How do innovations, rumours, cultural tastes or political frames diffuse?
- Can algorithmic community detection reveal meaningful social boundaries?
- When do detected clusters reflect real social groups, measurement artefacts or platform design?
- How can we distinguish peer influence from homophily?
- What are the epistemological risks of predicting social behaviour from network traces?

---

## Ethical and epistemological cautions

Network analysis can make social relations visible, but it can also oversimplify them. A doctoral use of SNA should always ask:

- What counts as a tie?
- Who is missing from the data?
- Which relations are observable and which remain hidden?
- Does the algorithm reproduce platform, institutional or sampling biases?
- Are we measuring social power, digital visibility or data availability?
- Can the result be interpreted sociologically, or is it only computationally convenient?

---

## Status

This is an evolving doctoral research repository. The current version provides the conceptual and organisational foundation; future versions should add tested implementations, notebooks, datasets and benchmark comparisons.
