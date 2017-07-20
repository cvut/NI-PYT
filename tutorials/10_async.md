Generátory a AsyncIO
====================

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/async/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/async).

Úkol
====

Vaším úkolem za 5 bodů je vytvořit asynchronní třídy reprezentující jednotlivé postavy v bludišti a rozhraní umožňující je spustit.

Program musí stále splňovat zadání z předchozího cvičení, zejména:

 * nesmí při žádné interakci uživatele s rozhraním zhavarovat
 * musí se dát nainstalovat a spustit pomocí `python -m pip install -r requirements.txt`; `python setup.py develop`; `python -m maze`

Do programu přidejte rozhraní pro spuštění hry.
Doporučujeme přidat do menu a lišty nástrojů `QAction` s atributem `checkable=True`.
Můžete ale použít i jiný vhodný způsob, kterým lze režim hry zapnout, ale i vypnout (přechod zpět do editačního módu).

Není možné začít hrát, pokud od některé z postav nevede žádná cesta k cíli. Této situaci vhodně zabraňte.

Do vizualizátoru bludiště doplňte funkcionalitu hry. V režimu hry:

 * nebudou zobrazeny čáry od postav k cíli
 * půjde pouze bořit či stavět zdi
  * pokud máte více typů zdí, půjde bořit/stavět pouze jeden druh z nich (`-1`)
  * zeď nepůjde stavět na políčko, kde je aktuálně nějaké postava
  * postavit zeď půjde pouze tehdy, pokud to žádnou postavu neodřízne od cíle
 * nebude vidět paleta
 * úkolem hráče je měnit bludiště tak, aby co nejdéle bránil postavám dojít do cíle
  * v případě že libovolná postava dojde do libovolného cíle, hra končí
   * v takovém případě informujte hráče o tom, jak dlouho vydržel odolávat náporu postav

