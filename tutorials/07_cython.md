C API a Cython
==============

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/lessons/intro/cython/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/cython).

Úkol
----

Vaším úkolem za 5 bodů je zrychlit pomocí Cythonu úkol z předchozího cvičení tak, aby zvládal řešit i bludiště o rozměrech v řádech *nižší jednotky tisíců* × *nižší jednotky tisíců* na moderním počítači (srovnatelném s těmi ve školní učebně) v průměrném čase maximálně 1 sekundu (a volání `.path()` by se u takového bludiště mělo stihnout za sekundu aspoň 50). Úkol musí splňovat všechny náležitosti z minulého týdne + podmínku na čas.

Odevzdávejte s tagem v0.2. Následující příkazy musí po instalaci závislostí z `requirements.txt` fungovat:

```
python setup.py build_ext -i  # sestaví modul napsaný v Cythonu
python -m pytest  # pustí testy
python -c 'from maze import analyze; analyze(...)'  # lze importovat a použít z Pythonu
```
 
Nepoužívejte pyximport.

Pokud řešení úlohy z minula nemáte, nebo si např. chcete rozšířit testy o ty naše,
můžete použít [naše řešení minulé úlohy](https://github.com/encukou/maze).
Nezapomeňte na splnění podmínek licence.

Termín je jako obvykle začátek příštího **prvního** cvičení, tedy středa 11:00.
