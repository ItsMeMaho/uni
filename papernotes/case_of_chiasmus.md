# Syntax Matters for Rhetorical Structure: The Case of Chiasmus

**Goals:** explore the use of syntactic features as a means to improve the quality of chiasmus detection

## Notes

* chiasmi can be ranked using a combination of shallow features like stopwords, conjunction detection, punctuation position, and similarity of n-gram context.

* linear model is used

* adding more Features:

    - POS-Tags

    - Dependency Structures

* Data: from Europarl (4 million words) -> annotate top 200 words => 13 chiasmi found
