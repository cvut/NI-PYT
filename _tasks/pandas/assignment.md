Vašim úkolem za pět bodů je pomocí frameworku Pandas "vyčistit" data od Policie ČR a odpovědět na otázky níže.

Řešení bude zpracováno jako **Jupyter Notebook**, ve kterém bude patrné,
která část kódu připravuje data a která odpovídá na otázky.
Ve druhé části bude pak patrné, která část odpovídá na kterou otázku.
Alternativně je možné řešení odevzdat jako skript v jazyce Python,
kde budou opět patrně oddělené části přípravy a odpovědí;
otázky a odpovědi pak vypisiujte na standardní výstup např. tímto stylem:

    Počet nahlášených krádeží dne 1. 1. 2018:
    448

    Celková délka tras pravidelných obchůzek (km):
    56289

Řešení odevzdejte standardně jako gitový repozitář.
V případě odevzdání přes GitHub (což preferujeme) **dejte přístup** kromě
uživatelů [hroncok](https://github.com/hroncok) a
[MarekSuchanek](https://github.com/MarekSuchanek) i Petru Viktorinovi
(uživatelské jméno [encukou](https://github.com/encukou)).

Repozitář musí obsahovat všechny soubory potřebné k běhu skriptu či Notebooku,
kromě vstupních dat (viz níže).
Můžete předpokládat, že skript/notebook bude spouštěn z kořenového adresáře
repozitáře.

K řešení použijte data zveřejněná Policií ČR (PČR):
[Statistika nehodovosti pro rok 2018](https://www.policie.cz/clanek/statistika-nehodovosti-900835.aspx?q=Y2hudW09Mg%3d%3d).
Konkrétně stahujte **RAR** pro **prosinec** (který obsahuje informace pro celý rok 2018).

Archiv rozbalte. (Toto by neměl být složitý úkol, kdyžtak si o rozbalená data napište nám nebo kolegovi.)

Rozbalená data uložte do adresáře `data` jako `data/2018/00.csv`, `data/2018/01.csv`, ... a `data/2018/CHODCI.csv`. 
Tyto soubory nepřidávejte do repozitáře. Jména souborů přidejte do `.gitignore`
a v `README` uveďte, kde se data dají získat.

Podíváte-li se na data, zjistíte dvě věci:
* Informace jsou nejspíš ve znakové sadě ČSN ISO/IEC 8859-2, jak je u státních institucí v ČR obvyklé. Při otevírání v Pythonu/Pandas vždy použijte `encoding='iso-8859-2'`.
* Je tam spousta čísel, na které potřebujete dekódovací klíč.

Klíč PČR dodává na stránce výše jako „popis položek formuláře“ ve formátu XLSX.
Pro zjednodušení si stáhněte a naimportujte `explanations.py`, kde máte připravené (rovnou jako Pythonní proměnné):

* `file_names` je slovník {jméno souboru: kraj}
* `main_columns` je seznam jmen sloupců v souborech `??.csv` (ve správném pořadí)
* `ped_columns` je seznam jmen sloupců v souboru `CHODCI.csv` (ve správném pořadí)
* `decode_key` je slovník {jméno sloupce: {číslo: význam čísla}}

Soubor uložte do repozitáře jako `explanations.py`.


## Obecná pravidla

Kód musí názorným způsobem vypočítat výsledek ze zadaných dat a nesmí způsobit
neošetřenou výjimku.
V případě Notebooku nesmí neošetřenou výjimku způsobit žádná buňka.

Váš kód **nesmí používat cykly** na procházení jednotlivých záznamů.
Použijte funkcionalitu Pandas.
Na procházení „sloupců“ cyklus použít můžete. („Sloupce“ tu definujeme jako kategorie, jejichž počet by nerostl bez omezení, kdyby rostl počet nehod.)

U úloh, kde je výstupem graf, musí být **graf součást výstupu** Notebooku.
Odevzdáváte-li skript, tento skript musí graf uložit do souboru a odkázat na
něj ze std. výstupu.

Případné grafy musí odpovídat zobrazovaným hodnotám, např. body by neměly být
propojeny čárou, pokud interpolace mezi nimi nedává smysl.

<!-- tímhle je letos nebudeme mást?
Kód musí korektně zpracovávat neznámé hodnoty (např. člověk s neznámým věkem
nemá 0 let).
-->

Nezapomeňte uvést **jednotky** (např. km, %, Kč) v případech, kdy nestačí
samotné číslo. (Viz příklad odpovědí výše.)


## Příprava dat

Vytvořte tabulku (pandas DataFrame) s daty o nehodách v roce 2018.
Jména sloupců (kromě `weekday(p2a)` a `a`-`t`) musí být pojmenované slovně, tak aby se v nich člověk vyznal. (Využijte `explanations.py`.)

Tabulka musí obsahovat všechny informace ze souborů `data/2018/*.csv` a navíc `kraj`, určující kraj ve kterém k nehodě došlo. Každá zaznamenaná nehoda musí odpovídat jednomu řádku v tabulce. (Pozor na to že soubor `CHODCI.csv` se váže k nehodám z ostatních souborů.)
Pro zjednodušení můžete ignorovat **jeden** řádek z `CHODCI.csv`, popíšete-li v `README` co to pro další analýzu znamená.

Tabulka musí mít index s unikátními hodnotami.

Hodnoty tabulky musí být *české popisky* převzaté z číselníku od PČR (resp. z `explanations.py`).

Prázdné sloupce odstraňte.

Tabulku exportujte do souboru `clean-2018.csv`. Tento soubor přidejte do `.gitignore` a nepřidávejte do repozitáře. (Je to vygenerovaný soubor.)


## Otázky a úkoly

* Kolik nehod v roce 2018 PČR zaznamenala?
* Kolik procent zaznamenaných nehod bylo smrtelných?
* Kolik lidí zemřelo při srážce s odrazníkem, patníkem, sloupkem dopravní značky apod.?
* Kolik procent zaznamenaných nehod, které se staly *na kolejích tramvaje*, bylo smrtelných?
* Vyberte **časté výrobní značky** vozidel (např. *Škoda*, *BMW*): ty které se účastnily alespoň padesáti nehod. Vykreslete graf, který pro každou **častou výrobní značku** ukáže procento nehod *v zatáčce* (vzhledem k celkovému počtu nehod vozidel této značky).

  *Například: vozidla značky ŠKODA se účastnila 21421 nehod, z toho 2505 nehod bylo v zatáčce. 2505 z 21421 je 11,7%, graf tedy bude pro značku ŠKODA ukazovat 11,7%.*
  
  Záznamy jako *žádná z uvedených* můžete pro jednoduchost považovat za samostatné značky.


## Referenční řešení

Naše refereční řešení bude k dispozici po termínu.
(Není-li, prosím, stěžujte si nám.)


## Nakonec

Tyto otázky jsou k zamyšlení, není povinné na ně odpovídat.

V čem se situace zlepšila za posledních pět let, od [roku 2013](https://www.policie.cz/clanek/statistika-nehodovosti-900835.aspx?q=Y2hudW09Nw%3d%3d)? Kam se může posunout dál?
