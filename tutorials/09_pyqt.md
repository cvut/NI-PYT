GUI v Pythonu: PyQt5
====================

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/pyqt/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/pyqt).

Úkol
----

Vaším úkolem za 5 bodů je vytvořit pomocí PyQt5 grafické uživatelské rozhraní,
které umožní vizualizovat a editovat simulaci Wa-Tor z úloh na NumPy a
Cython.

Při práci na úkolu doporučujeme adaptovat vytvořený program ze cvičení.

Rozhraní umožní:

* vytvářet novou simulaci zadaných rozměrů (prázdnou, náhodně generovanou apod., jak chcete)
* ukládat a načítat simulaci ve formě NumPy matic do/ze souborů dle volby uživatele
    * pokud se to nepovede, musí aplikace zobrazit chybové hlášení v grafické podobě (tj. ne jen do konzole)
    * formát souborů viz níže
* prohlížet simulaci v grafické podobě
    * včetně obrázků ryb a žraloků
    * pokud se simulace celá nevejde do okna, musí mít posuvníky (jako na cvičení)
      * procházení „okrajem“ mřížky pro simulaci toroidu není nutné
    * zoom (např. <kbd>Ctrl</kbd> + kolečko myši) není nutný, ale je příjemný
      * pro velké odzoomování nahraďte obrázky barvou
* klást do simulace zvířata (ryby, žraloky) a odebírat je (tyto změny se projeví v paměti na úrovni NumPy matice)
    * kvůli zjednodušení zvažujte pouze situaci, že všichni žraloci mají stejnou počáteční energii
    * „věk“ zvířat se při vložení do matice nastaví náhodně
* klikat na tlačítko *Next chronon*, které provede a vizualizuje jedno volání metody `.tick()`
* měnit parametry simulace mezi klikáním na tlačítko z předchozího bodu
* nabídka *Help ‣ About* vyvolá okno s informacemi o aplikaci:
    * název
    * stručný popis
    * autor/autoři (vy, případně i my, pokud používáte náš kód)
    * odkaz na repozitář
    * informace o licenci (pozor na licenci PyQt!)
    * pokud používáte public domain grafiku z [OpenGameArt.org], nemáte právní povinnost zdroj zmínit, ale považujeme to za slušnost

### Grafika

Stejně jako v materiálech, grafiku najdete na [GitHubu](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/pyqt/static/pics).
Je k dispozici pod public domain (tj. „dělej si s tím, co chceš“), pochází ze studia [Kenney]
a je (společně se další volně licencovanou grafikou) ke stažení z [OpenGameArt.org].
(Obrázek žraloka jsme vyrobili z obrázku ryby sami.)

[Kenney]: http://kenney.nl/
[OpenGameArt.org]: http://opengameart.org/users/kenney

 * [water.svg](https://github.com/pyvec/naucse.python.cz/blob/master/lessons/intro/pyqt/static/pics/water.svg)
 * [fish.svg](https://github.com/pyvec/naucse.python.cz/blob/master/lessons/intro/pyqt/static/pics/fish.svg) / [fish2.svg](https://github.com/pyvec/naucse.python.cz/blob/master/lessons/intro/pyqt/static/pics/fish2.svg)
 * [shark.svg](https://github.com/pyvec/naucse.python.cz/blob/master/lessons/intro/pyqt/static/pics/shark.svg)


### Formát souboru se simulací

Ukládejte a načítejte pouze rozložení zvířat a jejich věk. Další parametry neukládejte a při načítání použijte výchozí hodnoty. Ukládání a načítání řešte takto:

```python
numpy.savetxt(path, array)
array = numpy.loadtxt(path, dtype=numpy.int8)
```

To nám umožní testovat vaší implementaci s vlastními soubory.

### Odevzdání

Jako obvykle. Tag `v0.3`. Deadline je prodloužen do pondělí 18.12. včetně.

Pokud teprve začínáte, můžete použít [naše řešení minulé úlohy](https://github.com/hroncok/wator).

Uvítáme, pokud přidáte další testy k nově implementované logice, ale není to nutné.

Aplikace musí jít spustit ve virtualenvu (na systému, pro který jsou PyQt5 wheels na PyPI, a na kterém je nainstalovaný překladač C a hlavičkové soubory Pythonu) takto:

```
python -m pip install -r requirements.txt
python setup.py develop
python -m wator
```

Doporučujeme si sekvenci těchto příkazů vyzkoušet v novém virtualenvu, ať nedochází ke zbytečným chybám.

Aplikace nesmí při žádné akci uživatele zhavarovat (tím nemyslíme, když uživatel udělá z terminálu <kbd>Ctrl</kbd>+<kbd>C</kbd>, ale když např. klikne někam, kde jste to nečekali, nebo zruší dialog pro výběr jména souboru).
Pokud se vám zdá v zadání něco nelogické, prosím, zeptejte se.

