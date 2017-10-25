Moduly
======

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/distribution/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/distribution).

Úkol
----

Vaším úkolem za 5 bodů je udělat z vašeho dosavadního projektu balíček
instalovatelný přes pip a nahrát jej na testovací nebo opravdovou PyPI.

Jelikož používáme všichni stejný název aplikace *Labelord*, tak pro PyPI
použijte jako název `labelord_<username>` (v reálných situacích se
nedoporučuje jiný název než je jméno importovatelného modulu). Na
opravdovou PyPI prosím nahrávejte pouze originální díla s nějakou
open-source licencí a vždy pojmenovaná stejně jako je importovatelný modul.

Pokud svůj kód za žádných okolností nechcete zveřejnit ani na testovací PyPI,
dejte nám vědět a domluvíme se.

Podmínky (je jich hodně, ale jsou triviální):

 * Váš balíček musí fungovat (viz zadání předchozích úkolů) po instalaci pomocí pipu do "prázdného" virtualenvu.
   * *Pozn.:* Pokud jste přechozí úkoly nedělali a nebo neprochází testy, můžete použít naše [referenční řešení](https://github.com/MarekSuchanek/labelord).
 * Musí instalovat potřebné závislosti.
 * Musí obsahovat rozumný počet classsifiers a voleb pro `setup.py`.
 * Podpříkaz `sdist` nesmí skončit chybou ani vyvolat varování.
 * Musí splňovat konvence uvedené ve výukových materiálech.
 * Hlavní skript musí jít spouštět pomocí entry pointu `labelord` i pomocí `-m`.
 * Modul musí obsahovat `__init__.py` a logiku importovat z ostatních souborů.
 * Pokud jste již tak neučinili, tak rozdělte aplikaci na jednotlivé
   funkčí celky. Měli byste mít alespoň 3 submoduly, například:
   * `cli` - vstup + výpis na konzoli z prvního úkolu,
   * `web` - flask aplikace,
   * `github` - klient pro komunikaci s GitHub API (společný pro `cli` a
   `web`),
   * případně navíc ještě oddělit logiku práce se štítky či další.
 * Zabalený modul musí obsahovat soubor s textem licence (`LICENSE`, `COPYING`) \*
 * `long_description` musí být načten z `README`

\* Vhodnou licenci můžete najít na [choosealicense.com].
V případě, že váš kód nechcete šířit pod svobodnou licencí,
napište to do souboru vlastní podmínky. Nevymýšlejte si ale prosím vlastní
open-source licence.

[choosealicense.com]: http://choosealicense.com/

Odevzdáte tagem `v0.3` v obvyklém repozitáři
(ten můžete klidně přejmenovat podle modulu - na GitHubu v *Settings*).
Odkaz na (testovací) PyPI můžete napsat někam do README, do release na GitHubu apod.
V každém případě bychom ho měli mít možnost jednoduše najít.

Testy pro automatizované ověření **podmnožiny** povinných podmínek najdete
opět (společně s přechozími testy, kterými by měla aplikace stále projít)
v repozitáři [MarekSuchanek/labelord_tests](https://github.com/MarekSuchanek/labelord_tests)
ve větvi `setup`.
