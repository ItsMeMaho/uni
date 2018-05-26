# metapath2vec: Scalable Representation Learning for Heterogeneous Networks

**Goals:** representation learning in heterogeneous networks

## Notes

* A meta-path is a sequence of node classes and edge types between two given nodes. Meta-paths can be used to predict the closeness, or similarity, among graph nodes. This is especially useful when an edge between two nodes does not exist.

* formalize the heterogeneous network representation learning problem, where the objective is to simultaneously learn the low-dimensional and latent embeddings for multiple
types of nodes.

* Heterogeneous Network is defined as a graph
G = (V, E, T) 

* Heterogeneous Skip-Gram

* meta-path scheme: "APA" represents coauthor relationships on a paper between two authors. "APVPA" -> two authors A publish papers P at same venue V.

* transition probability by random walkers

* Heterogeneous negative sampling

## Questions / Thoughts

* for experiments in node classification for authors , the evaluation meassure declined with increasing neighborhood size. What is the reason for this? Is this an effect of the negative sampling? Or relying on the metapath patterns used? Or any other explanation?