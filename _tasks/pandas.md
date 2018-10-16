Vašim úkolem za pět bodů je odpovědět na otázky a vyřešit úkoly níže pomocí frameworku Pandas.

Řešení bude zpracováno jako **Jupyter Notebook**, ve kterém bude patrné,
která část kódu odpovídá na kterou otázku.
Případně je možné řešení odevzdat nebo jako skript v jazyce Python,
který otázky a odpovědi bude vypisovat na standardní výstup např. tímto stylem:

    Počet památných stromů v Brně:
    44

    Celková délka deseti nejdelších řek (km):
    56289

Řešení odevzdejte standardně jako gitový repozitář.
V případě odevzdání přes GitHub (což preferujeme) **dejte přístup** kromě
uživatelů [hroncok](https://github.com/hroncok) a
[MarekSuchanek](https://github.com/MarekSuchanek) i Petrovi Viktorinovi,
(uživatelské jméno [encukou](https://github.com/encukou)).

Repozitář musí obsahovat všechny soubory potřebné k běhu skriptu či Notebooku,
kromě vstupních dat (viz níže).
Můžete předpokládat, že skript/notebook bude spouštěn z kořenového adresáře
repozitáře.

K řešení použijte data z programátorského dotazníku
[**Python Developers Survey**](https://www.jetbrains.com/research/python-developers-survey-2017/#raw-data)
roku 2017.

Soubor se vstupními daty uložte do adresáře `data`, tj. jako
`data/pythondevsurvey2017_raw_data.csv`.
Tento soubor nepřidávejte do repozitáře ([chybí mu licence](https://github.com/python/python-dev-survey/issues/7),
takže se sdílením může být problém). Jméno souboru přidejte do `.gitignore`
a v `README` uveďte, kde se data dají získat.

Kód musí názorným způsobem vypočítat výsledek ze zadaných dat a nesmí způsobit
neošetřenou výjimku.
V případě Notebooku nesmí neošetřenou výjimku způsobit žádná buňka.

Váš kód **nesmí používat cykly** na procházení jednotlivých záznamů.
Použijte funkcionalitu Pandas.
Na procházení „sloupců“ cyklus použít můžete. („Sloupce“ tu definujeme jako kategorie, jejichž počet by nerostl bez omezení, kdyby na dotazník odpovídalo více a více lidí.)

U úloh, kde je výstupem graf, musí být **graf součást výstupu** Notebooku.
Odevzdáváte-li skript, tento skript musí graf uložit do souboru a odkázat na
něj ze std. výstupu.

Případné grafy musí odpovídat zobrazovaným hodnotám, např. body by neměly být
propojeny čárou, pokud interpolace mezi nimi nedává smysl.

Kód musí korektně zpracovávat neznámé hodnoty (např. člověk s neznámým věkem
nemá 0 let).

Nezapomeňte uvést **jednotky** (např. km, %, Kč) v případech, kdy nestačí
samotné číslo. (Viz příklad odpovědí výše.)

## Otázky a úkoly


* Kolik lidí celkem vyplnilo dotazník?
* Kolik z respondentů aktuálně používá Python v nějakém projektu?

  Pro zbytek otázek považujte za "Pythonisty" právě tyto respondenty.

* Kolik Pythonistů z Česka odpovědělo na dotazník? Kolik ze Slovenska?

* Ostatní jazyky, o kterých dotazník mluví, můžeme rozdělit na:
  * staticky typované (Java, C#, C, C++, Objective-C, Go, Scala, SQL, Kotlin, Swift, Rust, TypeScript),
  * dynamicky typované (JavaScript, PHP, Ruby, Bash/Shell, Visual Basic, R, Clojure, Perl, Groovy, CoffeeScript),
  * ostatní (HTML, CSS a ty, které dotazník přímo nezmiňuje) – ty ignorujte.

  Odpovězte na následující otázky:

  * Kolik Pythonistů používá i staticky typované jazyky?

  * Kolik Pythonistů používá i ostatní dynamicky typované jazyky (tedy kromě Pythonu samotného)?

  * Kolik Pythonistů používá jak staticky typované tak dynamicky typované jazyky?

* Vykreslete graf, který **pro každý další jazyk** ukáže procento Pythonistů, kteří:

  * pracují pouze na jednom projektu,
  * pracují na jednom hlavním a několika vedlejších projektech,
  * pracují na více projektech.

  Jazyky, které dotazník nezmiňuje („Ostatní“) ignorujte.
  Zobrazte ale i informace pro „Pouze Python“.


## Referenční řešení

Naše refereční řešení bude k dispozici po termínu.
(Není-li, prosím, stěžujte si nám.)


## Poznámka

[Dotazník pro tento rok](https://surveys.jetbrains.com/s3/c11-python-developers-survey-2018) je právě otevřený. Můžete ho vyplnit.
