# Algorithm Taxonomy for Social Network Analysis

This document maps the main algorithmic families used in Social Network Analysis, network science, computational sociology and graph machine learning.

Each family should be read through four lenses: mathematical object, sociological meaning, research use and limitations.

---

## 1. Graph foundations

| Concept | Description | Sociological meaning |
|---|---|---|
| Node | Actor, organisation, institution, event, document or concept | Unit of relational analysis |
| Edge | Relationship between nodes | Interaction, recognition, exchange, conflict, similarity or co-presence |
| Weight | Edge intensity | Frequency, strength, value or duration |
| Direction | Asymmetric relation | Advice, citation, hierarchy, following, command |
| Signed tie | Positive or negative relation | Trust, support, hostility or conflict |
| Bipartite graph | Two node types | People-events, authors-papers, organisations-projects |
| Multiplex graph | Several tie types among same actors | Friendship, advice, conflict, collaboration, kinship |

Basic measures: density, reciprocity, transitivity, clustering coefficient, components, shortest paths, assortativity and homophily.

---

## 2. Centrality and power

Centrality algorithms define importance in different ways. In sociology, never say that a node is simply "important" without specifying the metric.

| Algorithm | Computes | Sociological reading | Main caution |
|---|---|---|---|
| Degree | Number of direct ties | Visibility, activity, popularity | Local only |
| Strength | Sum of weighted ties | Intensity of direct relational activity | Weight meaning must be justified |
| In-degree | Incoming ties | Prestige, being chosen, attention received | Depends on edge definition |
| Out-degree | Outgoing ties | Activity, outreach, nomination | Can mean effort, not power |
| Closeness | Inverse distance to others | Reachability, speed of access | Weak in disconnected graphs |
| Harmonic closeness | Sum of inverse distances | Robust reachability | Still assumes path relevance |
| Betweenness | Share of shortest paths | Brokerage, mediation, gatekeeping | Assumes geodesic flow |
| Edge betweenness | Bridge edges | Intergroup bridges | Expensive in large networks |
| Eigenvector | Ties to central others | Prestige by association | Core dominance |
| Katz | Attenuated walks | Indirect influence | Parameter sensitive |
| PageRank | Random-walk authority | Recursive attention/status | Not automatically social value |
| HITS | Hubs and authorities | Curators vs recognised authorities | Web-origin assumptions |
| k-core | Cohesive embeddedness | Belonging to field centre | Dense is not always powerful |
| Structural holes | Constraint/effective size | Brokerage advantage | Requires theory of opportunity |

Classical sociological connections: Freeman on centrality, Granovetter on weak ties, Burt on structural holes, Bourdieu on capital and field position.

---

## 3. Cohesion and subgroup detection

| Family | Algorithms | Meaning |
|---|---|---|
| Components | weak/strong components, biconnected components | Integration and fragmentation |
| Cliques | maximal cliques | Perfectly closed groups |
| Relaxed cliques | k-plex, k-clique, k-clan | Cohesive groups in noisy data |
| Cores | k-core, k-truss | Embedded centres |
| Triadic closure | clustering, transitivity | Local closure and social reinforcement |

Cliques are often too strict for empirical sociology. Relaxed cohesive subgroups are usually more realistic.

---

## 4. Community detection

Community algorithms search for meso-level structure: social boundaries, clusters, modules or fields.

| Algorithm | Core idea | Strength | Limitation |
|---|---|---|---|
| Girvan-Newman | Remove high edge-betweenness bridges | Intuitive and pedagogical | Slow |
| Modularity optimisation | More internal ties than null model | Widely used | Resolution limit |
| Louvain | Fast greedy modularity optimisation | Scales well | May produce disconnected communities |
| Leiden | Improves Louvain connectivity | Strong default choice | Resolution still matters |
| Label propagation | Nodes adopt neighbour labels | Very fast | Unstable |
| Infomap | Compress random-walk flows | Good for flow networks | Model assumption specific |
| Spectral clustering | Laplacian eigenvectors | Strong mathematical basis | Parameter-sensitive |
| SBM | Tie probabilities by block | Statistical interpretation | Model assumptions |
| Mixed-membership SBM | Multiple block memberships | Overlapping social positions | More complex inference |
| Clique percolation | Overlapping clique chains | Multiple group belonging | Sensitive to clique size |

Doctoral question: when does an algorithmic cluster correspond to a meaningful social group?

---

## 5. Blockmodelling and role analysis

| Method | Meaning |
|---|---|
| Structural equivalence | Actors connected to the same others; interchangeable positions |
| Regular equivalence | Actors with similar relational roles, even if connected to different alters |
| CONCOR | Classical correlation-based blockmodeling |
| Role discovery / RolX | Automated role extraction from graph features |
| SBM | Model-based positional structure |

