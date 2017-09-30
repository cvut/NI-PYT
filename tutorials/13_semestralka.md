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

### Python klientská knihovna pro nový portál Klasifikace

Více informací bude doplněno později.

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

### CalDAV server pro Sirius

Na FIT funguje API [Sirius], které slouží jako zdroj dat pro aplikaci Fittable a poskytuje exporty rozvrhů ve formátu [iCalendar] (ICS) pro kalendářní aplikace. Nevýhodou exportu ICS je, že kalendářní aplikace neumožňují kalendář modifikovat, případně pokud si uživatel soubor ICS importuje, ztratí možnost synchronizace.

Cílem projektu je exponovat kalendářní data přes standardní protokol [CalDAV] a umožnit uživatelům osobní úpravy rozvrhu. Individuální změny se uloží pro každého uživatele zvlášť (tj. pokud změním poznámku u přednášky, ostatní uživatelé jí neuvidí). Synchronizace změn bude pouze jednosměrná, ze Siria do CalDAV; například pokud si smažu z osobního rozvrhu cvičení, v kalendářní aplikaci jej neuvidím, ale nadále jej uvidím v aplikaci Fittable.

Pro implementaci využijte existující implementace CalDAV pro Python, například [Radicale](http://radicale.org/) nebo [CalendarServer](https://www.calendarserver.org/). Projekt může být implementovaný jako rozšíření stávajícího kalendářního serveru nebo jako samostatná aplikace, která synchronizuje Sirius s CalDAV serverem.

#### Funkční požadavky

Uživatel si bude moci:

* přidat osobní rozvrh do kalendářní aplikace
  * (volitelně) přidat přes CalDAV i ostatní rozvrhy, např. místností, vyučujících a předmětů
* upravit události v osobním rozvrhu z kalendářní aplikace
  * smazat událost
  * změnit název a poznámku události
  * (volitelně) změnit účast u události
  * (volitelně) přesunout událost
  * (volitelně) přidávat přílohy k událostem
* (volitelně) měnit události u jiných rozvrhů, než osobního

Pokud se změní události na straně Siria, změny se projeví v rozvrzích uživatelů. Aplikace však zachová uživatelské změny v událostech (např. pokud se v Siriovi změní čas události, nezmění se poznámka uživatele).

(Volitelně / dle potřeby) Aplikace bude mít webové rozhraní, které uživateli poskytne autentizační údaje pro CalDAV a případně možnost nastavit další volby.

#### Nefunkční požadavky

* Aplikace bude poskytovat CalDAV rozhraní s autentizací pro přístup k rozvrhům uživatelů.
* Aplikace bude uchovávat změny událostí pro každého uživatele.
* Aplikace bude využívat [REST rozhraní pro Sirius](https://cvut.github.io/sirius/docs/api-v1.html), případně ICS export.
* Autentizace bude prováděná jednou z následujících metod:
  * Pomocí autorizačního tokenu unikátního pro každého uživatele z API Sirius.
  * Přes OAuth server FIT.
* Aplikace bude respektovat oprávnění uživatelů stanovená serverem Sirius.
* Aplikace bude ukládat data do vlastní databáze; doporučená je relační databáze PostgreSQL, po diskuzi můžete zvolit i jiné řešení.

#### Kontaktní osoby

ICT oddělení, místnost TH-A:1324

* [Jan Vlnas](https://usermap.cvut.cz/profile/vlnasjan/)
* [Jakub Jirůtka](https://usermap.cvut.cz/profile/jirutjak/)

[Sirius]: https://github.com/cvut/sirius
[iCalendar]: https://en.wikipedia.org/wiki/ICalendar
[CalDAV]: https://en.wikipedia.org/wiki/CalDAV

### Synchronizace Sirius s Google Calendar

Podstata práce je stejná jako u zadání [CalDAV server pro Sirius](#caldav-server-pro-sirius). Google Calendar podporuje přístup přes CalDAV, ale slouží pouze jako CalDAV server, nikoliv klient. Synchronizace s Google Calendar by proto byla řešená samostatnou aplikací, která by importovala data do Google Calendar přes [CalDAV rozhraní](https://developers.google.com/google-apps/calendar/caldav/v2/guide), nebo přes [Google Calendar API](https://developers.google.com/google-apps/calendar/overview).

Aplikace bude mít webové rozhraní, přes které uživatel:

* autorizuje přístup k API Sirius přes OAuth server,
* udělí přístup ke svému Google kalendáři a zvolí do kterého kalendáře se mají události importovat;
  * alternativně mu je zpřístupněn samostatný kalendář ve správě aplikace.

Aplikace musí umožňovat autentizaci proti [Google Apps for Education](https://ict.fit.cvut.cz/~web/current/web/ict/GoogleApps/) na FIT. Volitelně by aplikace mohla pracovat se _zdroji_ ([Calendar Resources](https://support.google.com/a/answer/1686462?hl=en)), pro alokaci místnosti, ve které se událost koná.

Kontaktní osoba: [Jan Vlnas](https://usermap.cvut.cz/profile/vlnasjan/).

### git2edux

[Tento repozitář](https://github.com/cvut/MI-PYT) obsahuje sadu skriptů a jiných souborů,
které obstarávají nahrávání obsahu na Edux.
Podstatou této práce je udělat stejnou věc pořádně, konfigurovatelně a znovupoužitelně.
Pokud se autor nějakého předmětu na FITu rozhodne, že chce tento nástroj využít,
vytvoří konfigurační soubor,
použije předpřipravenou šablonu pro konfigurační soubor Travis CI a je hotovo.
Nástroj by měl umět:

 * zajistit převod Markdown souborů na dokuwiki syntaxi pomocí pandocu
 * umožnit registraci vlastních filtrů aplikovaných před a po převodu
 * aplikovat mapování na Edux filesystem načtené z konfiguračního souboru
 * automaticky nahrávat na Edux obrázky a převádět reference na ně tak, aby fungovaly
 * podporovat nahrávání vlastních souborů z filtrů
 * převádět a nahrávat data na Edux asynchronně pomocí asyncio
 * více nahrávacích mechanismů (HTTP POST a WebDAV)
 * více možností přihlášení u HTTP POST (cookie a jméno s heslem)
 * obsahovat interaktivní průvodce pro vytvoření konfiguračních souborů (vlastního a pro Travis CI)
 * (nástroj by měl být jednoduše rozšířitelný pro použití s jinými CI)

S přístupem do Eduxu a lehkým úvodem do problému může osobně pomoci
[hroncok](http://github.com/hroncok).
