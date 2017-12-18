# [semantik] Aufgabe 9 - Marinco Holzinger
from nltk.sem.drt import *
dexpr = DrtExpression.fromstring

# Aufgabe 1
# 1. If Mary listens to music, she dances.
drs1 = dexpr(
    '([], [([m], [m=mary, listen_to_music(m)])->([z], [PRO(z)=x, dance(z)])])'
    )
print(drs1.pretty_format())

print('\n'+'#'*80)
# 2. Mary likes her dog. If it bites, she won't hate it.
drs2 = dexpr(
    '([m, h, d], [m=mary, d=dog, h=d, of(d,h), like(m, d),(([x], [PRO(x)=d,'
    'bite(x)])->([y, z], [PRO(y)=m, PRO(z)=d, -hate(y, z)]))])'
    )
print(drs2.pretty_format())
