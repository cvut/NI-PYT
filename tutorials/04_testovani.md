Testování
=========

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/lessons/intro/testing/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/testing).

Úkol
----

Vaším úkolem za 5 bodů je napsat testy k dosavadním úlohám pomocí pytestu.
Není nutné použít `flexmock` pokud to nepotřebujete.
Využití `betamax`u je silně doporučeno.

Podmínky:

 * Musí fungovat `setup.py test` a to nejen z gitu, ale i při rozbalení archivu z PyPI.
 * Všechny testovací závislosti se musí při uvedeném příkazu nainstalovat.
 * Testy samotné musí fungovat offline a bez nutnosti mít přístupové údaje k API.
 * Spuštění testů i znovu-nahrání kazet musí být zdokumentováno v README.
 * Nahrané kazety musí být v gitu a být součástí balíčku (ale neinstalují se).
 * Žádné nahrané kazety (ani jiné soubory) nesmí obsahovat citlivé údaje.
 * Alespoň část testu by měla být parametrická.
 * Musí být použit nativní způsob pytest testů (pytest umí spouštět i testy pro `unittest` apod.).
 * Testuje se všechno\*.
 * Testy musí běžet i na Travis CI.
 
\* Záměrně nestanovujeme podmínku na 100% pokrytí kódu testy.
Otestujte prostě kód tak, aby byly otestovány všechny podstatné součásti
včetně webové aplikace.
 
Úkol odevzdáváte tradičně s tagem v0.4 a nahráním nové verze na (testovací či pravou) PyPI.
