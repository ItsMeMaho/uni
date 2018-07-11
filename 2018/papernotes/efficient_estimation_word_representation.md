# Efficient Estimation of Word Representations in Vector Space

**Goal:** produce word-vectors from huge datasets that capture semantic (and syntactic) similarity

## Notes

* computational complexity is given for all models

    - Feedforward Neural Net Language Model (NNLM)

    - Recurrent Neural Net Language Model

but are too complex (non-linearity of Neural Networks), thus simpler model is proposed: 

* Log-linear Models:

    - Continuous Bag-of-Words (CBOW)

        - predict current word based on context

    - Contiuous Skip-gram

        - use current word as input and predict words in certain range (context)

give much faster and good results

## Questions / Thoughts

* we don't capture long dependencies of words

* doesn't include information from subword units/morphology
