Moduly
======

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/lessons/intro/distribution/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/distribution).

Úkol
----

Vaším úkolem za 5 bodů je udělat z vašeho dosavadního projektu balíček
instalovatelný přes pip a nahrát jej na testovací nebo opravdovou PyPI.

Na opravdovou PyPI prosím nahrávejte pouze s rozumným názvem a pokud jde o dílo
s nějakou open-source licencí.

Pokud svůj kód za žádných okolností nechcete zveřejnit ani na testovací PyPI,
dejte nám vědět a domluvíme se.

Podmínky (je jich hodně, ale jsou triviální):

 * Váš balíček musí fungovat (viz zadání předchozích úkolů) po instalaci pomocí pipu do "prázdného" virtualenvu.
 * Musí instalovat potřebné závislosti.
 * Musí obsahovat rozumný počet classsifiers a voleb pro `setup.py`.
 * Podpříkaz `sdist` nesmí skončit chybou ani vyvolat varování.
 * Musí splňovat zde uvedené konvence.
 * Hlavní skript musí jít spouštět pomocí entry pointu i pomocí `-m`.
 * Modul musí obsahovat `__init__.py` a logiku importovat z ostatních souborů.
 * Zabalený modul musí obsahovat soubor s textem licence (`LICENSE`, `COPYING`) \*
 * `long_description` musí být načten z `README`

\* Vhodnou licenci můžete najít na [choosealicense.com].
V případě, že váš kód nechcete šířit pod svobodnou licencí,
napište to do souboru vlastní podmínky. Nevymýšlejte si ale prosím vlastní
open-source licence.

[choosealicense.com]: http://choosealicense.com/

Odevzdáte tagem v0.3 v obvyklém repozitáři
(ten můžete klidně přejmenovat podle modulu - na GitHubu v *Settings*).
Odkaz na (testovací) PyPI můžete napsat někam do README, do release na GitHubu apod.
V každém případě bychom ho měli mít možnost jednoduše najít.
