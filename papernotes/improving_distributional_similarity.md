# Improving Distributional Similarity with Lessons Learned from Word Embeddings

**Goal:** Show that embedding algorithms aren't superiour per se, but more so system design choices/hyperparameters

## Notes

* Claim: when all methods are allowed to tune similar set of hyperparameters -> performance is largely comparable

* Skip-Gram with negative sampling (SGNS) is implicitly factorizing a word-
context matrix whose cell’s values are PMI,
shifted by a global constant

* Transferable Hyperparameters:

    - Preprocessing

        - dynamic context window

        - subsampling

        - delete rare words

    - association metric

        - shifted PMI

        - context distribution smoothing

    - Post-processing

        - adding context vectors

        - Eigenvalue weighting

        -vector normalization

SGNS only computational efficient way on very large corpus, but in some cases tuning a larger space of hyperparameters more beneficial

## Questions / Thoughts

* a comparison of runtimes would have been nice

* great study overall
