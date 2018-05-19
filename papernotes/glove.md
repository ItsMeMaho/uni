# GloVe: **Glo**bal **Ve**ctors for Word Representation

**Goal:** analyze model properties necessary to produce linear directions of meaning (or answer the Question: *How do word vectors represent meaning?*)

## Notes

* cost function $J = \sum\limits_{i,j = 1}^{V} f(X_{ij}) (w_i^T \tilde{w_j} + b_i + \tilde{b_j} - log X_{ij})^2$

* Model Complexity:

    - worst case: O(V^2)

    - best case: O(|X^0.8|)


## Questions / Thoughts

* See *Improving Distributional Similarity with Lessons Learned from Word Embeddings* [[pdf](https://transacl.org/ojs/index.php/tacl/article/download/570/124)]