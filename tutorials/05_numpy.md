NumPy
=====

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/numpy/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/numpy).

Úkol
----

Vaším úkolem za 5 bodů je vytvořit třídu `WaTor` v modulu `wator`
reprezentující simulaci [Wa-Tor].
Wa-Tor je vodní planeta ve tvaru dvoudimenzionálního toroidu,
na které žijí ryby a žraloci. Čas na planetě Wa-Tor plyne diskrétně
v jednotlivých skocích zvaných chronony. Za každý chronon se ryby a žraloci
pohybují o jedno políčko v mřížce toroidu (pokud je to možné).

Konkrétní pravidla simulace najdete na stránce [Wa-Tor] anglické Wikipedie.

[Wa-Tor]: https://en.wikipedia.org/wiki/Wa-Tor

Třída v konstruktoru přijme dvourozměrnou matici ryb a žraloků, kde 0
představuje prázdné políčko, kladná čísla představují ryby a záporná čísla
představují žraloky. Absolutní hodnota udává, kolik chrononů uplynulo od
poslední reprodukce daného tvora (po reprodukci se resetuje na 1).
Alternativně přijme velikost planety Wa-Tor,
počet ryb a počet žraloků a ty umístí náhodně s náhodným „věkem“.

Dále konstruktor přejímá několik údajů ovlivňujících simulaci
(výchozí hodnoty uvedeny v závorce):

 * po kolika chrononech se reprodukuje ryba (5),
 * po kolika chrononech se reprodukuje žralok (10),
 * jakou mají žraloci počáteční energii (5), volitelně matice energií definována dále,
 * kolik energie dostane žralok po snědení ryby (3).

Můžete předpokládat, že věky nebudou dosahovat stovek a můžete tedy využít
nějaký „malý“ datový typ. Velkost matice však není omezena ničím jiným než
dostupnými prostředky. Žraločí energie také může dosahovat vyšších hodnot.

Poznámka: Pokud se zvíře má zrovna reprodukovat, ale nemůže, protože nemá kam,
nezvedejte mu věk, aby vám hodnoty nepřetekly.
Na chování simulace by to nemělo mít vliv.

Třída bude obsahovat dvě „veřejné“ NumPy matice:

 * `.creatures` (stejný význam jako matice na vstupu),
 * `.energies` (množství energie pro žraloky na daných políčkách - int)

Třída bude obsahovat metodu `.tick()`, která provede uplynutí jednoho chrononu
a pohne rybami a žraloky.
Nejdříve se hýbou ryby, pak žraloci, pak případní hladoví žraloci umírají.
Pohyby v rámci druhu probíhají postupně v libovolném pořadí, dejte si ale
pozor, aby se některé ryby nebo žraloci nepohybovali v jednom chrononu vícekrát.

Když se žralok reprodukuje (dělí), oba jeho potomci mají stejnou energii
(o jedna menší než měl žralok v minulém chrononu). Pokud se žralok reprodukuje
a zároveň jí rybu, novou energii dostane pouze ten, který je na políčku,
kde původně byla ryba.

Dále bude obsahovat metody `.count_fish()` a `.count_sharks()`, které vrátí
počet ryb, respektive žraloků (tato čísla není nutné si uchovávat, stačí je
při zavolání metody zjistit).

Přesné rozhraní a chování třídy je dané přiloženými testy.
Testy najdete v repozitáři [hroncok/wator_tests](https://github.com/hroncok/wator_tests).

Odevzdávání:

* vytvořte si nový privátní git repozitář s názvem `wator` (do něj nás pozvěte, případné kolize s existujícími repozitáři řešte e-mailem);
* pokud ještě nemáte v tabulce hodnocení link na váš GitHub, pošlete nám jej na e-mail;
* na tuto úlohu budou navazovat další, všechny se budou tématicky věnovat simulaci Wa-Tor;
* v repozitáři odevzdávejte pomocí tagu `v0.1`;
* všechny závislosti pro spuštění testů (včetně `numpy` a `pytest`) uveďte v souboru `requirements.txt` (nemusí být s konkrétní verzí);
* naše testy můžete a nemusíte přidat do repozitáře;
* z kořenového adresáře repozitáře musí jít po instalaci závislostí udělat v Pythonu `from wator import WaTor` a nad danou třídou spustit testy.
