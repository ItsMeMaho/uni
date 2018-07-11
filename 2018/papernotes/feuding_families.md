# Feuding Families and Former Friends: Unsupervised Learning for Dynamic Fictional Reclationships

**Goals:** unsupervised approach for understanding changing relationship over time of fictional characters. Model learns global relationship descriptors and as well as a trajectory over these descriptors.

## Notes

* identify characters via BookNLP Pipline of Bamman

* take spans with 100 word context windows of two characters

* span is presented trough the average of words from embedding

* concatenate span + character + book embedding

* dictionary learning (for descriptors) -> approximate input as linear combinations from a dictionary

* compute weights over descriptors -> relationship state at given timestep

* enforce model to include linear interpolation of successive timesteps

* discourage system to learn descriptors that are too similar to each other