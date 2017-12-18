from nltk.sem.drt import *
dexpr = DrtExpression.fromstring

drs1 = dexpr('([], [([m], [m=mary, listen_to_music(m)])->([z], [PRO(z)=x, dance(z)])])')
print(drs1.pretty_format())