Máte k dispozici základní třídu `Actor`, která reprezentuje aktora (postavu v bludišti):

 * [class Actor](https://github.com/cvut/MI-PYT/blob/master/tutorials/10-async/actor.py)

Tato třída definuje rozhraní jednotlivých postav a zároveň implementuje základní chování postavy - jde nejkratší cestou k cíli rychlostí jedno políčko za sekundu.
Aby to mohlo fungovat, musí kód, který postavu používá:

 * na začátku hry udělat kopii matici bludiště (aby se bylo možné vrátit do editačního módu) a všechny postavy z ní "vyndat" a inicializovat je jako aktory
 * při zavolání `update_actor(actor)` zjistit, kde se postava nachází a překreslit ji,
 * při ukončení hry nebo programu všem aktorům říct, že se mají zrušit svůj task
   * *tip:* na úklid po skončení hlavní smyčky událostí se hodí `loop.run_until_complete()`

Je třeba použít smyčku událostí z `quamash`.

Rozhraní je definováno tak, aby nezáviselo na konkrétní implementaci vizualizace, uvnitř aktorů byste tedy neměli používat nic z Qt.
Některé charaktery (viz další sekce) možná budou potřebovat použít další API vašeho gridu.

Kromě úpravy rozhraní musíte implementovat několik aktorů, kteří dědí z třídy Actor a chovají se trochu jinak.

Aktoři
------

V bludišti máte 5 typů postav. Každá by měla mít jiné chování.
Každá postava vychází svým chováním ze základního aktora, jde tedy k cíli nejkratší možnou cestou rychlostí jedno políčko za sekundu,
pokud popis neříká jinak.

Zde je seznam různých charakterů. Každé postavě přiřaďte jeden charakter podle typu postavy (barva na obrázku, číslo v matici).

Charakterů je více než 5. Můžete si vybrat, kterých 5 použijete, musíte jich však použít minimálně 5 různých.
Musíte implementovat alespoň dva z hvězdičkou označených charakterů.

Poznámka o rychlostech: Když je nějaká postava rychlejší, neznamená to, že ve vašem cyklu v metodě `behavior` bude dělat delší kroky,
ale že jeden krok bude trvat kratší dobu (metoda `step` má atribut `duration`).

Při rozhodování o chování postav berte v úvahu hratelnost hry.

### Rychlík

Rychlík má stabilně o 75 % vyšší rychlost než základní aktor.

### Zrychlovač

Zrychlovač může po každém kroku s určitou pravděpodobností trvale zvýšit svou rychlost.
Čím déle chodí, tím rychlejší může být. Pravděpodobnost nastavte tak, aby hra byla hratelná; zrychlení tak, aby bylo znatelné (např. o čtvrt políčka za sekundu).
Doporučujeme nastavit i rychlostní strop, případně zrychlovat stále o menší a menší hodnotu.

### Skokan \*

Pokud je za jedním políčkem zdi průchozí políčko, odkud je cesta do cíle alespoň o 5 políček kratší, než z místa, kde se Skokan nachází,
Skokan touto zdí projde (přeskočí ji). Kvůli hratelnosti doporučujeme nastavit limity na to, jak často se toto může dít,
případně zakázat projít zdí přímo na cíl apod.

Chcete-li, můžete implementovat animaci skoku přes zeď.

### Teleportér \*

Teleportér se místo kroku může s určitou pravděpodobností teleportovat na náhodné průchozí a dostupné místo bludiště.
Při teleportu se postavička na malou chvíli rozechvěje, pak se přemístí a po chvilce se přestane chvět.
Celá akce by měla trvat méně než sekundu.
Doporučujeme zakázat teleport na políčka příliš blízko cíli.

### Zmatkář

Zmatkář s určitou pravděpodobností místo kroku směrem k cíli provede krok náhodným průchozím směrem (pokud to je možné, tak jiným, než ze kterého přišel).

### Sprinter

Sprinter zrychluje na rovných trasách.
Pokud půjde klikatou cestou, je stejně pomalý jako základní aktor. Pokud ale půjde déle rovně, může být velmi rychlý.
Na začátku hry a po každé změně směru má rychlost jako základní aktor.
Každý další pohyb ve stejném směru ale vykonává rychleji, než ten předchozí.
Pohyb v jiném směru je opět základní rychlostí.

Doporučujeme nastavit rychlostní strop, případně zrychlovat stále o menší a menší hodnotu.

Poznámka: Sprinter může chodit stejnou cestou jako základní aktor, nemusí cestu optimalizovat pro svoji schopnost.

### Pravák \*

Pravák se pohybuje bludištěm podle [pravidla pravé ruky](https://en.wikipedia.org/wiki/Maze_solving_algorithm#Wall_follower), místo toho, aby šel rovnou nejkratší cestou k cíli.
Pokud má kolem sebe nějakou zeď, jde podél ní.
Pokud se nachází ve volném prostoru a pravidlo nemůže aplikovat (např. na začátku, nebo pokud mu hráč jeho zeď zboří), chová se jako standardní aktor, dokud zeď nenajde nebo nedojde do cíle.

Chcete-li, můžete detekovat, jestli se Pravák někde nezacyklil, a pokud ano, udělat nějaké rozumné kroky k tomu, aby se z prekérní situace dostal.

### Dobíječ

Dobíječ nejprve stojí na místě náhodnou dobu (s exponenciálním rozdělením a střední hodnotou 5 sekund), dobíjí energii.
Pak ujde tolik kroků, kolik celých sekund čekal, rychlostí 3 políčka za sekundu. A opět dobíjí/čeká...
Z dlouhodobého hlediska se tedy pohybuje pomaleji než základní aktor, ale je nevyzpytatelnější.
Při dobíjení si jednou za sekundu poskočí, aby hráč věděl, že tato postava se nezasekla.
(Dobíjení můžete signalizovat nějak sofistikovaněji.)

### Tanečník

Před každým krokem zkontroluje políčko před sebou (tj. ve směru cesty k cíli),
diagonálně vpravo před sebou, a vpravo od sebe. Pokud jsou všechna tři volná, projde je
a vrátí se zpět na původní políčko.
Poté to samé udělá s políčky před sebou, diagonálně vlevo před sebou, a vlevo
od sebe.
Pak teprve udělá krok dopředu.

Pokud hráč políčko, na které by měl Tanečník vstoupit, zastaví zdí,
Tanečník poskočí, zbytek aktuálního "tance" neprovede, a pokračuje z aktuálního políčka.

### Tlusťoch \*

Pohybuje se o 25 % pomaleji než základní aktor.

Nesmí vstoupit na políčko, na kterém je právě jiný aktor.
Měl-li by to udělat, stojí místo toho na místě a odpočívá.

Ostatní aktoři nesmí vstoupit na políčko, kde se právě nachází (nebo na které
právě vstupuje) Tlusťoch. Pohybují se tak, jako by na pozici Tlusťocha byla zeď,
tj. základní aktor se Tlusťocha snaží obejít, a pokud to nejde, skáče na místě.

(Pravák Tlusťocha nepovažuje za zeď, podél které má jít; v případě, že mu Tlusťoch překáží, skáče na místě.
Teleportér se na Tlusťocha nesmí teleportovat.)

Tlusťoch ale nemá vliv na hráčovu schopnost stavět zdi, tj. pro tento účel se
nepočítá jako překážka.

### Smraďoch \*

Smraďoch všem kromě ostatních Smraďochů smrdí, a chtějí od něj pryč.
Pokud je v bezprostředním okolí (určete sami) ostatních aktorů (jiných charakterů), tito aktoři, pokud mohou, jdou směrem pryč od Smraďocha
(bez ohledu na svou plánovanou trasu), až dokud se z dosahu Smraďocha nedostanou.
Pokud nemohou pryč, se smradem se smíří a chovají se normálně.

Při chůzi směrem pryč od Smraďocha se aktoři pohybují rychlostí dle svého charakteru.
Tanečník (pokud může) tančí, Dobíječ (pokud musí) se dobíjí atp.

Je na vás, jestli Smraďoch smrdí i přes zdi. Chcete-li, můžete rozsah smradu vizualizovat.

### Vlastní

Implementujte jiné netriviální chovaní. Svůj záměr popište v README.

Vyhněte se i triviálním variantám jiných chování, které jste již implementovali
(např. máte-li Rychlíka, nedělejte v rámci vlastního zadání "Pomalíka", který je jen o trochu pomalejší než základní aktor.)

Nakolik je chování netriviální, určujeme při hodnocení my.
V případě pochybností se zeptejte pomocí issue nebo na cvičení.


Odevzdání, deadliny apod.
-------------------------

Váš úkol se skládá prakticky ze dvou částí:

 * úprava GUI pro novou funkcionalitu
 * asynchronní programování aktorů

A zároveň je to poslední úkol kromě semestrálky.

Proto na něj máte čas až do středy 28.12. 11:00. Nekažte si ale prosím kvůli úkolu Vánoce (a ani od nás v průběhu svátků nečekejte velkou komunikaci).

Odevzdávejte standardně s tagem `v0.4`. V případě potřeby opět můžete využít naše [řešení](http://github.com/encukou/maze) minulého úkolu.
