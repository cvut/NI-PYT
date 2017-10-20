Pandas
======

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/pandas/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/pandas).

Instalace:

```console
$ python -m venv __venv__
$ . __venv__/bin/activate

$ python -m pip install --upgrade pip wheel
$ python -m pip install notebook pandas matplotlib
```

Soubory ke stažení (do pracovního adresáře):
[actors.csv](http://naucse.python.cz/lessons/intro/pandas/static/actors.csv),
[spouses.csv](http://naucse.python.cz/lessons/intro/pandas/static/spouses.csv).

Úkol
----

Vašim úkolem za pět bodů je odpovědět na otázky a vyřešit úkoly níže.

Řešení může být zpracováno buď jako Jupyter Notebook, ve kterém bude patrné,
která část kódu odpovídá na kterou otázku, nebo jako skript v jazyce Python,
který otázky a odpovědi bude vypisovat na standardní výstup např. tímto stylem:

    Počet památných stromů v Brně:
    44

    Celková délka deseti nejdelších řek (km):
    56289

Repozitář musí obsahovat všechny soubory potřebné k běhu skriptu či Notebooku,
kromě vstupních dat (viz níže).
Můžete předpokládat, že skript/notebook bude spouštěn z kořenového adresáře
repozitáře.

K řešení použijte data z programátorského dotazníku [*Stack Overflow Annual Developer Survey*](https://insights.stackoverflow.com/survey/) roku 2017.
Soubory se vstupními daty uložte do adresáře `data`, tj. jako
`data/survey_results_public.csv` a `data/survey_results_schema.csv`.
Tyto soubory není třeba přidávat do repozitáře; pokud se pro tuto možnost
rozhodnete, vhodně nastavte `.gitignore` a v README uveďte, kde se data dají
získat.

Kód musí názorným způsobem vypočítat výsledek ze zadaných dat a nesmí způsobit
neošetřenou výjimku.
V případě Notebooku nesmí neošetřenou výjimku způsobit žádná buňka.

Váš kód nesmí používat cykly na procházení jednotlivých záznamů.
Použijte funkcionalitu Pandas.
Na procházení sloupců (jejichž počet by se nezměnil, kdyby na dotazník
odpovědělo více lidí) cyklus použít můžete.

U úloh, kde je výstupem graf, skript graf uloží do souboru a odkáže na něj
ze std. výstupu.
U Notebooku musí být grafy součást výstupu.

Případné grafy musí odpovídat zobrazovaným hodnotám, např. body by neměly být
propojeny čárou, pokud interpolace mezi nimi nedává smysl.

Kód musí korektně zpracovávat neznámé hodnoty (např. člověk s neznámým věkem
nemá 0 let).

Nezapomeňte uvést jednotky (např. km, %, Kč) v případech, kdy nestačí samotné
číslo. (Viz příklad odpovědí výše.)

Otázky a úkoly:

* Kolik lidí celkem vyplnilo dotazník?
* Kolik z nich bylo z ČR/SR?
* Jaká je, podle dotazníku, průměrná mzda programátorů v ČR/SR? Ve světě?

* Kolik lidí z ČR/SR uvedlo, že používá* Python?
* Kolik z nich chce v používání* Pythonu pokračovat?
* Kolik lidí Python nepoužívá*, ale chce ho začít používat*?

* Předcházející tři otázky odpovězte také pro Javu místo Pythonu.

* Vykreslete graf, který pro každý programovací jazyk, který lidi z ČR/SR
  uvedli, ukáže průměrnou měsíční mzdu lidí z ČR/SR, kteří tento jazyk
  používají* (podle dat dostupných z dotazníku).

Zkratka „ČR/SR” znamená Česko a Slovensko dohromady; není potřeba udávat
výsledek pro každou z těchto zemí zvlášť.

\* Používání jazyka znamená, že v něm daný člověk poslední rok intenzivně
pracoval.
