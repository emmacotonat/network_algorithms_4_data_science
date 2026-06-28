# Implementation Matrix

This matrix links algorithm families with recommended tools.

| Family | NetworkX | igraph | graph-tool | SNAP | NetworKit | PyG/DGL | R ecosystem |
|---|---:|---:|---:|---:|---:|---:|---:|
| Basic graph measures | Excellent | Excellent | Excellent | Good | Good | Limited | igraph, sna |
| Centrality | Excellent | Excellent | Excellent | Good | Excellent | Limited | igraph, sna |
| Community detection | Good | Excellent | Excellent | Good | Excellent | Limited | igraph |
| Louvain/Leiden | Add-ons | Excellent | Good | Limited | Good | Limited | igraph, leiden |
| Blockmodelling | Limited | Some | Some | Limited | Limited | Limited | blockmodeling |
| ERGM | Limited | Limited | Limited | No | No | No | statnet/ergm |
| SAOM/SIENA | No | No | No | No | No | No | RSiena |
| Diffusion simulation | Good | Good | Good | Good | Good | Possible | EpiModel |
| Temporal networks | Basic | Basic | Some | Some | Some | Strong | tsna, tergm |
| Multilayer networks | Limited | Some | Some | Limited | Limited | Possible | muxViz, multinet |
| Embeddings | Add-ons | Limited | Limited | Limited | Limited | Strong | limited |
| GNNs | No | No | No | No | No | Excellent | limited |
| Visualisation | Basic | Basic | Basic | Limited | Limited | TensorBoard | ggraph, visNetwork |

---

## Recommended practical stack

### For learning

- NetworkX
- pandas
- matplotlib
- pyvis
- Jupyter

### For larger graphs

- igraph
- graph-tool
- NetworKit

### For statistical network modelling

- R `statnet`
- R `ergm`
- R `RSiena`
- R `latentnet`

### For graph machine learning

- PyTorch Geometric
- DGL
- scikit-learn
- numpy
- scipy

---

## Repository implementation plan

Suggested Python modules:

```text
network_algorithms/
├── centrality/
├── community/
├── cohesion/
├── brokerage/
├── diffusion/
├── temporal/
├── multilayer/
├── signed/
├── statistical_models/
├── embeddings/
├── gnn/
├── causal_networks/
├── datasets/
└── visualization/
```

Each algorithm should include:

1. implementation
2. docstring
3. mathematical explanation
4. sociological interpretation
5. limitations
6. example
7. test
8. reference