Use this family when the research question is about position, role, class fractions, organisational fields or relational equivalence.

---

## 6. Diffusion, contagion and influence

| Algorithm/model | Meaning | Use cases |
|---|---|---|
| Independent cascade | Probabilistic activation through ties | Rumours, information, adoption |
| Linear threshold | Adoption after enough neighbours adopt | Norms, peer pressure, mobilisation |
| Complex contagion | Multiple exposures required | Risky behaviours, political participation |
| Bass diffusion | Innovation adoption curve | Markets and innovations |
| SIR/SIS/SEIR | Compartmental spreading | Disease, information, behaviour analogies |
| Influence maximisation | Choose seeds for maximum spread | Campaigns, interventions, marketing |

Caution: diffusion is not proof of influence. Homophily, shared context and common shocks can produce similar patterns.

---

## 7. Temporal and dynamic networks

| Method | Meaning |
|---|---|
| Temporal paths | Paths that respect time order |
| Dynamic centrality | Changing importance across time |
| Rolling-window networks | Reconstruct relations by period |
| Relational event models | Sequences of actions or interactions |
| TERGM | Temporal exponential random graph models |
| Dynamic SBM | Evolving block structure |
| SAOM / SIENA | Actor-oriented network change |

Temporal networks are essential when order matters: messages, meetings, interactions, contagion, institutional change.

---

## 8. Multilayer, multiplex and heterogeneous networks

| Type | Meaning |
|---|---|
| Multiplex | Same actors, multiple relation types |
| Multilayer | Several layers connected by coupling |
| Heterogeneous graph | Multiple node and edge types |
| Meta-path analysis | Meaningful paths across node/edge types |
| Multilayer modularity | Communities across layers |

Sociological insight: social life is not one-dimensional. Friendship, conflict, work, kinship and digital interaction can overlap or contradict each other.

---

## 9. Signed and semantic networks

| Family | Algorithms/concepts | Meaning |
|---|---|---|
| Balance theory | Balanced/unbalanced triads | Friend/enemy structures |
| Status theory | Signed directed status | Hierarchy and evaluation |
| Signed clustering | Communities with positive/negative ties | Alliances and conflict |
| Trust propagation | Trust and reputation | Credibility networks |
| Semantic networks | Co-occurrence, similarity, topic relations | Meaning, discourse, symbolic fields |

---

## 10. Statistical network models

| Model | Use |
|---|---|
| ERGM | Estimate local mechanisms producing observed networks |
| TERGM | ERGM logic over time |
| SAOM / SIENA | Actor-oriented network evolution |
| Latent space models | Tie probability from latent social distance |
| SBM | Block-based generative model |
| Graphons | Limits and generative structure for large graphs |
| Network autocorrelation | Outcomes affected by neighbours' outcomes |

Statistical models are crucial when the PhD question is explanatory rather than only descriptive.

---

## 11. Embeddings and graph representation learning

| Algorithm | Core idea | Sociological caution |
|---|---|---|
| DeepWalk | Random walks + language model | Latent dimensions need interpretation |
| node2vec | Biased walks: homophily vs structural equivalence | Parameters shape meaning |
| LINE | First/second-order proximity | Proximity is not necessarily relation |
| GraphSAGE | Inductive neighbourhood aggregation | Useful for unseen nodes |
| GCN | Graph convolution | Can oversmooth social differences |
| GAT | Attention over neighbours | Attention is not explanation by itself |

---

## 12. Graph neural networks

Main families: GCN, GraphSAGE, GAT, GIN, heterogeneous GNNs, temporal GNNs and explainable GNNs.

Use cases: node classification, link prediction, recommendation, anomaly detection and representation learning.

Doctoral caution: predictive accuracy is not the same as sociological explanation.

---

## 13. Anomaly detection

Algorithms may detect unusual degree profiles, egonet anomalies, dense fraud rings, temporal bursts, role anomalies or sudden centrality shifts.

Sociological caution: anomaly is not deviance. It is a statistical or structural difference that requires contextual interpretation.

---

## 14. Link prediction and recommendation

Classical algorithms: common neighbours, Jaccard, Adamic-Adar, resource allocation, preferential attachment.

Modern algorithms: matrix factorisation, random walks, embeddings, graph neural recommenders.

Sociological uses: tie formation, opportunity structures, institutional matching and digital platform mediation.

---

## 15. Causal inference with networks

Core problems: interference, spillovers, reflection problem, endogenous tie formation, peer effects, homophily vs influence.

Methods: network experiments, exposure mappings, instrumental variables, longitudinal designs, SAOM, causal diffusion models.

Doctoral warning: causal claims from observational network data require strong assumptions and careful research design.
