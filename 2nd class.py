Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from random import *
from statistics import *
from collections import *
# six roulette wheels -- 18 red 18 black 2 green
choice(['red','red','red','black','black','green'])
'black'
choice(['red','red','red','black','black','green'])
'red'
['red']*18
['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
choice(['red']*18 + ['black']*18 + ['green']*2)
'black'
population = ['red']*18 + ['black']*18 + ['green']*2
choice(population)
'red'
[choice(population) for i in range(6)]
['black', 'green', 'red', 'red', 'black', 'black']
Counter([choice(population) for i in range(6)])
Counter({'black': 3, 'red': 2, 'green': 1})
Counter(choices(population, k=6))
Counter({'black': 4, 'red': 2})
Choices(['red','black','green'],[18,18,2], k=6)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Choices(['red','black','green'],[18,18,2], k=6)
NameError: name 'Choices' is not defined. Did you mean: 'choices'?
choices(['red','black','green'],[18,18,2], k=6)
['black', 'red', 'black', 'red', 'black', 'black']
KeyboardInterrupt
Counter(choices(['red','black','green'],[18,18,2], k=6))
Counter({'red': 5, 'black': 1})
