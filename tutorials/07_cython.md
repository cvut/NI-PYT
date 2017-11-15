C API a Cython
==============

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/cython/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/cython).

Úkol
----

Vaším úkolem za 5 bodů je zrychlit pomocí Cythonu úkol ze cvičení na NumPy
tak, aby zvládal řešit i simulaci o rozměrech v řádech *nižší jednotky tisíců*
× *nižší jednotky tisíců* na moderním počítači (srovnatelném s těmi ve školní
učebně) v průměrném čase maximálně 15 sekund na chronon.
Náhodné generování takto velké simulace musí trvat méně než čtvrt sekundy.

Úkol musí splňovat všechny náležitosti z úlohy na NumPy + podmínku na čas.

Pokud teprve začínáte, můžete použít [naše řešení minulé úlohy](https://github.com/hroncok/wator).

Doporučujeme využít naše rychlostní testy. Ty najdete opět v repozitáři
[hroncok/wator_tests](https://github.com/hroncok/wator_tests/tree/cython),
ve větvi `cython`.

**Poznámka:** Při přebírání matic `creatures` a `energies` se postarejte o to,
aby měly správný typ. Vaše implementace bude používat nějaký malý a nějaký
velký celočíselný typ, ale testy z minulého týdne typy neřeší a tak do
konstruktoru lezou matice typu `float` (`double`).
Dá se to udělat metodou [astype] (chcete nastavit `copy=False`, abyste
v případě, že typ je v pořádku, nedělali kopii zbytečně).

[astype]: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html

Odevzdávejte s tagem v0.2. Následující příkazy musí po instalaci závislostí
z `requirements.txt` fungovat:

```
python setup.py build_ext -i  # sestaví modul napsaný v Cythonu
python -m pytest <path> # pustí testy
python -c 'from wator import WaTor; WaTor(...)'  # lze importovat a použít z Pythonu
```
 
Nepoužívejte pyximport.
