Testování
=========

Výukové materiály:
[naucse.python.cz](http://naucse.python.cz/2017/mipyt-zima/intro/testing/),
[GitHub](https://github.com/pyvec/naucse.python.cz/tree/master/lessons/intro/testing).

Úkol
----

Vaším úkolem za 5 bodů je rozšířit testy k dosavadní úloze _labelord_ pomocí
pytestu.
Není nutné použít `flexmock` pokud to nepotřebujete.
Využití `betamax`u je silně doporučeno.

Námi dodávané testy jsou tz. _akceptační_, skoro až _integrační_.
Testují aplikaci z venku, jako black box. Rozšiřte testovací sadu o testy
_jednotkové_: tedy testy, které testují vaše vlastní metody, funkce, třídy apod.

V případě, že jste předchozí úlohy nedělali, můžete použít naše řešení,
na které zde najdete včas odkaz. (Pokud se domníváte, že už by tu měl být, ale
není tu, založte prosím issue.)

Podmínky:

 * Musí fungovat `setup.py test` a to nejen z gitu, ale i při rozbalení archivu `sdist`.
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
