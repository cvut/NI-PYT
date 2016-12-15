Semestrální práce
=================

Součástí hodnocení je semestrální práce. Uvítáme, pokud si vyberete vlastní téma, které budete moci použít v jiném předmětu nebo sami pro sebe.
Téma je třeba nechat si od nás schválit.
Komplexnější témata mohou být po konzultaci s cvičícími uznaná jako jediná podmínka pro splnění předmětu.

Ve všech případech (kromě případných explicitních výjimek) musí práce splňovat tyto požadavky:

 * musí být napsaná v jazyce Python verze 3.3 nebo vyšší (Cython se samozřejmě také počítá),
 * musí splnit zadání, na kterém jsme se dohodli,
 * musí být v gitovém repozitáři,
 * kód musí splňovat [konvence](https://www.python.org/dev/peps/pep-0008/),
 * kód, komentáře i dokumentace musí být v angličtině,
 * commity musí obsahovat vhodně atomické změny a mít vysvětlující message,
 * kód musí být dostatečně pokryt testy (nechceme stanovovat číselnou hranici, použijte selský rozum),
 * projekt musí být zabalen jako pythonní balíček (za zveřejnění na PyPI pod svobodnou licencí jsou body navíc),
 * projekt by měl stavět na nějakém tématu probraném v předmětu MI-PYT.

Pro nerozhodné časem připravíme několik témat, které můžete použít, budeme ale raději, pokud si zvolíte téma vlastní.

Termíny
-------

 * **Téma schváleno do:** 21.12.2016 (předposlední cvičení)
 * **Odevzdáno do:** 31.1.2017 včetně

Volná témata
------------

Následuje seznam témat, které si můžete po dohodě s námi zvolit, pokud nemáte téma vlastní.
V žádném případě není vhodné na zde vypsaném tématu rovnou začít pracovat a doufat, že ho potom prostě jen odevzdáte.
I téma z tohoto seznamu musí být odladěno a schváleno, témata uvedená zde jsou pouze rámcová.

### Eduxator (zabráno)

Existuje rozpracovaný a nikdy nedokončený projekt [Eduxator], který umožňuje
z příkazové řádky zadávat klasifikaci do Eduxu.
Projekt je třeba vzít, oprášit a vylepšit. Zejména je třeba:

 * při komunikaci s Eduxem použít session
 * vylepšit testy (použít betamax a spol.)
 * rozšířit *knihovní* funkcionalitu o zatím nedokončenou část
 * implementovat interaktivní rozhraní pro příkazovou řádku (viz [README](https://github.com/hroncok/eduxator#the-idea))
 * implementovat neinteraktivní rozhraní pro příkazovou řádku
 * implementovat jednoduché REST API ve Flasku nebo jiném microframeworku
 * umožnit autentizaci pomocí jména a hesla, protože autentizace pomocí cookie neškáluje
 * přidat dokumentaci k jednotlivým součástem, aby projekt mohli využít i další vyučující

S přístupem do Eduxu a lehkým úvodem do problému může osobně pomoci
[hroncok](http://github.com/hroncok).

[Eduxator]: https://github.com/hroncok/eduxator

### Odevzdávací mechanismus pro úlohy z předmětu BI-3DT (zabráno)

Studenti předmětu [BI-3DT](https://edux.fit.cvut.cz/courses/BI-3DT/) odevzdávají
tento semestr poprvé domácí úkol na GitHub. Máme v současnosti velmi
komplikovaný a nepěkně napsaný systém, který pomocí Bashe a GitLab CI dokáže
pustit nad všemi odevzdanými úlohami nějaké testy.

Příští semestr bychom však rádi nasadili systém, který umožní studentům
automaticky pouštět testy při pushnutí do vlastního repozitáře
a zobrazovat výsledky těchto testů. Je však žádoucí, aby studenti
neviděli obsah testů, pouze jejich výsledek.

Šlo by o webovou aplikaci, která by po pushnutí provedla testy, výsledky
publikovala na webové stránce s permanentním, ale *tajným* URL a vrátila
GitHubu odkaz a informaci o výsledku. K tomu samozřejmě existuje
[API](https://developer.github.com/v3/repos/statuses/).

Součástí práce by bylo i přepsání [ošklivého testovacího skriptu](https://github.com/3DprintFIT/hedgehog-task/blob/master/runtests.sh)
do Pythonu. Bylo by ale dobré, aby aplikace uměla spouštět jakýkoliv kód,
podobně jako jiné CI systémy.

S úvodem do současného systému může osobně pomoci
[hroncok](http://github.com/hroncok).

### Analýza dat z MARAST kvízů

[MARAST](https://marast.fit.cvut.cz) je systém pro podporu výuky matematiky
na FIT. Jednou z jeho funkcí je testování studentů formou kvízu (*self-test*).
Kvíz je vždy otevřen k odpovídání po jistou dobu a student postupně
odpovídá na zobrazené otázky. Studentovým cílem je získat jistý počet správných
odpovědí přičemž počet zobrazených otázek není nijak omezen. Po špatné
odpovědi, nebo sérii špatných odpovědí, může být studentova možnost
odpovídat na jistou dobu zablokována.

Cílem této semestrální práce je pohrát si se záznamy o odpovídání v kvízech a
provést jejich analýzu. Otevřenou otázkou (nejen) mezi vyučujícími je jak
skutečně studenti ke kvízům přistupují. Nabízí se tedy nejprve zkoumat základní
ukazatele jako nejčastější časy odpovídání, délky odpovídání, vztah k
*deadline*, vliv zablokování kvízu na další odpovídání, atp. Dále by bylo
velmi zajímavé provést shlukování nad vhodně zvolenými parametry a zjistit
různé typy chování a velikost nalezených skupin (např. identifikovat čisté
klikače, studenty kteří odpovídají s malým počtem chyb, studenty, co dlouho
přemýšlí nad otázkou, ale i tak odpovídají špatně, atp.). Lze si vymyslet
i další možné experimenty, v tomto směru žádné meze nejsou.

Pro práci s daty využijte [pandas](http://pandas.pydata.org). Dále mohou
být užitečné [NumPy](http://www.numpy.org), [scikit-learn](https://scikit-learn.org) či [matplotlib](http://matplotlib.org). Jako úvod do související
problematiky lze doporučit stránky [skupiny adaptivního učení](http://www.fi.muni.cz/adaptivelearning/)
na Fakultě informatiky Masarykovy univerzity v Brně.
Výsledkem semestrální práce by měl být balíček umožňující snadné provedení
výpočtů nad budoucími novými daty a případnou integraci přímo do MARASTu
(například by šlo na základě dat z ukončeného kvízu studentovi zobrazovat
zpětnou vazbu ve formě informace o jeho příslušnosti k té které skupině).

Anonymizovaná data za poslední dva roky z předmětů BI-ZMA, BI-LIN, BI-PKM dodá
[kalvotom](http://github/kalvotom) ve formátu CSV, případně v jiném vhodném.
K dispozici jsou údaje o jednotlivých otázkách (okamžik zobrazení a
odpovězení; identifikátor studenta, otázky a kvízu; parametry kvízu).
Po zběžném pohledu se bude jednat přibližně o 200 000 odpovědí v několika
kvízech. Před započetím práce konkrétně probereme jaké metody zvolit a
jaké experimenty provést. V dalším průběhu [kalvotom](https://github.com/kalvotom)
rád pomůže při řešení nejasností (např. co se týče matematické stránky
některých metod).

