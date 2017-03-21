GUI v Pythonu: PyQt5
====================

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/lessons/intro/pyqt/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/pyqt).

Úkol
----

Vaším úkolem za 5 bodů je vytvořit pomocí PyQt5 grafické uživatelské rozhraní,
které umožní vizualizovat a editovat bludiště.
Můžete samozřejmě vyjít z práce na cvičení, ale zbývá toho poměrně dost dodělat.
Rozhraní umožní:

* vytvářet nové bludiště zadaných rozměrů (prázdné, náhodně generované apod., jak chcete)
    * generování náhodného bludiště však musí trvat snesitelně dlouho, v případě nutnosti si vypomožte Cythonem
* ukládat a načítat bludiště ve formě NumPy matic do/ze souborů dle volby uživatele
    * pokud se to nepovede, musí aplikace zobrazit chybové hlášení v grafické podobě (tj. ne jen do konzole)
    * formát souborů viz níže
* prohlížet bludiště v grafické podobě
    * včetně všech objektů v něm a vizualizace cest (viz níže)
    * pokud se bludiště celé nevejde do okna, musí mít posuvníky (jako na cvičení)
    * zoom (např. <kbd>Ctrl</kbd> + kolečko myši) není nutný, ale je příjemný
* klást do bludiště objekty (zdi, cíle, postavy) a odebírat je (tyto změny se projeví v paměti na úrovni NumPy matice)
* automaticky zobrazovat nejkratší cesty mezi postavami a cílem
* nabídka *Help ‣ About* vyvolá okno s informacemi o aplikaci:
    * název
    * stručný popis
    * autor/autoři (vy, případně i my, pokud používáte náš kód)
    * odkaz na repozitář
    * informace o licenci
    * pokud používáte public domain grafiku z [OpenGameArt.org], nemáte právní povinnost zdroj zmínit, ale považujeme to za slušnost

Veškerou potřebnou grafiku najdete v materiálech.

[OpenGameArt.org]: http://opengameart.org/users/kenney

### Objekty a jejich reprezentace v matici

* vystačíte si s jedním typem zdi (-1)
    * pokud to chcete mít později zajímavější, vytvořte si typy dva (-1 a -2)
* jako cíl (1) můžete použít obrázek hradu
* postavy jsou průchozí a je jich 5 různých druhů (2 až 6)
* pokud vaše algoritmy dokáží pracovat jen s jedním cílem, zabraňte vzniku bludiště s více cíli
    * buďto přidání druhého cíle nebude možné
    * nebo se tím odstraní předchozí cíl
* podobně pokud vaše algoritmy neumí pracovat s bludištěm bez cíle, zabraňte vzniku této situace

### Formát souboru s bludištěm

Ukládejte a načítejte bludiště takto, umožní nám to jednodušší kontrolu:

```python
numpy.savetxt(path, array)
array = numpy.loadtxt(path, dtype=numpy.int8)
```

### Zobrazování cesty

* nejkratší cesty od všech postav k cíli zobrazte pomocí obrázků čar z materiálů
* výpočet cesty pro jednu postavu máte připraven z minulých úkolů
    * aplikaci nebudeme testovat na bludiště tisíce krát tisíce jako minulý úkol, ale pro rozumné velikosti (cca do 200 na 200) výpočet musí proběhnout dostatečně svižně, aby aplikace byla použitelná
* musíte si zvolit vhodný způsob, jaky více cest od více postav složit do jedné tak, abyste mohli použít křižovatky apod.
    * *tip:* názvy souborů s čarami nejsou náhodné
    * *tip:* jelikož cesta vede přes políčka, na kterých může být postava nebo cíl, nemůžete cestu ukládat do matice s bludištěm
* výpočet nových cest musíte provést po každé změně bludiště (vytvoření, načtení, přidání/odebrání objektu)
    * kód spojující cesty by měl proto být relativně rychlý (v případě nutnosti si vypomožte Cythonem, ale při vhodně zvoleném algoritmu to není nutné)
* na cestě musí být znázorněny šipky směrem k cíli
    * matici šipek máte opět z úloh z minula, stačí je zobrazit pouze tam, kde jsou čáry
* od některých postav logicky cesta k cíli nemusí existovat, od nich tedy žádnou nevykreslujte (aplikace s takovou situací musí počítat a nesmí spadnout)

![Obrázek bludiště](09-qt/mazepic.png)

### Odevzdání

Jako obvykle. Tag `v0.3`, termín příští středu v 11:00. Pokud teprve začínáte, můžete použít naše [řešení] minulé úlohy (pozor na licenci\*), a nezapomeňte nás pozvat do repozitáře `maze`.

[řešení]: https://github.com/encukou/maze

\* Licence našeho řešení je (zatím) MIT. Při použití PyQt5 ale musíte použít GPL. Což jde, ale někam musíte napsat, že části vašeho programu mají MIT licenci, a přiložit kopii této licence. Abyste to měli jednodušší, dáváme vám souhlas, abyste naše řešení šířili pod stejnou licencí, jako má GPL varianta PyQt5. V takovém případě nás však nezapomeňte uvést jako autory.

Uvítáme, pokud přidáte další testy k nově implementované logice, ale není to nutné.

Aplikace musí jít spustit ve virtualenvu (na systému, pro který jsou PyQt5 wheels na PyPI, a na kterém je nainstalovaný překladač C a hlavičkové soubory Pythonu) takto:

```
python -m pip install -r requirements.txt
python setup.py develop
python -m maze
```

Doporučujeme si sekvenci těchto příkazů vyzkoušet v novém virtualenvu, ať nedochází ke zbytečným chybám.

Aplikace nesmí při žádné akci uživatele zhavarovat (tím nemyslíme, když uživatel udělá z terminálu <kbd>Ctrl</kbd>+<kbd>C</kbd>, ale když např. klikne někam, kde jste to nečekali, nebo zruší dialog pro výběr jména souboru).
Pokud se vám zdá v zadání něco nelogické, prosím, zeptejte se.

